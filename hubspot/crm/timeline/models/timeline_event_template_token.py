# coding: utf-8

"""
    CRM Timeline

    This feature allows an app to create and configure custom events that can show up in the timelines of certain CRM objects like contacts, companies, tickets, or deals. You'll find multiple use cases for this API in the sections below.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.crm.timeline.configuration import Configuration


class TimelineEventTemplateToken(object):
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
        "created_at": "datetime",
        "options": "list[TimelineEventTemplateTokenOption]",
        "name": "str",
        "label": "str",
        "object_property_name": "str",
        "type": "str",
        "updated_at": "datetime",
    }

    attribute_map = {"created_at": "createdAt", "options": "options", "name": "name", "label": "label", "object_property_name": "objectPropertyName", "type": "type", "updated_at": "updatedAt"}

    def __init__(self, created_at=None, options=None, name=None, label=None, object_property_name=None, type=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """TimelineEventTemplateToken - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._options = None
        self._name = None
        self._label = None
        self._object_property_name = None
        self._type = None
        self._updated_at = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if options is not None:
            self.options = options
        self.name = name
        self.label = label
        if object_property_name is not None:
            self.object_property_name = object_property_name
        self.type = type
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this TimelineEventTemplateToken.  # noqa: E501

        The date and time that the Event Template Token was created, as an ISO 8601 timestamp. Will be null if the template was created before Feb 18th, 2020.  # noqa: E501

        :return: The created_at of this TimelineEventTemplateToken.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TimelineEventTemplateToken.

        The date and time that the Event Template Token was created, as an ISO 8601 timestamp. Will be null if the template was created before Feb 18th, 2020.  # noqa: E501

        :param created_at: The created_at of this TimelineEventTemplateToken.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def options(self):
        """Gets the options of this TimelineEventTemplateToken.  # noqa: E501

        If type is `enumeration`, we should have a list of options to choose from.  # noqa: E501

        :return: The options of this TimelineEventTemplateToken.  # noqa: E501
        :rtype: list[TimelineEventTemplateTokenOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this TimelineEventTemplateToken.

        If type is `enumeration`, we should have a list of options to choose from.  # noqa: E501

        :param options: The options of this TimelineEventTemplateToken.  # noqa: E501
        :type options: list[TimelineEventTemplateTokenOption]
        """

        self._options = options

    @property
    def name(self):
        """Gets the name of this TimelineEventTemplateToken.  # noqa: E501

        The name of the token referenced in the templates. This must be unique for the specific template. It may only contain alphanumeric characters, periods, dashes, or underscores (. - _).  # noqa: E501

        :return: The name of this TimelineEventTemplateToken.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TimelineEventTemplateToken.

        The name of the token referenced in the templates. This must be unique for the specific template. It may only contain alphanumeric characters, periods, dashes, or underscores (. - _).  # noqa: E501

        :param name: The name of this TimelineEventTemplateToken.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def label(self):
        """Gets the label of this TimelineEventTemplateToken.  # noqa: E501

        Used for list segmentation and reporting.  # noqa: E501

        :return: The label of this TimelineEventTemplateToken.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this TimelineEventTemplateToken.

        Used for list segmentation and reporting.  # noqa: E501

        :param label: The label of this TimelineEventTemplateToken.  # noqa: E501
        :type label: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def object_property_name(self):
        """Gets the object_property_name of this TimelineEventTemplateToken.  # noqa: E501

        The name of the CRM object property. This will populate the CRM object property associated with the event. With enough of these, you can fully build CRM objects via the Timeline API.  # noqa: E501

        :return: The object_property_name of this TimelineEventTemplateToken.  # noqa: E501
        :rtype: str
        """
        return self._object_property_name

    @object_property_name.setter
    def object_property_name(self, object_property_name):
        """Sets the object_property_name of this TimelineEventTemplateToken.

        The name of the CRM object property. This will populate the CRM object property associated with the event. With enough of these, you can fully build CRM objects via the Timeline API.  # noqa: E501

        :param object_property_name: The object_property_name of this TimelineEventTemplateToken.  # noqa: E501
        :type object_property_name: str
        """

        self._object_property_name = object_property_name

    @property
    def type(self):
        """Gets the type of this TimelineEventTemplateToken.  # noqa: E501

        The data type of the token. You can currently choose from [string, number, date, enumeration].  # noqa: E501

        :return: The type of this TimelineEventTemplateToken.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TimelineEventTemplateToken.

        The data type of the token. You can currently choose from [string, number, date, enumeration].  # noqa: E501

        :param type: The type of this TimelineEventTemplateToken.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["date", "enumeration", "number", "string"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `type` ({0}), must be one of {1}".format(type, allowed_values))  # noqa: E501

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this TimelineEventTemplateToken.  # noqa: E501

        The date and time that the Event Template Token was last updated, as an ISO 8601 timestamp. Will be null if the template was created before Feb 18th, 2020.  # noqa: E501

        :return: The updated_at of this TimelineEventTemplateToken.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TimelineEventTemplateToken.

        The date and time that the Event Template Token was last updated, as an ISO 8601 timestamp. Will be null if the template was created before Feb 18th, 2020.  # noqa: E501

        :param updated_at: The updated_at of this TimelineEventTemplateToken.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], convert(item[1])), value.items()))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TimelineEventTemplateToken):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimelineEventTemplateToken):
            return True

        return self.to_dict() != other.to_dict()
