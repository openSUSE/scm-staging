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


class PayloadCommit(object):
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
        "added": "list[str]",
        "author": "PayloadUser",
        "committer": "PayloadUser",
        "id": "str",
        "message": "str",
        "modified": "list[str]",
        "removed": "list[str]",
        "timestamp": "datetime",
        "url": "str",
        "verification": "PayloadCommitVerification",
    }

    attribute_map = {
        "added": "added",
        "author": "author",
        "committer": "committer",
        "id": "id",
        "message": "message",
        "modified": "modified",
        "removed": "removed",
        "timestamp": "timestamp",
        "url": "url",
        "verification": "verification",
    }

    def __init__(
        self,
        added=None,
        author=None,
        committer=None,
        id=None,
        message=None,
        modified=None,
        removed=None,
        timestamp=None,
        url=None,
        verification=None,
        _configuration=None,
    ):  # noqa: E501
        """PayloadCommit - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._added = None
        self._author = None
        self._committer = None
        self._id = None
        self._message = None
        self._modified = None
        self._removed = None
        self._timestamp = None
        self._url = None
        self._verification = None
        self.discriminator = None

        if added is not None:
            self.added = added
        if author is not None:
            self.author = author
        if committer is not None:
            self.committer = committer
        if id is not None:
            self.id = id
        if message is not None:
            self.message = message
        if modified is not None:
            self.modified = modified
        if removed is not None:
            self.removed = removed
        if timestamp is not None:
            self.timestamp = timestamp
        if url is not None:
            self.url = url
        if verification is not None:
            self.verification = verification

    @property
    def added(self):
        """Gets the added of this PayloadCommit.  # noqa: E501


        :return: The added of this PayloadCommit.  # noqa: E501
        :rtype: list[str]
        """
        return self._added

    @added.setter
    def added(self, added):
        """Sets the added of this PayloadCommit.


        :param added: The added of this PayloadCommit.  # noqa: E501
        :type: list[str]
        """

        self._added = added

    @property
    def author(self):
        """Gets the author of this PayloadCommit.  # noqa: E501


        :return: The author of this PayloadCommit.  # noqa: E501
        :rtype: PayloadUser
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this PayloadCommit.


        :param author: The author of this PayloadCommit.  # noqa: E501
        :type: PayloadUser
        """

        self._author = author

    @property
    def committer(self):
        """Gets the committer of this PayloadCommit.  # noqa: E501


        :return: The committer of this PayloadCommit.  # noqa: E501
        :rtype: PayloadUser
        """
        return self._committer

    @committer.setter
    def committer(self, committer):
        """Sets the committer of this PayloadCommit.


        :param committer: The committer of this PayloadCommit.  # noqa: E501
        :type: PayloadUser
        """

        self._committer = committer

    @property
    def id(self):
        """Gets the id of this PayloadCommit.  # noqa: E501

        sha1 hash of the commit  # noqa: E501

        :return: The id of this PayloadCommit.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PayloadCommit.

        sha1 hash of the commit  # noqa: E501

        :param id: The id of this PayloadCommit.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def message(self):
        """Gets the message of this PayloadCommit.  # noqa: E501


        :return: The message of this PayloadCommit.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PayloadCommit.


        :param message: The message of this PayloadCommit.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def modified(self):
        """Gets the modified of this PayloadCommit.  # noqa: E501


        :return: The modified of this PayloadCommit.  # noqa: E501
        :rtype: list[str]
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this PayloadCommit.


        :param modified: The modified of this PayloadCommit.  # noqa: E501
        :type: list[str]
        """

        self._modified = modified

    @property
    def removed(self):
        """Gets the removed of this PayloadCommit.  # noqa: E501


        :return: The removed of this PayloadCommit.  # noqa: E501
        :rtype: list[str]
        """
        return self._removed

    @removed.setter
    def removed(self, removed):
        """Sets the removed of this PayloadCommit.


        :param removed: The removed of this PayloadCommit.  # noqa: E501
        :type: list[str]
        """

        self._removed = removed

    @property
    def timestamp(self):
        """Gets the timestamp of this PayloadCommit.  # noqa: E501


        :return: The timestamp of this PayloadCommit.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this PayloadCommit.


        :param timestamp: The timestamp of this PayloadCommit.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def url(self):
        """Gets the url of this PayloadCommit.  # noqa: E501


        :return: The url of this PayloadCommit.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PayloadCommit.


        :param url: The url of this PayloadCommit.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def verification(self):
        """Gets the verification of this PayloadCommit.  # noqa: E501


        :return: The verification of this PayloadCommit.  # noqa: E501
        :rtype: PayloadCommitVerification
        """
        return self._verification

    @verification.setter
    def verification(self, verification):
        """Sets the verification of this PayloadCommit.


        :param verification: The verification of this PayloadCommit.  # noqa: E501
        :type: PayloadCommitVerification
        """

        self._verification = verification

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
        if issubclass(PayloadCommit, dict):
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
        if not isinstance(other, PayloadCommit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PayloadCommit):
            return True

        return self.to_dict() != other.to_dict()
