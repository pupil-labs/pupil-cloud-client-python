# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pupilcloud.configuration import Configuration


class LabelPatchRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'color': 'str',
        'created_at': 'datetime',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'recording_ids': 'list[str]',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'color': 'color',
        'created_at': 'created_at',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'recording_ids': 'recording_ids',
        'updated_at': 'updated_at'
    }

    def __init__(self, color=None, created_at=None, description=None, id=None, name=None, recording_ids=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """LabelPatchRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._color = None
        self._created_at = None
        self._description = None
        self._id = None
        self._name = None
        self._recording_ids = None
        self._updated_at = None
        self.discriminator = None

        if color is not None:
            self.color = color
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        self.name = name
        if recording_ids is not None:
            self.recording_ids = recording_ids
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def color(self):
        """Gets the color of this LabelPatchRequest.  # noqa: E501


        :return: The color of this LabelPatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this LabelPatchRequest.


        :param color: The color of this LabelPatchRequest.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def created_at(self):
        """Gets the created_at of this LabelPatchRequest.  # noqa: E501


        :return: The created_at of this LabelPatchRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LabelPatchRequest.


        :param created_at: The created_at of this LabelPatchRequest.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this LabelPatchRequest.  # noqa: E501


        :return: The description of this LabelPatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LabelPatchRequest.


        :param description: The description of this LabelPatchRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this LabelPatchRequest.  # noqa: E501


        :return: The id of this LabelPatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LabelPatchRequest.


        :param id: The id of this LabelPatchRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this LabelPatchRequest.  # noqa: E501


        :return: The name of this LabelPatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LabelPatchRequest.


        :param name: The name of this LabelPatchRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def recording_ids(self):
        """Gets the recording_ids of this LabelPatchRequest.  # noqa: E501


        :return: The recording_ids of this LabelPatchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._recording_ids

    @recording_ids.setter
    def recording_ids(self, recording_ids):
        """Sets the recording_ids of this LabelPatchRequest.


        :param recording_ids: The recording_ids of this LabelPatchRequest.  # noqa: E501
        :type: list[str]
        """

        self._recording_ids = recording_ids

    @property
    def updated_at(self):
        """Gets the updated_at of this LabelPatchRequest.  # noqa: E501


        :return: The updated_at of this LabelPatchRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LabelPatchRequest.


        :param updated_at: The updated_at of this LabelPatchRequest.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LabelPatchRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LabelPatchRequest):
            return True

        return self.to_dict() != other.to_dict()
