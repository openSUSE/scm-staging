import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def userGetCurrent(api_config_override: Optional[APIConfig] = None) -> User:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user"
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

            return User(**response) if response is not None else User()


async def userGetOauth2Application(
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[OAuth2Application]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/applications/oauth2"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "limit": limit}

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

            return [OAuth2Application(**item) for item in response]


async def userCreateOAuth2Application(
    data: CreateOAuth2ApplicationOptions,
    api_config_override: Optional[APIConfig] = None,
) -> OAuth2Application:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/applications/oauth2"
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
            "post", base_path + path, params=query_params, json=data.dict()
        ) as inital_response:
            if inital_response.status != 201:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return (
                OAuth2Application(**response)
                if response is not None
                else OAuth2Application()
            )


async def userGetOAuth2Application(
    id: int, api_config_override: Optional[APIConfig] = None
) -> OAuth2Application:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/applications/oauth2/{id}"
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
                OAuth2Application(**response)
                if response is not None
                else OAuth2Application()
            )


async def userDeleteOAuth2Application(
    id: int, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/applications/oauth2/{id}"
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
            "delete",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return None


async def userUpdateOAuth2Application(
    id: int,
    data: CreateOAuth2ApplicationOptions,
    api_config_override: Optional[APIConfig] = None,
) -> OAuth2Application:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/applications/oauth2/{id}"
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
            "patch", base_path + path, params=query_params, json=data.dict()
        ) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return (
                OAuth2Application(**response)
                if response is not None
                else OAuth2Application()
            )


async def userListEmails(
    api_config_override: Optional[APIConfig] = None,
) -> List[Email]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/emails"
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

            return [Email(**item) for item in response]


async def userAddEmail(
    data: CreateEmailOption, api_config_override: Optional[APIConfig] = None
) -> List[Email]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/emails"
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
            "post", base_path + path, params=query_params, json=data.dict()
        ) as inital_response:
            if inital_response.status != 201:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return [Email(**item) for item in response]


