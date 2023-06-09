"""The config module contains the Models that are loaded from the webhook json
config file.

"""

from enum import StrEnum, auto, unique
import json
from pydantic import BaseModel


@unique
class SubmissionStyle(StrEnum):
    """Options how the bot will submit packages."""

    #: the bot submits the package directly to the destination project
    DIRECT = auto()

    #: the bot sends the project to the develproject defined in the destination
    #: project
    FACTORY_DEVEL = auto()


class BranchConfig(BaseModel):
    """Configuration entry of the bot for how to treat merge requests for a
    certain organization.

    """

    #: name of the branch against which the pull requests should be considered
    target_branch_name: str

    #: organization (= username) for which pull requests will be monitored
    organization: str

    #: Whether merge requests have to be approved by the package maintainer
    #: first, before a submitrequest is created. The default is ``False``.
    require_approval: bool = False

    #: project name on OBS against which the package should be submitted
    destination_project: str

    #: Defines how the bot should submit the packages, defaults to a direct
    #: submission (:py:attr:`SubmissionStyle.DIRECT`)
    submission_style: SubmissionStyle = SubmissionStyle.DIRECT

    #: Whether the bot shall merge the pull request once the submitrequest is
    #: accepted. Defaults to ``True``.
    merge_pr: bool = True


def load_config(config_dot_json_path: str) -> list[BranchConfig]:
    """Read the config from the json file with the provided path."""
    res = []
    with open(config_dot_json_path, "r") as conf_file:
        data = json.loads(conf_file.read(-1))
        for conf in data:
            res.append(BranchConfig(**conf))

    return res
