import asyncio
import os
from typing import AsyncGenerator
from fastapi.testclient import TestClient
import pytest

from scm_staging import app, project
from scm_staging.obs import Osc
from scm_staging.xml_factory import StrElementField


@pytest.fixture(scope="session")
def test_client() -> TestClient:
    return TestClient(app)


LOCAL_OSC_T = AsyncGenerator[tuple[Osc, Osc], None]


@pytest.fixture(scope="function")
async def local_osc(request: pytest.FixtureRequest) -> LOCAL_OSC_T:
    request.applymarker(pytest.mark.local_obs)
    yield (
        local := Osc(
            username=os.getenv("OSC_USER", "obsTestUser"),
            password=os.getenv("OSC_PASSWORD", "nots3cr3t"),
            api_url=(api_url := os.getenv("OBS_URL", "http://localhost:3000")),
        )
    ), (admin := Osc(username="Admin", password="opensuse", api_url=api_url))

    await asyncio.gather(local.teardown(), admin.teardown())


HOME_PROJ_T = AsyncGenerator[tuple[Osc, Osc, project.Project, project.Package], None]


@pytest.fixture(scope="function")
async def home_project(local_osc: LOCAL_OSC_T) -> HOME_PROJ_T:
    async for osc, admin in local_osc:
        prj = project.Project(
            name=f"home:{osc.username}", title=StrElementField("my home project")
        )
        pkg = project.Package(name="emacs", title="The Emacs package")

        await project.send_meta(osc, prj=prj)
        await project.send_meta(osc, prj=prj, pkg=pkg)

        yield osc, admin, prj, pkg

        await project.delete(osc, prj=prj)
