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


class WearerPatchRequest(object):
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
        'archived_at': 'datetime',
        'created_at': 'datetime',
        'id': 'str',
        'name': 'str',
        'offset_correction': 'OffsetCorrection',
        'photo_url': 'str',
        'training_accuracy': 'float',
        'training_updated_on': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'archived_at': 'archived_at',
        'created_at': 'created_at',
        'id': 'id',
        'name': 'name',
        'offset_correction': 'offset_correction',
        'photo_url': 'photo_url',
        'training_accuracy': 'training_accuracy',
        'training_updated_on': 'training_updated_on',
        'updated_at': 'updated_at'
    }

    def __init__(self, archived_at=None, created_at=None, id=None, name=None, offset_correction=None, photo_url=None, training_accuracy=None, training_updated_on=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """WearerPatchRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._archived_at = None
        self._created_at = None
        self._id = None
        self._name = None
        self._offset_correction = None
        self._photo_url = None
        self._training_accuracy = None
        self._training_updated_on = None
        self._updated_at = None
        self.discriminator = None

        if archived_at is not None:
            self.archived_at = archived_at
        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        self.name = name
        if offset_correction is not None:
            self.offset_correction = offset_correction
        if photo_url is not None:
            self.photo_url = photo_url
        if training_accuracy is not None:
            self.training_accuracy = training_accuracy
        if training_updated_on is not None:
            self.training_updated_on = training_updated_on
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def archived_at(self):
        """Gets the archived_at of this WearerPatchRequest.  # noqa: E501


        :return: The archived_at of this WearerPatchRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this WearerPatchRequest.


        :param archived_at: The archived_at of this WearerPatchRequest.  # noqa: E501
        :type: datetime
        """

        self._archived_at = archived_at

    @property
    def created_at(self):
        """Gets the created_at of this WearerPatchRequest.  # noqa: E501


        :return: The created_at of this WearerPatchRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WearerPatchRequest.


        :param created_at: The created_at of this WearerPatchRequest.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this WearerPatchRequest.  # noqa: E501


        :return: The id of this WearerPatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WearerPatchRequest.


        :param id: The id of this WearerPatchRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this WearerPatchRequest.  # noqa: E501


        :return: The name of this WearerPatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WearerPatchRequest.


        :param name: The name of this WearerPatchRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def offset_correction(self):
        """Gets the offset_correction of this WearerPatchRequest.  # noqa: E501


        :return: The offset_correction of this WearerPatchRequest.  # noqa: E501
        :rtype: OffsetCorrection
        """
        return self._offset_correction

    @offset_correction.setter
    def offset_correction(self, offset_correction):
        """Sets the offset_correction of this WearerPatchRequest.


        :param offset_correction: The offset_correction of this WearerPatchRequest.  # noqa: E501
        :type: OffsetCorrection
        """

        self._offset_correction = offset_correction

    @property
    def photo_url(self):
        """Gets the photo_url of this WearerPatchRequest.  # noqa: E501


        :return: The photo_url of this WearerPatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._photo_url

    @photo_url.setter
    def photo_url(self, photo_url):
        """Sets the photo_url of this WearerPatchRequest.


        :param photo_url: The photo_url of this WearerPatchRequest.  # noqa: E501
        :type: str
        """

        self._photo_url = photo_url

    @property
    def training_accuracy(self):
        """Gets the training_accuracy of this WearerPatchRequest.  # noqa: E501


        :return: The training_accuracy of this WearerPatchRequest.  # noqa: E501
        :rtype: float
        """
        return self._training_accuracy

    @training_accuracy.setter
    def training_accuracy(self, training_accuracy):
        """Sets the training_accuracy of this WearerPatchRequest.


        :param training_accuracy: The training_accuracy of this WearerPatchRequest.  # noqa: E501
        :type: float
        """

        self._training_accuracy = training_accuracy

    @property
    def training_updated_on(self):
        """Gets the training_updated_on of this WearerPatchRequest.  # noqa: E501


        :return: The training_updated_on of this WearerPatchRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._training_updated_on

    @training_updated_on.setter
    def training_updated_on(self, training_updated_on):
        """Sets the training_updated_on of this WearerPatchRequest.


        :param training_updated_on: The training_updated_on of this WearerPatchRequest.  # noqa: E501
        :type: datetime
        """

        self._training_updated_on = training_updated_on

    @property
    def updated_at(self):
        """Gets the updated_at of this WearerPatchRequest.  # noqa: E501


        :return: The updated_at of this WearerPatchRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this WearerPatchRequest.


        :param updated_at: The updated_at of this WearerPatchRequest.  # noqa: E501
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
        if not isinstance(other, WearerPatchRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WearerPatchRequest):
            return True

        return self.to_dict() != other.to_dict()
