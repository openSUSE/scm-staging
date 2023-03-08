import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def getGeneralAPISettings(
    api_config_override: Optional[APIConfig] = None,
) -> GeneralAPISettings:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/settings/api"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "get",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return (
                GeneralAPISettings(**response)
                if response is not None
                else GeneralAPISettings()
            )


async def getGeneralAttachmentSettings(
    api_config_override: Optional[APIConfig] = None,
) -> GeneralAttachmentSettings:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/settings/attachment"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "get",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return (
                GeneralAttachmentSettings(**response)
                if response is not None
                else GeneralAttachmentSettings()
            )


async def getGeneralRepositorySettings(
    api_config_override: Optional[APIConfig] = None,
) -> GeneralRepoSettings:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/settings/repository"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "get",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return (
                GeneralRepoSettings(**response)
                if response is not None
                else GeneralRepoSettings()
            )


async def getGeneralUISettings(
    api_config_override: Optional[APIConfig] = None,
) -> GeneralUISettings:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/settings/ui"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {}

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "get",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return (
                GeneralUISettings(**response)
                if response is not None
                else GeneralUISettings()
            )
