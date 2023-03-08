import json
from typing import *

import aiohttp

from ..api_config import APIConfig, HTTPException
from ..models import *


async def issueSearchIssues(
    state: Optional[str] = None,
    labels: Optional[str] = None,
    milestones: Optional[str] = None,
    q: Optional[str] = None,
    priority_repo_id: Optional[int] = None,
    type: Optional[str] = None,
    since: Optional[str] = None,
    before: Optional[str] = None,
    assigned: Optional[bool] = None,
    created: Optional[bool] = None,
    mentioned: Optional[bool] = None,
    review_requested: Optional[bool] = None,
    owner: Optional[str] = None,
    team: Optional[str] = None,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[Issue]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/issues/search"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "state": state,
        "labels": labels,
        "milestones": milestones,
        "q": q,
        "priority_repo_id": priority_repo_id,
        "type": type,
        "since": since,
        "before": before,
        "assigned": assigned,
        "created": created,
        "mentioned": mentioned,
        "review_requested": review_requested,
        "owner": owner,
        "team": team,
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

            return [Issue(**item) for item in response]


async def issueListIssues(
    owner: str,
    repo: str,
    state: Optional[str] = None,
    labels: Optional[str] = None,
    q: Optional[str] = None,
    type: Optional[str] = None,
    milestones: Optional[str] = None,
    since: Optional[str] = None,
    before: Optional[str] = None,
    created_by: Optional[str] = None,
    assigned_by: Optional[str] = None,
    mentioned_by: Optional[str] = None,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[Issue]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "state": state,
        "labels": labels,
        "q": q,
        "type": type,
        "milestones": milestones,
        "since": since,
        "before": before,
        "created_by": created_by,
        "assigned_by": assigned_by,
        "mentioned_by": mentioned_by,
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

            return [Issue(**item) for item in response]


async def issueCreateIssue(
    owner: str,
    repo: str,
    data: CreateIssueOption,
    api_config_override: Optional[APIConfig] = None,
) -> Issue:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues"
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

            return Issue(**response) if response is not None else Issue()


async def issueGetRepoComments(
    owner: str,
    repo: str,
    since: Optional[str] = None,
    before: Optional[str] = None,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[Comment]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/comments"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
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

            return [Comment(**item) for item in response]


async def issueGetComment(
    owner: str, repo: str, id: int, api_config_override: Optional[APIConfig] = None
) -> Comment:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/comments/{id}"
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

            return Comment(**response) if response is not None else Comment()


async def issueDeleteComment(
    owner: str, repo: str, id: int, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/comments/{id}"
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


async def issueEditComment(
    owner: str,
    repo: str,
    id: int,
    data: EditIssueCommentOption,
    api_config_override: Optional[APIConfig] = None,
) -> Comment:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/comments/{id}"
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

            return Comment(**response) if response is not None else Comment()


async def issueGetCommentReactions(
    owner: str, repo: str, id: int, api_config_override: Optional[APIConfig] = None
) -> List[Reaction]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/comments/{id}/reactions"
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

            return [Reaction(**item) for item in response]


async def issuePostCommentReaction(
    owner: str,
    repo: str,
    id: int,
    data: EditReactionOption,
    api_config_override: Optional[APIConfig] = None,
) -> Reaction:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/comments/{id}/reactions"
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
            if inital_response.status != 200:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return Reaction(**response) if response is not None else Reaction()


async def issueDeleteCommentReaction(
    owner: str,
    repo: str,
    id: int,
    data: EditReactionOption,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/comments/{id}/reactions"
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
            if inital_response.status != 200:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return None


async def issueGetIssue(
    owner: str, repo: str, index: int, api_config_override: Optional[APIConfig] = None
) -> Issue:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}"
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

            return Issue(**response) if response is not None else Issue()


async def issueDelete(
    owner: str, repo: str, index: int, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}"
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


async def issueEditIssue(
    owner: str,
    repo: str,
    index: int,
    data: EditIssueOption,
    api_config_override: Optional[APIConfig] = None,
) -> Issue:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}"
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
            if inital_response.status != 201:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return Issue(**response) if response is not None else Issue()


async def issueGetComments(
    owner: str,
    repo: str,
    index: int,
    since: Optional[str] = None,
    before: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[Comment]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/comments"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {"since": since, "before": before}

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

            return [Comment(**item) for item in response]


async def issueCreateComment(
    owner: str,
    repo: str,
    index: int,
    data: CreateIssueCommentOption,
    api_config_override: Optional[APIConfig] = None,
) -> Comment:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/comments"
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

            return Comment(**response) if response is not None else Comment()


async def issueDeleteCommentDeprecated(
    owner: str,
    repo: str,
    index: int,
    id: int,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/comments/{id}"
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


async def issueEditCommentDeprecated(
    owner: str,
    repo: str,
    index: int,
    id: int,
    data: EditIssueCommentOption,
    api_config_override: Optional[APIConfig] = None,
) -> Comment:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/comments/{id}"
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

            return Comment(**response) if response is not None else Comment()


async def issueEditIssueDeadline(
    owner: str,
    repo: str,
    index: int,
    data: EditDeadlineOption,
    api_config_override: Optional[APIConfig] = None,
) -> IssueDeadline:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/deadline"
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
                IssueDeadline(**response) if response is not None else IssueDeadline()
            )


async def issueGetLabels(
    owner: str, repo: str, index: int, api_config_override: Optional[APIConfig] = None
) -> List[Label]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/labels"
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

            return [Label(**item) for item in response]


async def issueAddLabel(
    owner: str,
    repo: str,
    index: int,
    data: IssueLabelsOption,
    api_config_override: Optional[APIConfig] = None,
) -> List[Label]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/labels"
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
            if inital_response.status != 200:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return [Label(**item) for item in response]


async def issueReplaceLabels(
    owner: str,
    repo: str,
    index: int,
    data: IssueLabelsOption,
    api_config_override: Optional[APIConfig] = None,
) -> List[Label]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/labels"
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
            "put", base_path + path, params=query_params, json=data.dict()
        ) as inital_response:
            if inital_response.status != 200:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return [Label(**item) for item in response]


async def issueClearLabels(
    owner: str, repo: str, index: int, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/labels"
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


async def issueRemoveLabel(
    owner: str,
    repo: str,
    index: int,
    id: int,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/labels/{id}"
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


async def issueGetIssueReactions(
    owner: str,
    repo: str,
    index: int,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[Reaction]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/reactions"
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

            return [Reaction(**item) for item in response]


async def issuePostIssueReaction(
    owner: str,
    repo: str,
    index: int,
    data: EditReactionOption,
    api_config_override: Optional[APIConfig] = None,
) -> Reaction:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/reactions"
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
            if inital_response.status != 200:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return Reaction(**response) if response is not None else Reaction()


async def issueDeleteIssueReaction(
    owner: str,
    repo: str,
    index: int,
    data: EditReactionOption,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/reactions"
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
            if inital_response.status != 200:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return None


async def issueDeleteStopWatch(
    owner: str, repo: str, index: int, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/stopwatch/delete"
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


async def issueStartStopWatch(
    owner: str, repo: str, index: int, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/stopwatch/start"
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

            return None


async def issueStopStopWatch(
    owner: str, repo: str, index: int, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/stopwatch/stop"
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

            return None


async def issueSubscriptions(
    owner: str,
    repo: str,
    index: int,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[User]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/subscriptions"
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


async def issueCheckSubscription(
    owner: str, repo: str, index: int, api_config_override: Optional[APIConfig] = None
) -> WatchInfo:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/subscriptions/check"
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

            return WatchInfo(**response) if response is not None else WatchInfo()


async def issueAddSubscription(
    owner: str,
    repo: str,
    index: int,
    user: str,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}"
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
            if inital_response.status != 200:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return None


async def issueDeleteSubscription(
    owner: str,
    repo: str,
    index: int,
    user: str,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}"
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
            if inital_response.status != 200:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return None


async def issueGetCommentsAndTimeline(
    owner: str,
    repo: str,
    index: int,
    since: Optional[str] = None,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    before: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[TimelineComment]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/timeline"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "since": since,
        "page": page,
        "limit": limit,
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

            return [TimelineComment(**item) for item in response]


async def issueTrackedTimes(
    owner: str,
    repo: str,
    index: int,
    user: Optional[str] = None,
    since: Optional[str] = None,
    before: Optional[str] = None,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[TrackedTime]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/times"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "user": user,
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

            return [TrackedTime(**item) for item in response]


async def issueAddTime(
    owner: str,
    repo: str,
    index: int,
    data: AddTimeOption,
    api_config_override: Optional[APIConfig] = None,
) -> TrackedTime:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/times"
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
            if inital_response.status != 200:
                raise HTTPException(
                    inital_response.status,
                    f" failed with status code: {inital_response.status}",
                )
            response = await inital_response.json()

            return TrackedTime(**response) if response is not None else TrackedTime()


async def issueResetTime(
    owner: str, repo: str, index: int, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/times"
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


async def issueDeleteTime(
    owner: str,
    repo: str,
    index: int,
    id: int,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/issues/{index}/times/{id}"
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


async def issueListLabels(
    owner: str,
    repo: str,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[Label]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/labels"
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

            return [Label(**item) for item in response]


async def issueCreateLabel(
    owner: str,
    repo: str,
    data: CreateLabelOption,
    api_config_override: Optional[APIConfig] = None,
) -> Label:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/labels"
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

            return Label(**response) if response is not None else Label()


async def issueGetLabel(
    owner: str, repo: str, id: int, api_config_override: Optional[APIConfig] = None
) -> Label:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/labels/{id}"
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

            return Label(**response) if response is not None else Label()


async def issueDeleteLabel(
    owner: str, repo: str, id: int, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/labels/{id}"
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


async def issueEditLabel(
    owner: str,
    repo: str,
    id: int,
    data: EditLabelOption,
    api_config_override: Optional[APIConfig] = None,
) -> Label:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/labels/{id}"
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

            return Label(**response) if response is not None else Label()


async def issueGetMilestonesList(
    owner: str,
    repo: str,
    state: Optional[str] = None,
    name: Optional[str] = None,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    api_config_override: Optional[APIConfig] = None,
) -> List[Milestone]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/milestones"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }

    query_params: Dict[str, Any] = {
        "state": state,
        "name": name,
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

            return [Milestone(**item) for item in response]


async def issueCreateMilestone(
    owner: str,
    repo: str,
    data: CreateMilestoneOption,
    api_config_override: Optional[APIConfig] = None,
) -> Milestone:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/milestones"
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

            return Milestone(**response) if response is not None else Milestone()


async def issueGetMilestone(
    owner: str, repo: str, id: str, api_config_override: Optional[APIConfig] = None
) -> Milestone:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/milestones/{id}"
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

            return Milestone(**response) if response is not None else Milestone()


async def issueDeleteMilestone(
    owner: str, repo: str, id: str, api_config_override: Optional[APIConfig] = None
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/milestones/{id}"
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


async def issueEditMilestone(
    owner: str,
    repo: str,
    id: str,
    data: EditMilestoneOption,
    api_config_override: Optional[APIConfig] = None,
) -> Milestone:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/repos/{owner}/{repo}/milestones/{id}"
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

            return Milestone(**response) if response is not None else Milestone()
