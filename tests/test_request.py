import asyncio
from typing import AsyncGenerator
import pytest
import xml.etree.ElementTree as ET
from scm_staging.obs import Osc
from scm_staging.project import Package, Project

from scm_staging.request import (
    _RequestCollection,
    Request,
    RequestAction,
    RequestActionType,
    RequestSource,
    RequestState,
    RequestStatus,
    RequestTarget,
    delete,
    fetch_request,
    search_for_requests,
    submit_package,
)
from tests.conftest import HOME_PROJ_T


@pytest.mark.parametrize(
    "api_response,expected_list",
    [
        (
            """<collection matches="5"><request id="1038934" creator="defolos">
  <action type="submit">
    <source project="home:defolos:BCI:CR:SLE-15-SP3" package="pcp-image"/>
    <target project="home:dancermak" package="pcp-image"/>
  </action>
  <state name="revoked" who="defolos" when="2022-11-30T08:06:01" created="2022-11-29T16:19:16">
    <comment/>
  </state>
</request>
<request id="1038935" creator="defolos">
  <action type="submit">
    <source project="home:defolos:BCI:CR:SLE-15-SP3" package="pcp-image"/>
    <target project="home:dancermak" package="pcp-image"/>
  </action>
  <state name="revoked" who="defolos" when="2022-11-30T08:05:53" created="2022-11-29T16:21:25">
    <comment/>
  </state>
</request>
<request id="1039138" creator="dancermak">
  <action type="submit">
    <source project="home:defolos:SCM_STAGING:Factory:zellij:110" package="zellij"/>
    <target project="home:dancermak" package="zellij"/>
  </action>
  <state name="revoked" who="dancermak" when="2022-11-30T15:09:21" created="2022-11-30T15:08:33">
    <comment/>
  </state>
  <review state="new" when="2022-11-30T15:08:33" by_package="zellij" by_project="home:defolos:SCM_STAGING:Factory:zellij:110"/>
</request>
<request id="1039149" creator="defolos">
  <action type="submit">
    <source project="home:defolos:SCM_STAGING:Factory:zellij:110" package="zellij"/>
    <target project="devel:Factory:git-workflow:mold:core" package="zellij"/>
  </action>
  <state name="revoked" who="defolos" when="2022-11-30T16:12:37" created="2022-11-30T16:11:15">
    <comment/>
  </state>
</request>
<request id="1039278" creator="defolos">
  <action type="submit">
    <source project="home:defolos:SCM_STAGING:Factory:zellij:110" package="zellij"/>
    <target project="devel:Factory:git-workflow:mold:core" package="zellij"/>
    <acceptinfo rev="1" srcmd5="cbbd0063ce6ef64fdc5f8f89b2633f5e" osrcmd5="d41d8cd98f00b204e9800998ecf8427e"/>
  </action>
  <state name="accepted" who="dirkmueller" when="2022-12-01T12:22:26" created="2022-12-01T09:48:43">
    <comment/>
  </state>
</request>
</collection>
""",
            [
                Request(
                    id=1038934,
                    creator="defolos",
                    description=None,
                    action=[
                        RequestAction(
                            type=RequestActionType.SUBMIT,
                            source=RequestSource(
                                project="home:defolos:BCI:CR:SLE-15-SP3",
                                package="pcp-image",
                            ),
                            target=RequestTarget(
                                project="home:dancermak", package="pcp-image"
                            ),
                        )
                    ],
                    state=RequestState(
                        state=RequestStatus.REVOKED,
                        who="defolos",
                        when="2022-11-30T08:06:01",
                        created="2022-11-29T16:19:16",
                    ),
                ),
                Request(
                    id=1038935,
                    creator="defolos",
                    description=None,
                    action=[
                        RequestAction(
                            type=RequestActionType.SUBMIT,
                            source=RequestSource(
                                project="home:defolos:BCI:CR:SLE-15-SP3",
                                package="pcp-image",
                            ),
                            target=RequestTarget(
                                project="home:dancermak", package="pcp-image"
                            ),
                        )
                    ],
                    state=RequestState(
                        state=RequestStatus.REVOKED,
                        who="defolos",
                        when="2022-11-30T08:05:53",
                        created="2022-11-29T16:21:25",
                    ),
                ),
                Request(
                    id=1039138,
                    creator="dancermak",
                    description=None,
                    action=[
                        RequestAction(
                            type=RequestActionType.SUBMIT,
                            source=RequestSource(
                                project="home:defolos:SCM_STAGING:Factory:zellij:110",
                                package="zellij",
                            ),
                            target=RequestTarget(
                                project="home:dancermak", package="zellij"
                            ),
                        )
                    ],
                    state=RequestState(
                        state=RequestStatus.REVOKED,
                        who="dancermak",
                        when="2022-11-30T15:09:21",
                        created="2022-11-30T15:08:33",
                    ),
                ),
                Request(
                    id=1039149,
                    creator="defolos",
                    description=None,
                    action=[
                        RequestAction(
                            type=RequestActionType.SUBMIT,
                            source=RequestSource(
                                project="home:defolos:SCM_STAGING:Factory:zellij:110",
                                package="zellij",
                            ),
                            target=RequestTarget(
                                project="devel:Factory:git-workflow:mold:core",
                                package="zellij",
                            ),
                        )
                    ],
                    state=RequestState(
                        state=RequestStatus.REVOKED,
                        who="defolos",
                        when="2022-11-30T16:12:37",
                        created="2022-11-30T16:11:15",
                    ),
                ),
                Request(
                    id=1039278,
                    creator="defolos",
                    description=None,
                    action=[
                        RequestAction(
                            type=RequestActionType.SUBMIT,
                            source=RequestSource(
                                project="home:defolos:SCM_STAGING:Factory:zellij:110",
                                package="zellij",
                            ),
                            target=RequestTarget(
                                project="devel:Factory:git-workflow:mold:core",
                                package="zellij",
                            ),
                        )
                    ],
                    state=RequestState(
                        state=RequestStatus.ACCEPTED,
                        who="dirkmueller",
                        when="2022-12-01T12:22:26",
                        created="2022-12-01T09:48:43",
                    ),
                ),
            ],
        )
    ],
)
def test_request_from_obs(api_response: str, expected_list: list[Request]):
    assert (
        _RequestCollection.from_xml(ET.fromstring(api_response)).request
        == expected_list
    )


