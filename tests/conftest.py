import os
from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application


from py_obs.osc import Osc

from scm_staging.webhook import AppConfig, make_app


class TestWebhook(AsyncHTTPTestCase):
    def get_app(self) -> Application:
        local = Osc(
            username=os.getenv("OSC_USER", "obsTestUser"),
            password=os.getenv("OSC_PASSWORD", "nots3cr3t"),
            api_url=os.getenv("OBS_URL", "http://localhost:3000"),
        )

        return make_app(
            AppConfig(
                bot_user="foobar",
                branch_name="factory",
                osc=local,
                destination_project="don:t:matter",
                _conf=None,
                _api_client=None,
            )
        )
