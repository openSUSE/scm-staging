import enum
from dataclasses import dataclass, field
from typing import ClassVar

from scm_staging.obs import Osc
from scm_staging.xml_factory import MetaMixin, StrElementField


@enum.unique
class PersonRole(enum.StrEnum):
    BUGOWNER = enum.auto()
    MAINTAINER = enum.auto()
    READER = enum.auto()


@dataclass(frozen=True)
class Person(MetaMixin):
    userid: str
    role: PersonRole = PersonRole.MAINTAINER

    _element_name: ClassVar[str] = "person"


@dataclass(frozen=True)
class Person2(MetaMixin):
    name: str
    role: PersonRole = PersonRole.MAINTAINER

    _element_name: ClassVar[str] = "person"

    def to_person(self) -> Person:
        return Person(userid=self.name, role=self.role)


@dataclass(frozen=True)
class User(MetaMixin):
    login: StrElementField
    email: StrElementField | None
    realname: StrElementField | None
    state: StrElementField | None

    _element_name: ClassVar[str] = "person"


async def fetch_user(osc: Osc, username: str) -> User:
    return await User.from_response(
        await osc.api_request(f"/person/{username}", method="GET")
    )


@dataclass(frozen=True)
class Owner(MetaMixin):
    project: str
    package: str | None = None

    person: list[Person2] = field(default_factory=list)

    _element_name: ClassVar[str] = "owner"


@dataclass(frozen=True)
class OwnerCollection(MetaMixin):
    _element_name: ClassVar[str] = "collection"

    owner: list[Owner] = field(default_factory=list)
