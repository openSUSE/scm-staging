from dataclasses import dataclass
from enum import StrEnum, auto
from typing import ClassVar
from scm_staging.obs import Osc
from scm_staging.xml_factory import MetaMixin


class PackageCode(StrEnum):
    UNRESOLVABLE = auto()
    SUCCEEDED = auto()
    FAILED = auto()
    BROKEN = auto()
    DISABLED = auto()
    EXCLUDED = auto()
    BLOCKED = auto()
    LOCKED = auto()
    UNKNOWN = auto()
    SCHEDULED = auto()
    BUILDING = auto()
    FINISHED = auto()


@dataclass(frozen=True)
class PackageStatus(MetaMixin):
    _element_name: ClassVar[str] = "status"

    package: str
    code: PackageCode

    details: list[str]


class RepositoryCode(StrEnum):
    UNKNOWN = auto()
    BROKEN = auto()
    SCHEDULING = auto()
    BLOCKED = auto()
    BUILDING = auto()
    FINISHED = auto()
    PUBLISHING = auto()
    PUBLISHED = auto()
    UNPUBLISHED = auto()


@dataclass(frozen=True)
class BuildResult(MetaMixin):
    _element_name: ClassVar[str] = "result"

    project: str
    repository: str
    arch: str
    state: RepositoryCode
    code: RepositoryCode
    dirty: bool | None

    status: list[PackageStatus]


@dataclass(frozen=True)
class BuildResultList(MetaMixin):
    _element_name: ClassVar[str] = "resultlist"

    result: list[BuildResult]


async def fetch_build_result(
    osc: Osc, project_name: str, package_name: str
) -> list[BuildResult]:
    return (
        await BuildResultList.from_response(
            await osc.api_request(
                f"/build/{project_name}/_result",
                params={
                    "view": "status",
                    "multibuild": "1",
                    "locallink": "1",
                    "package": package_name,
                },
            )
        )
    ).result
