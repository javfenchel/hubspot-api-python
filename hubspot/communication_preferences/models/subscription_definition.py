# coding: utf-8

"""
    Subscriptions

    Subscriptions allow contacts to control what forms of communications they receive. Contacts can decide whether they want to receive communication pertaining to a specific topic, brand, or an entire HubSpot account.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.communication_preferences.configuration import Configuration


class SubscriptionDefinition(object):
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
        "id": "str",
        "name": "str",
        "description": "str",
        "purpose": "str",
        "communication_method": "str",
        "is_active": "bool",
        "is_default": "bool",
        "is_internal": "bool",
        "created_at": "datetime",
        "updated_at": "datetime",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "description": "description",
        "purpose": "purpose",
        "communication_method": "communicationMethod",
        "is_active": "isActive",
        "is_default": "isDefault",
        "is_internal": "isInternal",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
    }

    def __init__(
        self,
        id=None,
        name=None,
        description=None,
        purpose=None,
        communication_method=None,
        is_active=None,
        is_default=None,
        is_internal=None,
        created_at=None,
        updated_at=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """SubscriptionDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._purpose = None
        self._communication_method = None
        self._is_active = None
        self._is_default = None
        self._is_internal = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        if purpose is not None:
            self.purpose = purpose
        if communication_method is not None:
            self.communication_method = communication_method
        self.is_active = is_active
        self.is_default = is_default
        self.is_internal = is_internal
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this SubscriptionDefinition.  # noqa: E501

        The ID of the definition.  # noqa: E501

        :return: The id of this SubscriptionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionDefinition.

        The ID of the definition.  # noqa: E501

        :param id: The id of this SubscriptionDefinition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this SubscriptionDefinition.  # noqa: E501

        The name of the subscription.  # noqa: E501

        :return: The name of this SubscriptionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionDefinition.

        The name of the subscription.  # noqa: E501

        :param name: The name of this SubscriptionDefinition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this SubscriptionDefinition.  # noqa: E501

        A description of the subscription.  # noqa: E501

        :return: The description of this SubscriptionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubscriptionDefinition.

        A description of the subscription.  # noqa: E501

        :param description: The description of this SubscriptionDefinition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def purpose(self):
        """Gets the purpose of this SubscriptionDefinition.  # noqa: E501

        The purpose of this subscription or the department in your organization that uses it.  # noqa: E501

        :return: The purpose of this SubscriptionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this SubscriptionDefinition.

        The purpose of this subscription or the department in your organization that uses it.  # noqa: E501

        :param purpose: The purpose of this SubscriptionDefinition.  # noqa: E501
        :type: str
        """

        self._purpose = purpose

    @property
    def communication_method(self):
        """Gets the communication_method of this SubscriptionDefinition.  # noqa: E501

        The method or technology used to contact.  # noqa: E501

        :return: The communication_method of this SubscriptionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._communication_method

    @communication_method.setter
    def communication_method(self, communication_method):
        """Sets the communication_method of this SubscriptionDefinition.

        The method or technology used to contact.  # noqa: E501

        :param communication_method: The communication_method of this SubscriptionDefinition.  # noqa: E501
        :type: str
        """

        self._communication_method = communication_method

    @property
    def is_active(self):
        """Gets the is_active of this SubscriptionDefinition.  # noqa: E501

        Whether the definition is active or archived.  # noqa: E501

        :return: The is_active of this SubscriptionDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this SubscriptionDefinition.

        Whether the definition is active or archived.  # noqa: E501

        :param is_active: The is_active of this SubscriptionDefinition.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_active is None:  # noqa: E501
            raise ValueError("Invalid value for `is_active`, must not be `None`")  # noqa: E501

        self._is_active = is_active

    @property
    def is_default(self):
        """Gets the is_default of this SubscriptionDefinition.  # noqa: E501

        A subscription definition created by HubSpot.  # noqa: E501

        :return: The is_default of this SubscriptionDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this SubscriptionDefinition.

        A subscription definition created by HubSpot.  # noqa: E501

        :param is_default: The is_default of this SubscriptionDefinition.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_default is None:  # noqa: E501
            raise ValueError("Invalid value for `is_default`, must not be `None`")  # noqa: E501

        self._is_default = is_default

    @property
    def is_internal(self):
        """Gets the is_internal of this SubscriptionDefinition.  # noqa: E501

        A default description that is used by some HubSpot tools and cannot be edited.  # noqa: E501

        :return: The is_internal of this SubscriptionDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_internal

    @is_internal.setter
    def is_internal(self, is_internal):
        """Sets the is_internal of this SubscriptionDefinition.

        A default description that is used by some HubSpot tools and cannot be edited.  # noqa: E501

        :param is_internal: The is_internal of this SubscriptionDefinition.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_internal is None:  # noqa: E501
            raise ValueError("Invalid value for `is_internal`, must not be `None`")  # noqa: E501

        self._is_internal = is_internal

    @property
    def created_at(self):
        """Gets the created_at of this SubscriptionDefinition.  # noqa: E501

        Time at which the definition was created.  # noqa: E501

        :return: The created_at of this SubscriptionDefinition.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SubscriptionDefinition.

        Time at which the definition was created.  # noqa: E501

        :param created_at: The created_at of this SubscriptionDefinition.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SubscriptionDefinition.  # noqa: E501

        Time at which the definition was last updated.  # noqa: E501

        :return: The updated_at of this SubscriptionDefinition.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SubscriptionDefinition.

        Time at which the definition was last updated.  # noqa: E501

        :param updated_at: The updated_at of this SubscriptionDefinition.  # noqa: E501
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
        if not isinstance(other, SubscriptionDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionDefinition):
            return True

        return self.to_dict() != other.to_dict()