@pytest.mark.asyncio
async def test_submit_package(home_project: HOME_PROJ_T):
    async for osc, admin_osc, prj, pkg in home_project:
        req = await submit_package(
            osc, source_prj=prj.name, pkg_name=pkg.name, dest_prj="openSUSE:Factory"
        )

        assert req
        assert req.id is not None
        assert req.creator == osc.username
        assert req.state is not None
        assert req.state.state == RequestStatus.NEW

        assert len(req.action) == 1
        assert (
            (
                (action := req.action[0]).source
                == RequestSource(project=prj.name, package=pkg.name)
            )
            and (action.type == RequestActionType.SUBMIT)
            and (
                action.target
                == RequestTarget(project="openSUSE:Factory", package=pkg.name)
            )
        )

        assert len(await search_for_requests(osc, ids=[req.id])) == 1

        await delete(admin_osc, request=req)

        assert len(await search_for_requests(osc, ids=[req.id])) == 0


@pytest.mark.asyncio
async def test_supersede_submit(home_project: HOME_PROJ_T):
    async for osc, admin_osc, prj, pkg in home_project:
        req = await submit_package(
            osc, source_prj=prj.name, pkg_name=pkg.name, dest_prj="openSUSE:Factory"
        )

        req2 = await submit_package(
            osc,
            source_prj=prj.name,
            pkg_name=pkg.name,
            dest_prj="openSUSE:Factory",
            supersede_old_request=False,
        )

        assert req.id and req2.id
        ids = [req.id, req2.id]
        reqs = await search_for_requests(osc, ids=ids)
        assert len(reqs) == 2
        assert (
            (st0 := reqs[0].state)
            and st0.state == RequestStatus.NEW
            and (st1 := reqs[1].state)
            and st1.state == RequestStatus.NEW
        )

        req3 = await submit_package(
            osc, source_prj=prj.name, pkg_name=pkg.name, dest_prj="openSUSE:Factory"
        )
        assert req3.id is not None

        reqs = await search_for_requests(osc, ids=ids)
        assert len(reqs) == 2
        assert (
            (st0 := reqs[0].state)
            and st0.state == RequestStatus.SUPERSEDED
            and st0.superseded_by == req3.id
            and (st1 := reqs[1].state)
            and st1.state == RequestStatus.SUPERSEDED
            and st1.superseded_by == req3.id
        )

        await asyncio.gather(*(delete(admin_osc, request=r) for r in (req, req2, req3)))


@pytest.mark.asyncio
async def test_fetch_request(home_project: HOME_PROJ_T):
    async for osc, admin_osc, prj, pkg in home_project:
        req = await submit_package(
            osc, source_prj=prj.name, pkg_name=pkg.name, dest_prj="openSUSE:Factory"
        )

        assert req == await fetch_request(osc, request=req)

        await delete(admin_osc, request=req)
