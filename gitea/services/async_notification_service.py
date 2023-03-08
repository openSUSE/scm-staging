import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def notifyGetList(
    all: Optional[bool] = None,
    status_types: Optional[List[str]] = None,
    subject_type: Optional[List[str]] = None,
    since: Optional[str] = None,
    before: Optional[str] = None,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[NotificationThread]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/notifications"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "all": all,
        "status-types": status_types,
        "subject-type": subject_type,
        "since": since,
        "before": before,
        "page": page,
        "limit": limit,
    }

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

            return [NotificationThread(**item) for item in response]


async def notifyReadList(
    last_read_at: Optional[str] = None,
    all: Optional[str] = None,
    status_types: Optional[List[str]] = None,
    to_status: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[NotificationThread]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/notifications"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "last_read_at": last_read_at,
        "all": all,
        "status-types": status_types,
        "to-status": to_status,
    }

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "put",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 205:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return [NotificationThread(**item) for item in response]


async def notifyNewAvailable(
    api_config_override: Optional[APIConfig] = None,
) -> NotificationCount:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/notifications/new"
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
                NotificationCount(**response)
                if response is not None
                else NotificationCount()
            )


async def notifyGetThread(
    id: str, api_config_override: Optional[APIConfig] = None
) -> NotificationThread:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/notifications/threads/{id}"
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
                NotificationThread(**response)
                if response is not None
                else NotificationThread()
            )


async def notifyReadThread(
    id: str,
    to_status: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> NotificationThread:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/notifications/threads/{id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"to-status": to_status}

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "patch",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 205:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return (
                NotificationThread(**response)
                if response is not None
                else NotificationThread()
            )


async def notifyGetRepoList(
    owner: str,
    repo: str,
    all: Optional[bool] = None,
    status_types: Optional[List[str]] = None,
    subject_type: Optional[List[str]] = None,
    since: Optional[str] = None,
    before: Optional[str] = None,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[NotificationThread]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/notifications"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "all": all,
        "status-types": status_types,
        "subject-type": subject_type,
        "since": since,
        "before": before,
        "page": page,
        "limit": limit,
    }

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

            return [NotificationThread(**item) for item in response]


async def notifyReadRepoList(
    owner: str,
    repo: str,
    all: Optional[str] = None,
    status_types: Optional[List[str]] = None,
    to_status: Optional[str] = None,
    last_read_at: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[NotificationThread]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/notifications"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "all": all,
        "status-types": status_types,
        "to-status": to_status,
        "last_read_at": last_read_at,
    }

    query_params = {
        key: value for (key, value) in query_params.items() if value is not None
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(
            "put",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 205:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return [NotificationThread(**item) for item in response]
