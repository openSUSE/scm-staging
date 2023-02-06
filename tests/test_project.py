import xml.etree.ElementTree as ET
import pytest
from scm_staging.person import PersonRole
from scm_staging.project import PathEntry, Person, Project, Repository
from scm_staging.xml_factory import StrElementField


@pytest.mark.parametrize(
    "project,prj_meta",
    [
        (
            Project(
                name="home:defolos:BCI:CR:SLE-15-SP4",
                title=StrElementField("BCI Development project for SLE 15 SP4"),
                person=[
                    Person(userid="fcrozat", role=PersonRole.BUGOWNER),
                    Person(userid="aherzig", role=PersonRole.MAINTAINER),
                ],
                repository=[
                    Repository(
                        name="standard",
                        path=[
                            PathEntry(project="SUSE:Registry", repository="standard"),
                            PathEntry(
                                project="SUSE:SLE-15-SP4:Update", repository="standard"
                            ),
                        ],
                        arch=["x86_64", "aarch64", "s390x", "ppc64le"],
                    )
                ],
            ),
            """<project name="home:defolos:BCI:CR:SLE-15-SP4"><title>BCI Development project for SLE 15 SP4</title><description/><person userid="fcrozat" role="bugowner"/><person userid="aherzig" role="maintainer"/><repository name="standard"><path project="SUSE:Registry" repository="standard"/><path project="SUSE:SLE-15-SP4:Update" repository="standard"/><arch>x86_64</arch><arch>aarch64</arch><arch>s390x</arch><arch>ppc64le</arch></repository></project>""",
        )
    ],
)
def test_project(project: Project, prj_meta: str):
    assert ET.canonicalize(
        ET.tostring(project.meta, short_empty_elements=True).decode("utf-8")
    ) == ET.canonicalize(prj_meta)
