from typing import *

from pydantic import BaseModel, Field

from .ExternalTracker import ExternalTracker
from .ExternalWiki import ExternalWiki
from .InternalTracker import InternalTracker
from .Permission import Permission
from .RepoTransfer import RepoTransfer
from .User import User


class Repository(BaseModel):
    """
    None model
        Repository represents a repository

    """

    allow_merge_commits: Optional[bool] = Field(
        alias="allow_merge_commits", default=None
    )

    allow_rebase: Optional[bool] = Field(alias="allow_rebase", default=None)

    allow_rebase_explicit: Optional[bool] = Field(
        alias="allow_rebase_explicit", default=None
    )

    allow_rebase_update: Optional[bool] = Field(
        alias="allow_rebase_update", default=None
    )

    allow_squash_merge: Optional[bool] = Field(alias="allow_squash_merge", default=None)

    archived: Optional[bool] = Field(alias="archived", default=None)

    avatar_url: Optional[str] = Field(alias="avatar_url", default=None)

    clone_url: Optional[str] = Field(alias="clone_url", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    default_branch: Optional[str] = Field(alias="default_branch", default=None)

    default_delete_branch_after_merge: Optional[bool] = Field(
        alias="default_delete_branch_after_merge", default=None
    )

    default_merge_style: Optional[str] = Field(
        alias="default_merge_style", default=None
    )

    description: Optional[str] = Field(alias="description", default=None)

    empty: Optional[bool] = Field(alias="empty", default=None)

    external_tracker: Optional[ExternalTracker] = Field(
        alias="external_tracker", default=None
    )

    external_wiki: Optional[ExternalWiki] = Field(alias="external_wiki", default=None)

    fork: Optional[bool] = Field(alias="fork", default=None)

    forks_count: Optional[int] = Field(alias="forks_count", default=None)

    full_name: Optional[str] = Field(alias="full_name", default=None)

    has_issues: Optional[bool] = Field(alias="has_issues", default=None)

    has_projects: Optional[bool] = Field(alias="has_projects", default=None)

    has_pull_requests: Optional[bool] = Field(alias="has_pull_requests", default=None)

    has_wiki: Optional[bool] = Field(alias="has_wiki", default=None)

    html_url: Optional[str] = Field(alias="html_url", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    ignore_whitespace_conflicts: Optional[bool] = Field(
        alias="ignore_whitespace_conflicts", default=None
    )

    internal: Optional[bool] = Field(alias="internal", default=None)

    internal_tracker: Optional[InternalTracker] = Field(
        alias="internal_tracker", default=None
    )

    language: Optional[str] = Field(alias="language", default=None)

    languages_url: Optional[str] = Field(alias="languages_url", default=None)

    mirror: Optional[bool] = Field(alias="mirror", default=None)

    mirror_interval: Optional[str] = Field(alias="mirror_interval", default=None)

    mirror_updated: Optional[str] = Field(alias="mirror_updated", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    open_issues_count: Optional[int] = Field(alias="open_issues_count", default=None)

    open_pr_counter: Optional[int] = Field(alias="open_pr_counter", default=None)

    original_url: Optional[str] = Field(alias="original_url", default=None)

    owner: Optional[User] = Field(alias="owner", default=None)

    parent: Optional["Repository"] = Field(alias="parent", default=None)

    permissions: Optional[Permission] = Field(alias="permissions", default=None)

    private: Optional[bool] = Field(alias="private", default=None)

    release_counter: Optional[int] = Field(alias="release_counter", default=None)

    repo_transfer: Optional[RepoTransfer] = Field(alias="repo_transfer", default=None)

    size: Optional[int] = Field(alias="size", default=None)

    ssh_url: Optional[str] = Field(alias="ssh_url", default=None)

    stars_count: Optional[int] = Field(alias="stars_count", default=None)

    template: Optional[bool] = Field(alias="template", default=None)

    updated_at: Optional[str] = Field(alias="updated_at", default=None)

    watchers_count: Optional[int] = Field(alias="watchers_count", default=None)

    website: Optional[str] = Field(alias="website", default=None)
