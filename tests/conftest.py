import asyncio
import os
from typing import AsyncGenerator
from fastapi.testclient import TestClient
import pytest

from scm_staging import app
from py_obs.osc import Osc
from py_obs import project


@pytest.fixture(scope="session")
def test_client() -> TestClient:
    return TestClient(app)


LOCAL_OSC_T = AsyncGenerator[tuple[Osc, Osc], None]


@pytest.fixture(scope="function")
async def local_osc() -> LOCAL_OSC_T:
    yield (
        local := Osc(
            username=os.getenv("OSC_USER", "obsTestUser"),
            password=os.getenv("OSC_PASSWORD", "nots3cr3t"),
            api_url=(api_url := os.getenv("OBS_URL", "http://localhost:3000")),
        )
    ), (admin := Osc(username="Admin", password="opensuse", api_url=api_url))

    await asyncio.gather(local.teardown(), admin.teardown())


HOME_PROJ_T = AsyncGenerator[tuple[Osc, Osc, project.Project, project.Package], None]
