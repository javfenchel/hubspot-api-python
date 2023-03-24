# coding: utf-8

"""
    Calling Extensions API

    Provides a way for apps to add custom calling options to a contact record. This works in conjunction with the [Calling SDK](#), which is used to build your phone/calling UI. The endpoints here allow your service to appear as an option to HubSpot users when they access the *Call* action on a contact record. Once accessed, your custom phone/calling UI will be displayed in an iframe at the specified URL with the specified dimensions on that record.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.extensions.calling.configuration import Configuration


class SettingsResponse(object):
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
        "name": "str",
        "url": "str",
        "height": "int",
        "width": "int",
        "is_ready": "bool",
        "supports_custom_objects": "bool",
        "created_at": "datetime",
        "updated_at": "datetime",
    }

    attribute_map = {
        "name": "name",
        "url": "url",
        "height": "height",
        "width": "width",
        "is_ready": "isReady",
        "supports_custom_objects": "supportsCustomObjects",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
    }

    def __init__(
        self,
        name=None,
        url=None,
        height=None,
        width=None,
        is_ready=None,
        supports_custom_objects=None,
        created_at=None,
        updated_at=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """SettingsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._url = None
        self._height = None
        self._width = None
        self._is_ready = None
        self._supports_custom_objects = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.name = name
        self.url = url
        self.height = height
        self.width = width
        self.is_ready = is_ready
        self.supports_custom_objects = supports_custom_objects
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def name(self):
        """Gets the name of this SettingsResponse.  # noqa: E501

        The name of your calling service to display to users.  # noqa: E501

        :return: The name of this SettingsResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SettingsResponse.

        The name of your calling service to display to users.  # noqa: E501

        :param name: The name of this SettingsResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def url(self):
        """Gets the url of this SettingsResponse.  # noqa: E501

        The URL to your phone/calling UI, built with the [Calling SDK](#).  # noqa: E501

        :return: The url of this SettingsResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SettingsResponse.

        The URL to your phone/calling UI, built with the [Calling SDK](#).  # noqa: E501

        :param url: The url of this SettingsResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def height(self):
        """Gets the height of this SettingsResponse.  # noqa: E501

        The target height of the iframe that will contain your phone/calling UI.  # noqa: E501

        :return: The height of this SettingsResponse.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this SettingsResponse.

        The target height of the iframe that will contain your phone/calling UI.  # noqa: E501

        :param height: The height of this SettingsResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and height is None:  # noqa: E501
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def width(self):
        """Gets the width of this SettingsResponse.  # noqa: E501

        The target width of the iframe that will contain your phone/calling UI.  # noqa: E501

        :return: The width of this SettingsResponse.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this SettingsResponse.

        The target width of the iframe that will contain your phone/calling UI.  # noqa: E501

        :param width: The width of this SettingsResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and width is None:  # noqa: E501
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

    @property
    def is_ready(self):
        """Gets the is_ready of this SettingsResponse.  # noqa: E501

        When true, your service will appear as an option under the *Call* action in contact records of connected accounts.  # noqa: E501

        :return: The is_ready of this SettingsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_ready

    @is_ready.setter
    def is_ready(self, is_ready):
        """Sets the is_ready of this SettingsResponse.

        When true, your service will appear as an option under the *Call* action in contact records of connected accounts.  # noqa: E501

        :param is_ready: The is_ready of this SettingsResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_ready is None:  # noqa: E501
            raise ValueError("Invalid value for `is_ready`, must not be `None`")  # noqa: E501

        self._is_ready = is_ready

    @property
    def supports_custom_objects(self):
        """Gets the supports_custom_objects of this SettingsResponse.  # noqa: E501

        When true, you are indicating that your service is compatible with engagement v2 service and can be used with custom objects.  # noqa: E501

        :return: The supports_custom_objects of this SettingsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._supports_custom_objects

    @supports_custom_objects.setter
    def supports_custom_objects(self, supports_custom_objects):
        """Sets the supports_custom_objects of this SettingsResponse.

        When true, you are indicating that your service is compatible with engagement v2 service and can be used with custom objects.  # noqa: E501

        :param supports_custom_objects: The supports_custom_objects of this SettingsResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and supports_custom_objects is None:  # noqa: E501
            raise ValueError("Invalid value for `supports_custom_objects`, must not be `None`")  # noqa: E501

        self._supports_custom_objects = supports_custom_objects

    @property
    def created_at(self):
        """Gets the created_at of this SettingsResponse.  # noqa: E501

        When this calling extension was created.  # noqa: E501

        :return: The created_at of this SettingsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SettingsResponse.

        When this calling extension was created.  # noqa: E501

        :param created_at: The created_at of this SettingsResponse.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SettingsResponse.  # noqa: E501

        The last time the settings for this calling extension were modified.  # noqa: E501

        :return: The updated_at of this SettingsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SettingsResponse.

        The last time the settings for this calling extension were modified.  # noqa: E501

        :param updated_at: The updated_at of this SettingsResponse.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, SettingsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettingsResponse):
            return True

        return self.to_dict() != other.to_dict()
