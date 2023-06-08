import pathlib
import pytest

from scm_staging.db import (
    PullRequestToSubmitRequest,
    create_db,
    find_submitrequests,
    insert_submit_request,
    remove_submit_request,
)


@pytest.fixture
def db(tmp_path: pathlib.Path) -> str:
    create_db(db_path := str(tmp_path / "test.db"))
    return db_path


PR_TO_SR_1 = PullRequestToSubmitRequest(
    submit_request_id=5,
    obs_project_name="home:foobar:testing",
    obs_package_name="gcc",
    gitea_repo_name="gcc",
    gitea_repo_owner="rpm",
    merge_pr=True,
    pull_request_number=2,
)
PR_TO_SR_2 = PullRequestToSubmitRequest(
    submit_request_id=42,
    obs_project_name="openSUSE:Factory",
    obs_package_name="patterns-base",
    gitea_repo_name="leap",
    gitea_repo_owner="pool",
    merge_pr=False,
    pull_request_number=3,
)


def test_db_insert(db: str) -> None:
    insert_submit_request(db, PR_TO_SR_1)

    assert find_submitrequests(db) == [PR_TO_SR_1]


def test_find_all_srs(
    db: str,
) -> None:
    insert_submit_request(db, PR_TO_SR_1)
    insert_submit_request(db, PR_TO_SR_2)

    assert len(find_submitrequests(db)) == 2


@pytest.mark.parametrize(
    "kwargs,expected_srs",
    [
        ({"sr_id": PR_TO_SR_1.submit_request_id}, [PR_TO_SR_1]),
        ({"sr_id": PR_TO_SR_2.submit_request_id}, [PR_TO_SR_2]),
        ({"sr_id": 6666}, []),
        ({"obs_package_name": PR_TO_SR_1.obs_package_name}, [PR_TO_SR_1]),
        ({"obs_project_name": PR_TO_SR_2.obs_project_name}, [PR_TO_SR_2]),
        (
            {
                "obs_project_name": PR_TO_SR_2.obs_project_name,
                "obs_package_name": PR_TO_SR_2.obs_package_name,
            },
            [PR_TO_SR_2],
        ),
        (
            {
                "sr_id": PR_TO_SR_1.submit_request_id,
                "obs_project_name": PR_TO_SR_1.obs_project_name,
                "obs_package_name": PR_TO_SR_1.obs_package_name,
            },
            [PR_TO_SR_1],
        ),
        ({"sr_id": 666, "obs_project_name": "foobar"}, []),
    ],
)
def test_find_sr(
    db: str, kwargs, expected_srs: list[PullRequestToSubmitRequest]
) -> None:
    insert_submit_request(db, PR_TO_SR_1)
    insert_submit_request(db, PR_TO_SR_2)

    assert find_submitrequests(db, **kwargs) == expected_srs


def test_remove_sr(db: str) -> None:
    insert_submit_request(db, PR_TO_SR_1)
    insert_submit_request(db, PR_TO_SR_2)

    assert len(find_submitrequests(db)) == 2

    remove_submit_request(db, PR_TO_SR_1.submit_request_id)

    assert find_submitrequests(db) == [PR_TO_SR_2]
