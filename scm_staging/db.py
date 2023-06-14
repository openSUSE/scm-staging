"""This module contains the helper functions to store the created submitrequests
and the respective pull requests on gitea in a database to keep track of them.

The rabbit listener and the webhook share information via the database.

"""

import sqlite3

from pydantic import BaseModel


class PullRequestToSubmitRequest(BaseModel):
    """pydantic model used to store the submit requests and their corresponding
    pull requests on gitea.

    """

    #: numeric id of the SubmitRequest on OBS
    submit_request_id: int

    #: name of the project on OBS where the package is created
    obs_project_name: str

    #: name of the package on OBS where the pull request is checked out
    obs_package_name: str

    #: Owner of the repository against which the PR has been opened
    gitea_repo_owner: str

    #: Name of the repository against which the PR has been opened
    gitea_repo_name: str

    #: Number of the pull request via which the PR can be found in the web
    #: UI. This is **not** the ID of the pull request!
    pull_request_number: int

    #: flag whether the pull request should be merged once the submit request is
    #: accepted
    merge_pr: bool


_SR_ID_KEY = "id"
_OBS_PRJ_NAME_KEY = "obs_prj_name"
_OBS_PKG_NAME_KEY = "obs_pkg_name"
_GITEA_REPO_OWNER_KEY = "git_prj_name"
_GITEA_REPO_NAME_KEY = "git_pkg_name"
_PR_NUMBER_KEY = "pr_number"
_MERGE_PR_KEY = "merge_pr"
_TABLE_KEYS = [
    _SR_ID_KEY,
    _OBS_PRJ_NAME_KEY,
    _OBS_PKG_NAME_KEY,
    _GITEA_REPO_OWNER_KEY,
    _GITEA_REPO_NAME_KEY,
    _PR_NUMBER_KEY,
    _MERGE_PR_KEY,
]


def create_db(db_file: str) -> None:
    """Initializes the database and creates the required table if it does not
    yet exist. If the database and/or the table already exist, then this
    function does nothing.

    """
    con = sqlite3.connect(db_file)

    sql_cmd = (
        "CREATE TABLE IF NOT EXISTS requests("
        + ", ".join(
            f"{key} {type}"
            for key, type in (
                (_SR_ID_KEY, "INTEGER PRIMARY KEY"),
                (_OBS_PRJ_NAME_KEY, "VARCHAR"),
                (_OBS_PKG_NAME_KEY, "VARCHAR"),
                (_GITEA_REPO_OWNER_KEY, "VARCHAR"),
                (_GITEA_REPO_NAME_KEY, "VARCHAR"),
                (_PR_NUMBER_KEY, "INTEGER"),
                (_MERGE_PR_KEY, "BOOLEAN"),
            )
        )
        + ")"
    )

    with con:
        con.execute(sql_cmd)
    con.close()


def insert_submit_request(db_file: str, pr_to_sr: PullRequestToSubmitRequest) -> None:
    """Inserts the supplied :py:class:`PullRequestToSubmitRequest` into the
    database.

    """
    con = sqlite3.connect(db_file)
    sql_insert = (
        "INSERT INTO requests("
        + ", ".join(_TABLE_KEYS)
        + ") VALUES("
        + ", ".join("?" for _ in _TABLE_KEYS)
        + ")"
    )

    try:
        with con:
            con.execute(
                sql_insert,
                (
                    pr_to_sr.submit_request_id,
                    pr_to_sr.obs_project_name,
                    pr_to_sr.obs_package_name,
                    pr_to_sr.gitea_repo_owner,
                    pr_to_sr.gitea_repo_name,
                    pr_to_sr.pull_request_number,
                    pr_to_sr.merge_pr,
                ),
            )
    finally:
        con.close()


def remove_submit_request(db_file: str, sr_id: int) -> None:
    """Removes the submit request with the supplied id from the database."""
    con = sqlite3.connect(db_file)
    try:
        with con:
            con.execute("DELETE from requests where id = ?", (sr_id,))
    finally:
        con.close()


def find_submitrequests(
    db_file: str,
    *,
    sr_id: int | None = None,
    obs_project_name: str | None = None,
    obs_package_name: str | None = None,
) -> list[PullRequestToSubmitRequest]:
    """Returns all submitrequests from the database when no optional parameters
    are supplied. If any of the optional parameters is supplied then only
    submitrequests with that matching parameter are returned. If no
    submitrequests match, then an empty list is returned.

    """
    con = sqlite3.connect(db_file)
    try:
        with con:
            select = "SELECT * FROM requests"

            params: tuple[int | str, ...] = ()
            select_params = [
                (param, key)
                for param, key in (
                    (sr_id, _SR_ID_KEY),
                    (obs_project_name, _OBS_PRJ_NAME_KEY),
                    (obs_package_name, _OBS_PKG_NAME_KEY),
                )
                if param
            ]
            if select_params:
                select += " WHERE " + " AND ".join(
                    f"{key} = ?" for _, key in select_params
                )
                params = tuple(param for param, _ in select_params)

            res = con.execute(select, params)
            return [
                PullRequestToSubmitRequest(
                    submit_request_id=sr_id,
                    obs_project_name=obs_prj_name,
                    obs_package_name=obs_pkg_name,
                    gitea_repo_owner=repo_owner,
                    gitea_repo_name=repo_name,
                    pull_request_number=pr_num,
                    merge_pr=merge_pr,
                )
                for sr_id, obs_prj_name, obs_pkg_name, repo_owner, repo_name, pr_num, merge_pr in res.fetchall()
            ]
    finally:
        con.close()
