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


class TransferRepoOption(object):
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
    swagger_types = {"new_owner": "str", "team_ids": "list[int]"}

    attribute_map = {"new_owner": "new_owner", "team_ids": "team_ids"}

    def __init__(
        self, new_owner=None, team_ids=None, _configuration=None
    ):  # noqa: E501
        """TransferRepoOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._new_owner = None
        self._team_ids = None
        self.discriminator = None

        self.new_owner = new_owner
        if team_ids is not None:
            self.team_ids = team_ids

    @property
    def new_owner(self):
        """Gets the new_owner of this TransferRepoOption.  # noqa: E501


        :return: The new_owner of this TransferRepoOption.  # noqa: E501
        :rtype: str
        """
        return self._new_owner

    @new_owner.setter
    def new_owner(self, new_owner):
        """Sets the new_owner of this TransferRepoOption.


        :param new_owner: The new_owner of this TransferRepoOption.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and new_owner is None:
            raise ValueError(
                "Invalid value for `new_owner`, must not be `None`"
            )  # noqa: E501

        self._new_owner = new_owner

    @property
    def team_ids(self):
        """Gets the team_ids of this TransferRepoOption.  # noqa: E501

        ID of the team or teams to add to the repository. Teams can only be added to organization-owned repositories.  # noqa: E501

        :return: The team_ids of this TransferRepoOption.  # noqa: E501
        :rtype: list[int]
        """
        return self._team_ids

    @team_ids.setter
    def team_ids(self, team_ids):
        """Sets the team_ids of this TransferRepoOption.

        ID of the team or teams to add to the repository. Teams can only be added to organization-owned repositories.  # noqa: E501

        :param team_ids: The team_ids of this TransferRepoOption.  # noqa: E501
        :type: list[int]
        """

        self._team_ids = team_ids

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
        if issubclass(TransferRepoOption, dict):
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
        if not isinstance(other, TransferRepoOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransferRepoOption):
            return True

        return self.to_dict() != other.to_dict()
