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


class StopWatch(object):
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
        "created": "datetime",
        "duration": "str",
        "issue_index": "int",
        "issue_title": "str",
        "repo_name": "str",
        "repo_owner_name": "str",
        "seconds": "int",
    }

    attribute_map = {
        "created": "created",
        "duration": "duration",
        "issue_index": "issue_index",
        "issue_title": "issue_title",
        "repo_name": "repo_name",
        "repo_owner_name": "repo_owner_name",
        "seconds": "seconds",
    }

    def __init__(
        self,
        created=None,
        duration=None,
        issue_index=None,
        issue_title=None,
        repo_name=None,
        repo_owner_name=None,
        seconds=None,
        _configuration=None,
    ):  # noqa: E501
        """StopWatch - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created = None
        self._duration = None
        self._issue_index = None
        self._issue_title = None
        self._repo_name = None
        self._repo_owner_name = None
        self._seconds = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if duration is not None:
            self.duration = duration
        if issue_index is not None:
            self.issue_index = issue_index
        if issue_title is not None:
            self.issue_title = issue_title
        if repo_name is not None:
            self.repo_name = repo_name
        if repo_owner_name is not None:
            self.repo_owner_name = repo_owner_name
        if seconds is not None:
            self.seconds = seconds

    @property
    def created(self):
        """Gets the created of this StopWatch.  # noqa: E501


        :return: The created of this StopWatch.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this StopWatch.


        :param created: The created of this StopWatch.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def duration(self):
        """Gets the duration of this StopWatch.  # noqa: E501


        :return: The duration of this StopWatch.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this StopWatch.


        :param duration: The duration of this StopWatch.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def issue_index(self):
        """Gets the issue_index of this StopWatch.  # noqa: E501


        :return: The issue_index of this StopWatch.  # noqa: E501
        :rtype: int
        """
        return self._issue_index

    @issue_index.setter
    def issue_index(self, issue_index):
        """Sets the issue_index of this StopWatch.


        :param issue_index: The issue_index of this StopWatch.  # noqa: E501
        :type: int
        """

        self._issue_index = issue_index

    @property
    def issue_title(self):
        """Gets the issue_title of this StopWatch.  # noqa: E501


        :return: The issue_title of this StopWatch.  # noqa: E501
        :rtype: str
        """
        return self._issue_title

    @issue_title.setter
    def issue_title(self, issue_title):
        """Sets the issue_title of this StopWatch.


        :param issue_title: The issue_title of this StopWatch.  # noqa: E501
        :type: str
        """

        self._issue_title = issue_title

    @property
    def repo_name(self):
        """Gets the repo_name of this StopWatch.  # noqa: E501


        :return: The repo_name of this StopWatch.  # noqa: E501
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        """Sets the repo_name of this StopWatch.


        :param repo_name: The repo_name of this StopWatch.  # noqa: E501
        :type: str
        """

        self._repo_name = repo_name

    @property
    def repo_owner_name(self):
        """Gets the repo_owner_name of this StopWatch.  # noqa: E501


        :return: The repo_owner_name of this StopWatch.  # noqa: E501
        :rtype: str
        """
        return self._repo_owner_name

    @repo_owner_name.setter
    def repo_owner_name(self, repo_owner_name):
        """Sets the repo_owner_name of this StopWatch.


        :param repo_owner_name: The repo_owner_name of this StopWatch.  # noqa: E501
        :type: str
        """

        self._repo_owner_name = repo_owner_name

    @property
    def seconds(self):
        """Gets the seconds of this StopWatch.  # noqa: E501


        :return: The seconds of this StopWatch.  # noqa: E501
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """Sets the seconds of this StopWatch.


        :param seconds: The seconds of this StopWatch.  # noqa: E501
        :type: int
        """

        self._seconds = seconds

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
        if issubclass(StopWatch, dict):
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
        if not isinstance(other, StopWatch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StopWatch):
            return True

        return self.to_dict() != other.to_dict()
