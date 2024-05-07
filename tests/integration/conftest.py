import asyncio
import json
import subprocess
from base64 import b64encode
import os
from tempfile import TemporaryDirectory
from typing import Any, AsyncGenerator
from py_gitea_opensuse_org import (
    ApiClient,
    Configuration,
    CreateFileOptions,
    CreateHookOption,
    CreateRepoOption,
    RepositoryApi,
    UserApi,
)
from py_obs.osc import Osc
from py_obs.person import Person, PersonRole, StrElementField
from py_obs.project import (
    DevelProject,
    Package,
    PathEntry,
    Project,
    Repository,
    delete,
    fetch_all_files,
    send_meta,
    upload_file_contents,
)
from pydantic import BaseModel, validator
import pytest

from scm_staging.config import BranchConfig


@pytest.fixture(scope="session")
async def api_test_osc() -> AsyncGenerator[Osc, None]:
    if not (pw := os.getenv("OSC_PASSWORD")):
        raise RuntimeError("OSC_PASSWORD environment variable not provided")
    yield (
        osc := Osc(
            username="defolos", password=pw, api_url="https://api-test.opensuse.org"
        )
    )
    await osc.teardown()


@pytest.fixture(scope="session")
def api_client() -> ApiClient:
    if not (api_key := os.getenv("GITEA_API_KEY")):
        raise RuntimeError("GITEA_API_KEY environment variable must be set")

    return ApiClient(
        Configuration(
            api_key={"AuthorizationHeaderToken": api_key},
            api_key_prefix={"AuthorizationHeaderToken": "token"},
            host="https://src.opensuse.org/api/v1",
        )
    )


@pytest.fixture(scope="session")
def repo_api(api_client: ApiClient) -> RepositoryApi:
    return RepositoryApi(api_client)


@pytest.fixture(scope="session")
def user_api(api_client: ApiClient) -> UserApi:
    return UserApi(api_client)


class Settings(BaseModel):
    gitea_api_key: str
    gitea_username: str
    osc: Osc
    api_client: ApiClient
    config_json: str
    hook_ip: str

    class Config:
        arbitrary_types_allowed = True

    @validator("api_client")
    def check_api_client(cls, v: Any) -> ApiClient:
        if not isinstance(v, ApiClient):
            raise ValueError(f"Invalid api_client type {type(v)}")
        return v


@pytest.fixture(scope="session")
async def settings_for_test(
    api_test_osc: AsyncGenerator[Osc, None], api_client: ApiClient
) -> AsyncGenerator[Settings, None]:
    with TemporaryDirectory() as tmp_dir:
        async for osc in api_test_osc:
            user = await UserApi(api_client).user_get_current()
            assert (login := user.login)

            test_hook_config = [
                BranchConfig(
                    target_branch_name="main",
                    organization=login,
                    destination_project=f"home:{osc.username}:factory",
                ).dict()
            ]

            with open(
                conf_json := os.path.join(tmp_dir, "config.json"), "w"
            ) as conf_json_f:
                conf_json_f.write(json.dumps(test_hook_config))

            yield Settings(
                gitea_api_key=os.getenv("GITEA_API_KEY"),
                gitea_username=login,
                osc=osc,
                api_client=api_client,
                config_json=conf_json,
                hook_ip=os.getenv("WEBHOOK_IP"),
            )


@pytest.fixture(scope="session")
async def webhook_container(
    settings_for_test: AsyncGenerator[Settings, None], pytestconfig: pytest.Config
) -> AsyncGenerator[Settings, None]:
    subprocess.run(
        [
            "buildah",
            "bud",
            "--layers",
            "-t",
            "webhook",
            "-f",
            f"{pytestconfig.rootpath / 'Dockerfile.webhook'}",
            str(pytestconfig.rootpath),
        ]
    )
    async for settings in settings_for_test:
        subprocess.run(
            [
                "podman",
                "run",
                "--rm",
                "-d",
                "-p",
                "8000:8000/tcp",
                "-e",
                f'GITEA_API_KEY="{settings.gitea_api_key}"',
                "-e",
                f'OSC_USER="{settings.osc.username}"',
                "-e",
                f'OSC_PASSWORD="{settings.osc.password}"',
                "--name",
                "webhook",
                "-v",
                f"{settings.config_json}:/src/config.json:z",
                "localhost/webhook:latest",
            ],
            check=True,
        )
        yield settings

    subprocess.run(["podman", "stop", "webhook"])
    subprocess.run(["podman", "rm", "-f", "webhook"])


