from dataclasses import dataclass, field
from typing import ClassVar, overload
import xml.etree.ElementTree as ET

from scm_staging.obs import Osc
from scm_staging.person import OwnerCollection, Person, Person2, PersonRole
from .xml_factory import MetaMixin, StrElementField


@dataclass(frozen=True)
class PathEntry(MetaMixin):
    project: str
    repository: str

    _element_name: ClassVar[str] = "path"


@dataclass(frozen=True)
class Repository(MetaMixin):
    name: str
    path: list[PathEntry] | None = None
    arch: list[str] | None = None

    _element_name: ClassVar[str] = "repository"


@dataclass(frozen=True)
class Project(MetaMixin):
    name: str
    title: StrElementField
    description: StrElementField = StrElementField("")

    person: list[Person] | None = None
    repository: list[Repository] | None = None

    _element_name: ClassVar[str] = "project"


@dataclass(frozen=True)
class Package:
    name: str
    title: str
    description: str = ""

    scmsync: str | None = None

    _element_name: ClassVar[str] = "package"

    @property
    def meta(self) -> ET.Element:
        (pkg_conf := ET.Element(Package._element_name)).attrib["name"] = self.name
        (title := ET.Element("title")).text = self.title
        (descr := ET.Element("description")).text = self.description
        pkg_conf.append(title)
        pkg_conf.append(descr)
        if self.scmsync:
            (scmsync := ET.Element("scmsync")).text = self.scmsync
            pkg_conf.append(scmsync)

        return pkg_conf


@dataclass(frozen=True)
class PackageMaintainers:
    package: list[Person2] = field(default_factory=list)
    project: list[Person2] = field(default_factory=list)


@overload
async def search_for_maintainers(
    osc: Osc, *, pkg: Package, roles: list[PersonRole] | None = None
) -> PackageMaintainers:
    ...


@overload
async def search_for_maintainers(
    osc: Osc, *, pkg_name: str, roles: list[PersonRole] | None = None
) -> PackageMaintainers:
    ...


async def search_for_maintainers(
    osc: Osc,
    *,
    pkg: Package | None = None,
    pkg_name: str | None = None,
    roles: list[PersonRole] | None = None,
) -> PackageMaintainers:
    if not pkg_name:
        assert pkg
        pkg_name = pkg.name

    params = {"package": pkg_name}
    if roles:
        params["filter"] = ",".join(roles)

    owners = await OwnerCollection.from_response(
        await osc.api_request("/search/owner", method="GET", params=params)
    )

    pkg_maintainers = []
    prj_maintainers = []
    for owner in owners.owner:
        if owner.project and owner.package == pkg_name:
            pkg_maintainers.extend(owner.person)

        if owner.project and not owner.package:
            prj_maintainers.extend(owner.person)

    return PackageMaintainers(package=pkg_maintainers, project=prj_maintainers)


@overload
async def send_meta(osc: Osc, *, prj: Project) -> None:
    ...


@overload
async def send_meta(osc: Osc, *, prj: Project, pkg: Package) -> None:
    ...


@overload
async def send_meta(osc: Osc, *, prj_name: str, prj_meta: ET.Element) -> None:
    ...


@overload
async def send_meta(
    osc: Osc, *, prj_name: str, pkg_name: str, pkg_meta: ET.Element
) -> None:
    ...


async def send_meta(
    osc: Osc,
    *,
    prj: Project | None = None,
    prj_name: str | None = None,
    prj_meta: ET.Element | None = None,
    pkg: Package | None = None,
    pkg_name: str | None = None,
    pkg_meta: ET.Element | None = None,
) -> None:
    route = "/source/"

    if prj and pkg:
        route += f"{prj.name}/{pkg.name}"
        meta = pkg.meta
    elif prj and not pkg:
        route += prj.name
        meta = prj.meta
    elif prj_name and pkg_name and pkg_meta:
        route += f"{prj_name}/{pkg_name}"
        meta = pkg_meta
    elif prj_name and prj_meta:
        route += prj_name
        meta = prj_meta
    else:
        assert False, "Invalid parameter combination"

    route += "/_meta"

    await osc.api_request(route=route, payload=ET.tostring(meta), method="PUT")


@overload
async def delete(osc: Osc, *, prj: Project | str, force: bool = False) -> None:
    ...


@overload
async def delete(
    osc: Osc, *, prj: Project | str, pkg: Package | str, force: bool = False
) -> None:
    ...


async def delete(
    osc: Osc,
    *,
    prj: Project | str,
    pkg: Package | str | None = None,
    force: bool = False,
) -> None:
    prj_name = prj.name if isinstance(prj, Project) else prj
    route = f"/source/{prj_name}/"
    if pkg:
        route += pkg.name if isinstance(pkg, Package) else pkg

    await osc.api_request(
        route, method="DELETE", params={"force": "1"} if force else None
    )
