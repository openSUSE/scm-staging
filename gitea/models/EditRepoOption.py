from typing import *

from pydantic import BaseModel, Field

from .ExternalTracker import ExternalTracker
from .ExternalWiki import ExternalWiki
from .InternalTracker import InternalTracker


class EditRepoOption(BaseModel):
    """
    None model
        EditRepoOption options when editing a repository&#39;s properties

    """

    allow_manual_merge: Optional[bool] = Field(alias="allow_manual_merge", default=None)

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

    autodetect_manual_merge: Optional[bool] = Field(
        alias="autodetect_manual_merge", default=None
    )

    default_branch: Optional[str] = Field(alias="default_branch", default=None)

    default_delete_branch_after_merge: Optional[bool] = Field(
        alias="default_delete_branch_after_merge", default=None
    )

    default_merge_style: Optional[str] = Field(
        alias="default_merge_style", default=None
    )

    description: Optional[str] = Field(alias="description", default=None)

    enable_prune: Optional[bool] = Field(alias="enable_prune", default=None)

    external_tracker: Optional[ExternalTracker] = Field(
        alias="external_tracker", default=None
    )

    external_wiki: Optional[ExternalWiki] = Field(alias="external_wiki", default=None)

    has_issues: Optional[bool] = Field(alias="has_issues", default=None)

    has_projects: Optional[bool] = Field(alias="has_projects", default=None)

    has_pull_requests: Optional[bool] = Field(alias="has_pull_requests", default=None)

    has_wiki: Optional[bool] = Field(alias="has_wiki", default=None)

    ignore_whitespace_conflicts: Optional[bool] = Field(
        alias="ignore_whitespace_conflicts", default=None
    )

    internal_tracker: Optional[InternalTracker] = Field(
        alias="internal_tracker", default=None
    )

    mirror_interval: Optional[str] = Field(alias="mirror_interval", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    private: Optional[bool] = Field(alias="private", default=None)

    template: Optional[bool] = Field(alias="template", default=None)

    website: Optional[str] = Field(alias="website", default=None)
