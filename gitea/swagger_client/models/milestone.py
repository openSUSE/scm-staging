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


class Milestone(object):
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
        "closed_at": "datetime",
        "closed_issues": "int",
        "created_at": "datetime",
        "description": "str",
        "due_on": "datetime",
        "id": "int",
        "open_issues": "int",
        "state": "StateType",
        "title": "str",
        "updated_at": "datetime",
    }

    attribute_map = {
        "closed_at": "closed_at",
        "closed_issues": "closed_issues",
        "created_at": "created_at",
        "description": "description",
        "due_on": "due_on",
        "id": "id",
        "open_issues": "open_issues",
        "state": "state",
        "title": "title",
        "updated_at": "updated_at",
    }

    def __init__(
        self,
        closed_at=None,
        closed_issues=None,
        created_at=None,
        description=None,
        due_on=None,
        id=None,
        open_issues=None,
        state=None,
        title=None,
        updated_at=None,
        _configuration=None,
    ):  # noqa: E501
        """Milestone - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._closed_at = None
        self._closed_issues = None
        self._created_at = None
        self._description = None
        self._due_on = None
        self._id = None
        self._open_issues = None
        self._state = None
        self._title = None
        self._updated_at = None
        self.discriminator = None

        if closed_at is not None:
            self.closed_at = closed_at
        if closed_issues is not None:
            self.closed_issues = closed_issues
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if due_on is not None:
            self.due_on = due_on
        if id is not None:
            self.id = id
        if open_issues is not None:
            self.open_issues = open_issues
        if state is not None:
            self.state = state
        if title is not None:
            self.title = title
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def closed_at(self):
        """Gets the closed_at of this Milestone.  # noqa: E501


        :return: The closed_at of this Milestone.  # noqa: E501
        :rtype: datetime
        """
        return self._closed_at

    @closed_at.setter
    def closed_at(self, closed_at):
        """Sets the closed_at of this Milestone.


        :param closed_at: The closed_at of this Milestone.  # noqa: E501
        :type: datetime
        """

        self._closed_at = closed_at

    @property
    def closed_issues(self):
        """Gets the closed_issues of this Milestone.  # noqa: E501


        :return: The closed_issues of this Milestone.  # noqa: E501
        :rtype: int
        """
        return self._closed_issues

    @closed_issues.setter
    def closed_issues(self, closed_issues):
        """Sets the closed_issues of this Milestone.


        :param closed_issues: The closed_issues of this Milestone.  # noqa: E501
        :type: int
        """

        self._closed_issues = closed_issues

    @property
    def created_at(self):
        """Gets the created_at of this Milestone.  # noqa: E501


        :return: The created_at of this Milestone.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Milestone.


        :param created_at: The created_at of this Milestone.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this Milestone.  # noqa: E501


        :return: The description of this Milestone.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Milestone.


        :param description: The description of this Milestone.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def due_on(self):
        """Gets the due_on of this Milestone.  # noqa: E501


        :return: The due_on of this Milestone.  # noqa: E501
        :rtype: datetime
        """
        return self._due_on

    @due_on.setter
    def due_on(self, due_on):
        """Sets the due_on of this Milestone.


        :param due_on: The due_on of this Milestone.  # noqa: E501
        :type: datetime
        """

        self._due_on = due_on

    @property
    def id(self):
        """Gets the id of this Milestone.  # noqa: E501


        :return: The id of this Milestone.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Milestone.


        :param id: The id of this Milestone.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def open_issues(self):
        """Gets the open_issues of this Milestone.  # noqa: E501


        :return: The open_issues of this Milestone.  # noqa: E501
        :rtype: int
        """
        return self._open_issues

    @open_issues.setter
    def open_issues(self, open_issues):
        """Sets the open_issues of this Milestone.


        :param open_issues: The open_issues of this Milestone.  # noqa: E501
        :type: int
        """

        self._open_issues = open_issues

    @property
    def state(self):
        """Gets the state of this Milestone.  # noqa: E501


        :return: The state of this Milestone.  # noqa: E501
        :rtype: StateType
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Milestone.


        :param state: The state of this Milestone.  # noqa: E501
        :type: StateType
        """

        self._state = state

    @property
    def title(self):
        """Gets the title of this Milestone.  # noqa: E501


        :return: The title of this Milestone.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Milestone.


        :param title: The title of this Milestone.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def updated_at(self):
        """Gets the updated_at of this Milestone.  # noqa: E501


        :return: The updated_at of this Milestone.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Milestone.


        :param updated_at: The updated_at of this Milestone.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if issubclass(Milestone, dict):
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
        if not isinstance(other, Milestone):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Milestone):
            return True

        return self.to_dict() != other.to_dict()
