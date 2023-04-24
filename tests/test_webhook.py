import os.path
from fastapi.testclient import TestClient
import pytest
import scm_staging

from scm_staging.webhook import AppConfig
from tests.conftest import LOCAL_OSC_T

PR_EVENTS: dict[str, str] = {}

for event in (
    "pull_request_assign.json",
    "pull_request.json",
    "pull_request_milestone.json",
    "pull_request_review_rejected.json",
    "pull_request_comment.json",
    "pull_request_label.json",
    "pull_request_review_approved.json",
    "pull_request_sync.json",
):
    with open(
        os.path.join(os.path.dirname(__file__), "gitea-webhook", "events", event)
    ) as event_json:
        PR_EVENTS[event[:-5]] = event_json.read(-1)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "payload",
    (pytest.param(json, id=event_name) for event_name, json in PR_EVENTS.items()),
)
async def test_parse_payload_smoke_test(
    payload: str, test_client: TestClient, local_osc: LOCAL_OSC_T
):
    async for osc, _ in local_osc:
        scm_staging.webhook._app_config = AppConfig(
            "irrelevant", "irrelevant", osc, "dest", None, None
        )
        test_client.post("/hook", content=payload)