class FakeFactorySetup(BaseModel):
    settings: Settings
    repo_name: str
    fake_factory: Project
    fake_devel_languages_python: Project
    python_scp: Package
    python_scp_devel: Package

    class Config:
        arbitrary_types_allowed = True


@pytest.fixture(scope="session")
async def fake_factory(
    webhook_container: AsyncGenerator[Settings, None], repo_api: RepositoryApi
) -> AsyncGenerator[FakeFactorySetup, None]:
    # user = await user_api.user_get

    async for settings in webhook_container:
        fake_factory, fake_dlp = (
            Project(
                name=name,
                title=StrElementField(title),
                repository=[
                    Repository(
                        name="openSUSE_Factory",
                        arch=["x86_64"],
                        path=[
                            PathEntry(
                                project="openSUSE.org:openSUSE:Factory",
                                repository="snapshot",
                            )
                        ],
                    )
                ],
            )
            for name, title in (
                (f"home:{settings.osc.username}:factory", "Fake Factory"),
                (
                    f"home:{settings.osc.username}:devel:languages:python",
                    "Python Development",
                ),
            )
        )
        pkg_name = "python-scp"

        try:
            await repo_api.create_current_user_repo(
                body=CreateRepoOption(name=pkg_name)
            )

            await asyncio.gather(
                send_meta(settings.osc, prj=fake_factory),
                send_meta(settings.osc, prj=fake_dlp),
            )

            python_scp = Package(
                name=pkg_name,
                title=StrElementField("The python scp package"),
                devel=DevelProject(project=fake_dlp.name, package=pkg_name),
                person=[Person(userid=settings.osc.username, role=PersonRole.BUGOWNER)],
            )
            python_scp_devel = Package(
                name=pkg_name,
                title=python_scp.title,
                scmsync=StrElementField(
                    f"https://src.opensuse.org/{settings.gitea_username}/{pkg_name}"
                ),
            )

            # make this sequential, so that the devel pkg exists before the "factory" package
            await send_meta(settings.osc, prj=fake_dlp, pkg=python_scp_devel)
            await send_meta(settings.osc, prj=fake_factory, pkg=python_scp)
            await upload_file_contents(
                settings.osc,
                prj=fake_factory,
                pkg=python_scp,
                file="_link",
                new_contents="""<link project="openSUSE.org:openSUSE:Factory"/>""",
            )

            files = await fetch_all_files(
                settings.osc, prj=fake_factory, pkg=python_scp, expand_links=True
            )

            # tasks = []
            for fname, contents in files.items():
                await repo_api.repo_create_file(
                    owner=settings.gitea_username,
                    repo=pkg_name,
                    filepath=fname,
                    body=CreateFileOptions(content=b64encode(contents).decode()),
                )

            await repo_api.repo_create_hook(
                owner=settings.gitea_username,
                repo=pkg_name,
                body=CreateHookOption(
                    active=True,
                    config={
                        "content_type": "json",
                        # FIXME: make this url configurable
                        "url": f"http://{settings.hook_ip}:8000/hook",
                        "http-method": "POST",
                    },
                    type="gitea",
                ),
            )

            yield FakeFactorySetup(
                settings=settings,
                repo_name=pkg_name,
                fake_factory=fake_factory,
                fake_devel_languages_python=fake_dlp,
                python_scp_devel=python_scp_devel,
                python_scp=python_scp,
            )

        finally:
            for prj in (fake_factory, fake_dlp):
                try:
                    await delete(settings.osc, prj=prj, force=True)
                except:
                    pass

            await repo_api.repo_delete(settings.gitea_username, pkg_name)
