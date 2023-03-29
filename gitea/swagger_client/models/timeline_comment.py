# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class TimelineComment(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "assignee": "User",
        "assignee_team": "Team",
        "body": "str",
        "created_at": "datetime",
        "dependent_issue": "Issue",
        "html_url": "str",
        "id": "int",
        "issue_url": "str",
        "label": "Label",
        "milestone": "Milestone",
        "new_ref": "str",
        "new_title": "str",
        "old_milestone": "Milestone",
        "old_project_id": "int",
        "old_ref": "str",
        "old_title": "str",
        "project_id": "int",
        "pull_request_url": "str",
        "ref_action": "str",
        "ref_comment": "Comment",
        "ref_commit_sha": "str",
        "ref_issue": "Issue",
        "removed_assignee": "bool",
        "resolve_doer": "User",
        "review_id": "int",
        "tracked_time": "TrackedTime",
        "type": "str",
        "updated_at": "datetime",
        "user": "User",
    }

    attribute_map = {
        "assignee": "assignee",
        "assignee_team": "assignee_team",
        "body": "body",
        "created_at": "created_at",
        "dependent_issue": "dependent_issue",
        "html_url": "html_url",
        "id": "id",
        "issue_url": "issue_url",
        "label": "label",
        "milestone": "milestone",
        "new_ref": "new_ref",
        "new_title": "new_title",
        "old_milestone": "old_milestone",
        "old_project_id": "old_project_id",
        "old_ref": "old_ref",
        "old_title": "old_title",
        "project_id": "project_id",
        "pull_request_url": "pull_request_url",
        "ref_action": "ref_action",
        "ref_comment": "ref_comment",
        "ref_commit_sha": "ref_commit_sha",
        "ref_issue": "ref_issue",
        "removed_assignee": "removed_assignee",
        "resolve_doer": "resolve_doer",
        "review_id": "review_id",
        "tracked_time": "tracked_time",
        "type": "type",
        "updated_at": "updated_at",
        "user": "user",
    }

    def __init__(
        self,
        assignee=None,
        assignee_team=None,
        body=None,
        created_at=None,
        dependent_issue=None,
        html_url=None,
        id=None,
        issue_url=None,
        label=None,
        milestone=None,
        new_ref=None,
        new_title=None,
        old_milestone=None,
        old_project_id=None,
        old_ref=None,
        old_title=None,
        project_id=None,
        pull_request_url=None,
        ref_action=None,
        ref_comment=None,
        ref_commit_sha=None,
        ref_issue=None,
        removed_assignee=None,
        resolve_doer=None,
        review_id=None,
        tracked_time=None,
        type=None,
        updated_at=None,
        user=None,
        _configuration=None,
    ):  # noqa: E501
        """TimelineComment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assignee = None
        self._assignee_team = None
        self._body = None
        self._created_at = None
        self._dependent_issue = None
        self._html_url = None
        self._id = None
        self._issue_url = None
        self._label = None
        self._milestone = None
        self._new_ref = None
        self._new_title = None
        self._old_milestone = None
        self._old_project_id = None
        self._old_ref = None
        self._old_title = None
        self._project_id = None
        self._pull_request_url = None
        self._ref_action = None
        self._ref_comment = None
        self._ref_commit_sha = None
        self._ref_issue = None
        self._removed_assignee = None
        self._resolve_doer = None
        self._review_id = None
        self._tracked_time = None
        self._type = None
        self._updated_at = None
        self._user = None
        self.discriminator = None

        if assignee is not None:
            self.assignee = assignee
        if assignee_team is not None:
            self.assignee_team = assignee_team
        if body is not None:
            self.body = body
        if created_at is not None:
            self.created_at = created_at
        if dependent_issue is not None:
            self.dependent_issue = dependent_issue
        if html_url is not None:
            self.html_url = html_url
        if id is not None:
            self.id = id
        if issue_url is not None:
            self.issue_url = issue_url
        if label is not None:
            self.label = label
        if milestone is not None:
            self.milestone = milestone
        if new_ref is not None:
            self.new_ref = new_ref
        if new_title is not None:
            self.new_title = new_title
        if old_milestone is not None:
            self.old_milestone = old_milestone
        if old_project_id is not None:
            self.old_project_id = old_project_id
        if old_ref is not None:
            self.old_ref = old_ref
        if old_title is not None:
            self.old_title = old_title
        if project_id is not None:
            self.project_id = project_id
        if pull_request_url is not None:
            self.pull_request_url = pull_request_url
        if ref_action is not None:
            self.ref_action = ref_action
        if ref_comment is not None:
            self.ref_comment = ref_comment
        if ref_commit_sha is not None:
            self.ref_commit_sha = ref_commit_sha
        if ref_issue is not None:
            self.ref_issue = ref_issue
        if removed_assignee is not None:
            self.removed_assignee = removed_assignee
        if resolve_doer is not None:
            self.resolve_doer = resolve_doer
        if review_id is not None:
            self.review_id = review_id
        if tracked_time is not None:
            self.tracked_time = tracked_time
        if type is not None:
            self.type = type
        if updated_at is not None:
            self.updated_at = updated_at
        if user is not None:
            self.user = user

    @property
    def assignee(self):
        """Gets the assignee of this TimelineComment.  # noqa: E501


        :return: The assignee of this TimelineComment.  # noqa: E501
        :rtype: User
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """Sets the assignee of this TimelineComment.


        :param assignee: The assignee of this TimelineComment.  # noqa: E501
        :type: User
        """

        self._assignee = assignee

    @property
    def assignee_team(self):
        """Gets the assignee_team of this TimelineComment.  # noqa: E501


        :return: The assignee_team of this TimelineComment.  # noqa: E501
        :rtype: Team
        """
        return self._assignee_team

    @assignee_team.setter
    def assignee_team(self, assignee_team):
        """Sets the assignee_team of this TimelineComment.


        :param assignee_team: The assignee_team of this TimelineComment.  # noqa: E501
        :type: Team
        """

        self._assignee_team = assignee_team

    @property
    def body(self):
        """Gets the body of this TimelineComment.  # noqa: E501


        :return: The body of this TimelineComment.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this TimelineComment.


        :param body: The body of this TimelineComment.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def created_at(self):
        """Gets the created_at of this TimelineComment.  # noqa: E501


        :return: The created_at of this TimelineComment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TimelineComment.


        :param created_at: The created_at of this TimelineComment.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def dependent_issue(self):
        """Gets the dependent_issue of this TimelineComment.  # noqa: E501


        :return: The dependent_issue of this TimelineComment.  # noqa: E501
        :rtype: Issue
        """
        return self._dependent_issue

    @dependent_issue.setter
    def dependent_issue(self, dependent_issue):
        """Sets the dependent_issue of this TimelineComment.


        :param dependent_issue: The dependent_issue of this TimelineComment.  # noqa: E501
        :type: Issue
        """

        self._dependent_issue = dependent_issue

    @property
    def html_url(self):
        """Gets the html_url of this TimelineComment.  # noqa: E501


        :return: The html_url of this TimelineComment.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this TimelineComment.


        :param html_url: The html_url of this TimelineComment.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def id(self):
        """Gets the id of this TimelineComment.  # noqa: E501


        :return: The id of this TimelineComment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TimelineComment.


        :param id: The id of this TimelineComment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def issue_url(self):
        """Gets the issue_url of this TimelineComment.  # noqa: E501


        :return: The issue_url of this TimelineComment.  # noqa: E501
        :rtype: str
        """
        return self._issue_url

    @issue_url.setter
    def issue_url(self, issue_url):
        """Sets the issue_url of this TimelineComment.


        :param issue_url: The issue_url of this TimelineComment.  # noqa: E501
        :type: str
        """

        self._issue_url = issue_url

    @property
    def label(self):
        """Gets the label of this TimelineComment.  # noqa: E501


        :return: The label of this TimelineComment.  # noqa: E501
        :rtype: Label
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this TimelineComment.


        :param label: The label of this TimelineComment.  # noqa: E501
        :type: Label
        """

        self._label = label

    @property
    def milestone(self):
        """Gets the milestone of this TimelineComment.  # noqa: E501


        :return: The milestone of this TimelineComment.  # noqa: E501
        :rtype: Milestone
        """
        return self._milestone

    @milestone.setter
    def milestone(self, milestone):
        """Sets the milestone of this TimelineComment.


        :param milestone: The milestone of this TimelineComment.  # noqa: E501
        :type: Milestone
        """

        self._milestone = milestone

    @property
    def new_ref(self):
        """Gets the new_ref of this TimelineComment.  # noqa: E501


        :return: The new_ref of this TimelineComment.  # noqa: E501
        :rtype: str
        """
        return self._new_ref

    @new_ref.setter
    def new_ref(self, new_ref):
        """Sets the new_ref of this TimelineComment.


        :param new_ref: The new_ref of this TimelineComment.  # noqa: E501
        :type: str
        """

        self._new_ref = new_ref

    @property
    def new_title(self):
        """Gets the new_title of this TimelineComment.  # noqa: E501


        :return: The new_title of this TimelineComment.  # noqa: E501
        :rtype: str
        """
        return self._new_title

    @new_title.setter
    def new_title(self, new_title):
        """Sets the new_title of this TimelineComment.


        :param new_title: The new_title of this TimelineComment.  # noqa: E501
        :type: str
        """

        self._new_title = new_title

    @property
    def old_milestone(self):
        """Gets the old_milestone of this TimelineComment.  # noqa: E501


        :return: The old_milestone of this TimelineComment.  # noqa: E501
        :rtype: Milestone
        """
        return self._old_milestone

    @old_milestone.setter
    def old_milestone(self, old_milestone):
        """Sets the old_milestone of this TimelineComment.


        :param old_milestone: The old_milestone of this TimelineComment.  # noqa: E501
        :type: Milestone
        """

        self._old_milestone = old_milestone

    @property
    def old_project_id(self):
        """Gets the old_project_id of this TimelineComment.  # noqa: E501


        :return: The old_project_id of this TimelineComment.  # noqa: E501
        :rtype: int
        """
        return self._old_project_id

    @old_project_id.setter
    def old_project_id(self, old_project_id):
        """Sets the old_project_id of this TimelineComment.


        :param old_project_id: The old_project_id of this TimelineComment.  # noqa: E501
        :type: int
        """

        self._old_project_id = old_project_id

    @property
    def old_ref(self):
        """Gets the old_ref of this TimelineComment.  # noqa: E501


        :return: The old_ref of this TimelineComment.  # noqa: E501
        :rtype: str
        """
        return self._old_ref

    @old_ref.setter
    def old_ref(self, old_ref):
        """Sets the old_ref of this TimelineComment.


        :param old_ref: The old_ref of this TimelineComment.  # noqa: E501
        :type: str
        """

        self._old_ref = old_ref

    @property
    def old_title(self):
        """Gets the old_title of this TimelineComment.  # noqa: E501


        :return: The old_title of this TimelineComment.  # noqa: E501
        :rtype: str
        """
        return self._old_title

    @old_title.setter
    def old_title(self, old_title):
        """Sets the old_title of this TimelineComment.


        :param old_title: The old_title of this TimelineComment.  # noqa: E501
        :type: str
        """

        self._old_title = old_title

    @property
    def project_id(self):
        """Gets the project_id of this TimelineComment.  # noqa: E501


        :return: The project_id of this TimelineComment.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TimelineComment.


        :param project_id: The project_id of this TimelineComment.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def pull_request_url(self):
        """Gets the pull_request_url of this TimelineComment.  # noqa: E501


        :return: The pull_request_url of this TimelineComment.  # noqa: E501
        :rtype: str
        """
        return self._pull_request_url

    @pull_request_url.setter
    def pull_request_url(self, pull_request_url):
        """Sets the pull_request_url of this TimelineComment.


        :param pull_request_url: The pull_request_url of this TimelineComment.  # noqa: E501
        :type: str
        """

        self._pull_request_url = pull_request_url

    @property
    def ref_action(self):
        """Gets the ref_action of this TimelineComment.  # noqa: E501


        :return: The ref_action of this TimelineComment.  # noqa: E501
        :rtype: str
        """
        return self._ref_action

    @ref_action.setter
    def ref_action(self, ref_action):
        """Sets the ref_action of this TimelineComment.


        :param ref_action: The ref_action of this TimelineComment.  # noqa: E501
        :type: str
        """

        self._ref_action = ref_action

    @property
    def ref_comment(self):
        """Gets the ref_comment of this TimelineComment.  # noqa: E501


        :return: The ref_comment of this TimelineComment.  # noqa: E501
        :rtype: Comment
        """
        return self._ref_comment

    @ref_comment.setter
    def ref_comment(self, ref_comment):
        """Sets the ref_comment of this TimelineComment.


        :param ref_comment: The ref_comment of this TimelineComment.  # noqa: E501
        :type: Comment
        """

        self._ref_comment = ref_comment

    @property
    def ref_commit_sha(self):
        """Gets the ref_commit_sha of this TimelineComment.  # noqa: E501

        commit SHA where issue/PR was referenced  # noqa: E501

        :return: The ref_commit_sha of this TimelineComment.  # noqa: E501
        :rtype: str
        """
        return self._ref_commit_sha

    @ref_commit_sha.setter
    def ref_commit_sha(self, ref_commit_sha):
        """Sets the ref_commit_sha of this TimelineComment.

        commit SHA where issue/PR was referenced  # noqa: E501

        :param ref_commit_sha: The ref_commit_sha of this TimelineComment.  # noqa: E501
        :type: str
        """

        self._ref_commit_sha = ref_commit_sha

    @property
    def ref_issue(self):
        """Gets the ref_issue of this TimelineComment.  # noqa: E501


        :return: The ref_issue of this TimelineComment.  # noqa: E501
        :rtype: Issue
        """
        return self._ref_issue

    @ref_issue.setter
    def ref_issue(self, ref_issue):
        """Sets the ref_issue of this TimelineComment.


        :param ref_issue: The ref_issue of this TimelineComment.  # noqa: E501
        :type: Issue
        """

        self._ref_issue = ref_issue

    @property
    def removed_assignee(self):
        """Gets the removed_assignee of this TimelineComment.  # noqa: E501

        whether the assignees were removed or added  # noqa: E501

        :return: The removed_assignee of this TimelineComment.  # noqa: E501
        :rtype: bool
        """
        return self._removed_assignee

    @removed_assignee.setter
    def removed_assignee(self, removed_assignee):
        """Sets the removed_assignee of this TimelineComment.

        whether the assignees were removed or added  # noqa: E501

        :param removed_assignee: The removed_assignee of this TimelineComment.  # noqa: E501
        :type: bool
        """

        self._removed_assignee = removed_assignee

    @property
    def resolve_doer(self):
        """Gets the resolve_doer of this TimelineComment.  # noqa: E501


        :return: The resolve_doer of this TimelineComment.  # noqa: E501
        :rtype: User
        """
        return self._resolve_doer

    @resolve_doer.setter
    def resolve_doer(self, resolve_doer):
        """Sets the resolve_doer of this TimelineComment.


        :param resolve_doer: The resolve_doer of this TimelineComment.  # noqa: E501
        :type: User
        """

        self._resolve_doer = resolve_doer

    @property
    def review_id(self):
        """Gets the review_id of this TimelineComment.  # noqa: E501


        :return: The review_id of this TimelineComment.  # noqa: E501
        :rtype: int
        """
        return self._review_id

    @review_id.setter
    def review_id(self, review_id):
        """Sets the review_id of this TimelineComment.


        :param review_id: The review_id of this TimelineComment.  # noqa: E501
        :type: int
        """

        self._review_id = review_id

    @property
    def tracked_time(self):
        """Gets the tracked_time of this TimelineComment.  # noqa: E501


        :return: The tracked_time of this TimelineComment.  # noqa: E501
        :rtype: TrackedTime
        """
        return self._tracked_time

    @tracked_time.setter
    def tracked_time(self, tracked_time):
        """Sets the tracked_time of this TimelineComment.


        :param tracked_time: The tracked_time of this TimelineComment.  # noqa: E501
        :type: TrackedTime
        """

        self._tracked_time = tracked_time

    @property
    def type(self):
        """Gets the type of this TimelineComment.  # noqa: E501


        :return: The type of this TimelineComment.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TimelineComment.


        :param type: The type of this TimelineComment.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this TimelineComment.  # noqa: E501


        :return: The updated_at of this TimelineComment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TimelineComment.


        :param updated_at: The updated_at of this TimelineComment.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this TimelineComment.  # noqa: E501


        :return: The user of this TimelineComment.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TimelineComment.


        :param user: The user of this TimelineComment.  # noqa: E501
        :type: User
        """

        self._user = user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(TimelineComment, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TimelineComment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimelineComment):
            return True

        return self.to_dict() != other.to_dict()
