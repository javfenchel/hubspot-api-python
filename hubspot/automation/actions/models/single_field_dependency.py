# coding: utf-8

"""
    Custom Workflow Actions

    Create custom workflow actions  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.automation.actions.configuration import Configuration


class SingleFieldDependency(object):
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
        "dependency_type": "str",
        "dependent_field_names": "list[str]",
        "controlling_field_name": "str",
    }

    attribute_map = {
        "dependency_type": "dependencyType",
        "dependent_field_names": "dependentFieldNames",
        "controlling_field_name": "controllingFieldName",
    }

    def __init__(
        self,
        dependency_type="SINGLE_FIELD",
        dependent_field_names=None,
        controlling_field_name=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """SingleFieldDependency - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dependency_type = None
        self._dependent_field_names = None
        self._controlling_field_name = None
        self.discriminator = None

        self.dependency_type = dependency_type
        self.dependent_field_names = dependent_field_names
        self.controlling_field_name = controlling_field_name

    @property
    def dependency_type(self):
        """Gets the dependency_type of this SingleFieldDependency.  # noqa: E501


        :return: The dependency_type of this SingleFieldDependency.  # noqa: E501
        :rtype: str
        """
        return self._dependency_type

    @dependency_type.setter
    def dependency_type(self, dependency_type):
        """Sets the dependency_type of this SingleFieldDependency.


        :param dependency_type: The dependency_type of this SingleFieldDependency.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and dependency_type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `dependency_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["SINGLE_FIELD"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and dependency_type not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `dependency_type` ({0}), must be one of {1}".format(  # noqa: E501
                    dependency_type, allowed_values
                )
            )

        self._dependency_type = dependency_type

    @property
    def dependent_field_names(self):
        """Gets the dependent_field_names of this SingleFieldDependency.  # noqa: E501


        :return: The dependent_field_names of this SingleFieldDependency.  # noqa: E501
        :rtype: list[str]
        """
        return self._dependent_field_names

    @dependent_field_names.setter
    def dependent_field_names(self, dependent_field_names):
        """Sets the dependent_field_names of this SingleFieldDependency.


        :param dependent_field_names: The dependent_field_names of this SingleFieldDependency.  # noqa: E501
        :type: list[str]
        """
        if (
            self.local_vars_configuration.client_side_validation
            and dependent_field_names is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `dependent_field_names`, must not be `None`"
            )  # noqa: E501

        self._dependent_field_names = dependent_field_names

    @property
    def controlling_field_name(self):
        """Gets the controlling_field_name of this SingleFieldDependency.  # noqa: E501


        :return: The controlling_field_name of this SingleFieldDependency.  # noqa: E501
        :rtype: str
        """
        return self._controlling_field_name

    @controlling_field_name.setter
    def controlling_field_name(self, controlling_field_name):
        """Sets the controlling_field_name of this SingleFieldDependency.


        :param controlling_field_name: The controlling_field_name of this SingleFieldDependency.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and controlling_field_name is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `controlling_field_name`, must not be `None`"
            )  # noqa: E501

        self._controlling_field_name = controlling_field_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SingleFieldDependency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SingleFieldDependency):
            return True

        return self.to_dict() != other.to_dict()
