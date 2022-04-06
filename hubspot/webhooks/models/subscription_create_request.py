# coding: utf-8

"""
    Webhooks API

    Provides a way for apps to subscribe to certain change events in HubSpot. Once configured, apps will receive event payloads containing details about the changes at a specified target URL. There can only be one target URL for receiving event notifications per app.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.webhooks.configuration import Configuration


class SubscriptionCreateRequest(object):
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
    openapi_types = {"event_type": "str", "property_name": "str", "active": "bool"}

    attribute_map = {"event_type": "eventType", "property_name": "propertyName", "active": "active"}

    def __init__(self, event_type=None, property_name=None, active=None, local_vars_configuration=None):  # noqa: E501
        """SubscriptionCreateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._event_type = None
        self._property_name = None
        self._active = None
        self.discriminator = None

        self.event_type = event_type
        if property_name is not None:
            self.property_name = property_name
        if active is not None:
            self.active = active

    @property
    def event_type(self):
        """Gets the event_type of this SubscriptionCreateRequest.  # noqa: E501

        Type of event to listen for. Can be one of `create`, `delete`, `deletedForPrivacy`, or `propertyChange`.  # noqa: E501

        :return: The event_type of this SubscriptionCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this SubscriptionCreateRequest.

        Type of event to listen for. Can be one of `create`, `delete`, `deletedForPrivacy`, or `propertyChange`.  # noqa: E501

        :param event_type: The event_type of this SubscriptionCreateRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501
        allowed_values = [
            "contact.propertyChange",
            "company.propertyChange",
            "deal.propertyChange",
            "ticket.propertyChange",
            "product.propertyChange",
            "line_item.propertyChange",
            "contact.creation",
            "contact.deletion",
            "contact.privacyDeletion",
            "company.creation",
            "company.deletion",
            "deal.creation",
            "deal.deletion",
            "ticket.creation",
            "ticket.deletion",
            "product.creation",
            "product.deletion",
            "line_item.creation",
            "line_item.deletion",
            "conversation.creation",
            "conversation.deletion",
            "conversation.newMessage",
            "conversation.privacyDeletion",
            "conversation.propertyChange",
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and event_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `event_type` ({0}), must be one of {1}".format(event_type, allowed_values))  # noqa: E501

        self._event_type = event_type

    @property
    def property_name(self):
        """Gets the property_name of this SubscriptionCreateRequest.  # noqa: E501

        The internal name of the property to monitor for changes. Only applies when `eventType` is `propertyChange`.  # noqa: E501

        :return: The property_name of this SubscriptionCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this SubscriptionCreateRequest.

        The internal name of the property to monitor for changes. Only applies when `eventType` is `propertyChange`.  # noqa: E501

        :param property_name: The property_name of this SubscriptionCreateRequest.  # noqa: E501
        :type: str
        """

        self._property_name = property_name

    @property
    def active(self):
        """Gets the active of this SubscriptionCreateRequest.  # noqa: E501

        Determines if the subscription is active or paused. Defaults to false.  # noqa: E501

        :return: The active of this SubscriptionCreateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this SubscriptionCreateRequest.

        Determines if the subscription is active or paused. Defaults to false.  # noqa: E501

        :param active: The active of this SubscriptionCreateRequest.  # noqa: E501
        :type: bool
        """

        self._active = active

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
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
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
        if not isinstance(other, SubscriptionCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
