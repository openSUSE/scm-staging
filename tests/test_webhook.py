import os.path

from tests.conftest import TestWebhook

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


class WebhookSmokeTest(TestWebhook):
    def test_with_recorded_payload(
        self,
    ) -> None:
        for event, json in PR_EVENTS.items():
            print(event)
            res = self.fetch("/hook", method="POST", body=json, raise_error=True)
            assert res

        # self.fetch("/", raise_error=True)