async def userDeleteEmail(
    data: DeleteEmailOption, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/emails"
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
            "delete", base_path + path, params=query_params, json=data.dict()
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return None


async def userCurrentListFollowers(
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[User]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/followers"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "limit": limit}

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

            return [User(**item) for item in response]


async def userCurrentListFollowing(
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[User]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/following"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "limit": limit}

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

            return [User(**item) for item in response]


async def userCurrentCheckFollowing(
    username: str, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/following/{username}"
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
            if inital_response.status != 204:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return None


async def userCurrentPutFollow(
    username: str, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/following/{username}"
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
            "put",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return None


async def userCurrentDeleteFollow(
    username: str, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/following/{username}"
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
            "delete",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return None


async def getVerificationToken(api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/gpg_key_token"
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

            return None


async def userVerifyGPGKey(api_config_override: Optional[APIConfig] = None) -> GPGKey:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/gpg_key_verify"
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
            "post",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 201:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return GPGKey(**response) if response is not None else GPGKey()


async def userCurrentListGPGKeys(
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[GPGKey]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/gpg_keys"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "limit": limit}

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

            return [GPGKey(**item) for item in response]


async def userCurrentPostGPGKey(
    data: CreateGPGKeyOption, api_config_override: Optional[APIConfig] = None
) -> GPGKey:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/gpg_keys"
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
            "post", base_path + path, params=query_params, json=data.dict()
        ) as inital_response:
            if inital_response.status != 201:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return GPGKey(**response) if response is not None else GPGKey()


async def userCurrentGetGPGKey(
    id: int, api_config_override: Optional[APIConfig] = None
) -> GPGKey:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/gpg_keys/{id}"
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

            return GPGKey(**response) if response is not None else GPGKey()


async def userCurrentDeleteGPGKey(
    id: int, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/gpg_keys/{id}"
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
            "delete",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return None


async def userCurrentListKeys(
    fingerprint: Optional[str] = None,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[PublicKey]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/keys"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "fingerprint": fingerprint,
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

            return [PublicKey(**item) for item in response]


async def userCurrentPostKey(
    data: CreateKeyOption, api_config_override: Optional[APIConfig] = None
) -> PublicKey:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/keys"
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
            "post", base_path + path, params=query_params, json=data.dict()
        ) as inital_response:
            if inital_response.status != 201:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return PublicKey(**response) if response is not None else PublicKey()


async def userCurrentGetKey(
    id: int, api_config_override: Optional[APIConfig] = None
) -> PublicKey:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/keys/{id}"
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

            return PublicKey(**response) if response is not None else PublicKey()


async def userCurrentDeleteKey(
    id: int, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/keys/{id}"
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
            "delete",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return None


async def userCurrentListRepos(
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[Repository]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/repos"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "limit": limit}

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

            return [Repository(**item) for item in response]


async def getUserSettings(
    api_config_override: Optional[APIConfig] = None,
) -> List[UserSettings]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/settings"
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

            return [UserSettings(**item) for item in response]


async def updateUserSettings(
    data: UserSettingsOptions, api_config_override: Optional[APIConfig] = None
) -> List[UserSettings]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/settings"
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
            "patch", base_path + path, params=query_params, json=data.dict()
        ) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return [UserSettings(**item) for item in response]


async def userCurrentListStarred(
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[Repository]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/starred"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "limit": limit}

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

            return [Repository(**item) for item in response]


async def userCurrentCheckStarring(
    owner: str, repo: str, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/starred/{owner}/{repo}"
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
            if inital_response.status != 204:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return None


async def userCurrentPutStar(
    owner: str, repo: str, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/starred/{owner}/{repo}"
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
            "put",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return None


async def userCurrentDeleteStar(
    owner: str, repo: str, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/starred/{owner}/{repo}"
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
            "delete",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return None


async def userGetStopWatches(
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[StopWatch]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/stopwatches"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "limit": limit}

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

            return [StopWatch(**item) for item in response]


async def userCurrentListSubscriptions(
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[Repository]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/subscriptions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "limit": limit}

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

            return [Repository(**item) for item in response]


async def userListTeams(
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[Team]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/teams"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "limit": limit}

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

            return [Team(**item) for item in response]


async def userCurrentTrackedTimes(
    page: Optional[int] = None,
    limit: Optional[int] = None,
    since: Optional[str] = None,
    before: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[TrackedTime]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/user/times"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "page": page,
        "limit": limit,
        "since": since,
        "before": before,
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

            return [TrackedTime(**item) for item in response]


async def userSearch(
    q: Optional[str] = None,
    uid: Optional[int] = None,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> userSearch_200_response:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/users/search"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"q": q, "uid": uid, "page": page, "limit": limit}

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
                userSearch_200_response(**response)
                if response is not None
                else userSearch_200_response()
            )


async def userGet(
    username: str, api_config_override: Optional[APIConfig] = None
) -> User:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/users/{username}"
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

            return User(**response) if response is not None else User()


async def userListFollowers(
    username: str,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[User]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/users/{username}/followers"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "limit": limit}

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

            return [User(**item) for item in response]


async def userListFollowing(
    username: str,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[User]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/users/{username}/following"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "limit": limit}

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

            return [User(**item) for item in response]


async def userCheckFollowing(
    username: str, target: str, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/users/{username}/following/{target}"
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
            if inital_response.status != 204:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return None


async def userListGPGKeys(
    username: str,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[GPGKey]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/users/{username}/gpg_keys"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "limit": limit}

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

            return [GPGKey(**item) for item in response]


async def userGetHeatmapData(
    username: str, api_config_override: Optional[APIConfig] = None
) -> List[UserHeatmapData]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/users/{username}/heatmap"
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

            return [UserHeatmapData(**item) for item in response]


async def userListKeys(
    username: str,
    fingerprint: Optional[str] = None,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[PublicKey]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/users/{username}/keys"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "fingerprint": fingerprint,
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

            return [PublicKey(**item) for item in response]


async def userListRepos(
    username: str,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[Repository]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/users/{username}/repos"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "limit": limit}

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

            return [Repository(**item) for item in response]


async def userListStarred(
    username: str,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[Repository]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/users/{username}/starred"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "limit": limit}

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

            return [Repository(**item) for item in response]


async def userListSubscriptions(
    username: str,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[Repository]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/users/{username}/subscriptions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "limit": limit}

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

            return [Repository(**item) for item in response]


async def userGetTokens(
    username: str,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[AccessToken]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/users/{username}/tokens"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"page": page, "limit": limit}

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

            return [AccessToken(**item) for item in response]


async def userCreateToken(
    username: str,
    data: CreateAccessTokenOption,
    api_config_override: Optional[APIConfig] = None,
) -> AccessToken:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/users/{username}/tokens"
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
            "post", base_path + path, params=query_params, json=data.dict()
        ) as inital_response:
            if inital_response.status != 201:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return AccessToken(**response) if response is not None else AccessToken()


async def userDeleteAccessToken(
    username: str, token: str, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/users/{username}/tokens/{token}"
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
            "delete",
            base_path + path,
            params=query_params,
        ) as inital_response:
            if inital_response.status != 204:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return None
