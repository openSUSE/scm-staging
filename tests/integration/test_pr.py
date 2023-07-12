import asyncio
from base64 import b64encode
from typing import AsyncGenerator
from py_gitea_opensuse_org import (
    CreatePullRequestOption,
    RepositoryApi,
    UpdateFileOptions,
)
from py_obs.request import search_for_requests
import pytest

from tests.integration.conftest import FakeFactorySetup

pytestmark = pytest.mark.integration


@pytest.mark.asyncio
async def test_create_sr_on_pr(
    fake_factory: AsyncGenerator[FakeFactorySetup, None], repo_api: RepositoryApi
) -> None:
    async for fake_fctr in fake_factory:
        # fork_name = f"{fake_fctr.repo_name}-fork"
        user = fake_fctr.settings.gitea_username
        try:
            # osc = fake_fctr.settings.osc
            # client = fake_fctr.settings.api_client

            repo = await repo_api.create_fork(
                fake_fctr.settings.gitea_username,
                fake_fctr.repo_name,
                body=CreateForkOption(name=fork_name),
            )

            changes = f"{fake_fctr.repo_name}.changes"
            changes_file = await repo_api.repo_get_contents(
                user, fake_fctr.repo_name, changes
            )
            print(changes_file)
            await repo_api.repo_update_file(
                user,
                fake_fctr.repo_name,
                changes,
                UpdateFileOptions(
                    new_branch="for-fctry",
                    sha=changes_file.sha,
                    content=b64encode(
                        bytes("Dummy change\n", encoding="utf8")
                        + b64encode(bytes(changes_file.content or "", encoding="utf8"))
                    ).decode(),
                ),
            )
            await repo_api.repo_create_pull_request(
                user,
                fake_fctr.repo_name,
                body=CreatePullRequestOption(
                    head="for-fctry", base="main", title="Test PR for the fake Factory"
                ),
            )

            # give the bot time to catch up
            await asyncio.sleep(5)

            rqs = await search_for_requests(
                (osc := fake_fctr.settings.osc),
                user=osc.username,
                package=fake_fctr.python_scp,
                project=fake_fctr.fake_factory,
            )
            assert len(rqs) == 1
        finally:
            # await repo_api.repo_delete(user, fake_fctr.repo_name)
            pass
