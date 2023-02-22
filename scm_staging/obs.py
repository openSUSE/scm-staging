import aiohttp
import dataclasses
import os
import typing

from scm_staging.logger import LOGGER


@dataclasses.dataclass
class Osc:
    username: str
    password: str

    api_url: str = "https://api.opensuse.org/"

    _session: aiohttp.ClientSession = None

    @staticmethod
    def from_env() -> "Osc":
        if not (username := os.getenv("OSC_USER")):
            raise ValueError("environment variable OSC_USER is not set")
        if not (password := os.getenv("OSC_PASSWORD")):
            raise ValueError("environment variable OSC_PASSWORD is not set")
        return Osc(username=username, password=password)

    async def api_request(
        self,
        route: str,
        payload: bytes | str | None = None,
        params: dict[str, str] | None = None,
        method: typing.Literal["GET", "POST", "PUT", "DELETE"] = "GET",
    ) -> aiohttp.ClientResponse:
        LOGGER.debug(
            "Sending a %s request to %s with the parameters %s and the payload %s",
            method,
            route,
            params,
            payload,
        )
        return await self._session.request(
            method=method, params=params, url=route, data=payload
        )

    def __post_init__(self) -> None:
        self._session = aiohttp.ClientSession(
            auth=aiohttp.BasicAuth(login=self.username, password=self.password),
            raise_for_status=True,
            base_url=self.api_url,
            # https://github.com/openSUSE/open-build-service/issues/13737
            headers={"Accept": "application/xml; charset=utf-8"},
        )

    async def teardown(self) -> None:
        await self._session.close()
