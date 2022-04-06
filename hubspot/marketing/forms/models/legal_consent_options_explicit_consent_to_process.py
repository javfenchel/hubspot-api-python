# coding: utf-8

"""
    FormsExternalService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.marketing.forms.configuration import Configuration


class LegalConsentOptionsExplicitConsentToProcess(object):
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
        "type": "str",
        "communication_consent_text": "str",
        "communications_checkboxes": "list[LegalConsentCheckbox]",
        "consent_to_process_text": "str",
        "consent_to_process_checkbox_label": "str",
        "consent_to_process_footer_text": "str",
        "privacy_text": "str",
    }

    attribute_map = {
        "type": "type",
        "communication_consent_text": "communicationConsentText",
        "communications_checkboxes": "communicationsCheckboxes",
        "consent_to_process_text": "consentToProcessText",
        "consent_to_process_checkbox_label": "consentToProcessCheckboxLabel",
        "consent_to_process_footer_text": "consentToProcessFooterText",
        "privacy_text": "privacyText",
    }

    def __init__(
        self,
        type="explicit_consent_to_process",
        communication_consent_text=None,
        communications_checkboxes=None,
        consent_to_process_text=None,
        consent_to_process_checkbox_label=None,
        consent_to_process_footer_text=None,
        privacy_text=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """LegalConsentOptionsExplicitConsentToProcess - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._communication_consent_text = None
        self._communications_checkboxes = None
        self._consent_to_process_text = None
        self._consent_to_process_checkbox_label = None
        self._consent_to_process_footer_text = None
        self._privacy_text = None
        self.discriminator = None

        self.type = type
        if communication_consent_text is not None:
            self.communication_consent_text = communication_consent_text
        self.communications_checkboxes = communications_checkboxes
        if consent_to_process_text is not None:
            self.consent_to_process_text = consent_to_process_text
        if consent_to_process_checkbox_label is not None:
            self.consent_to_process_checkbox_label = consent_to_process_checkbox_label
        if consent_to_process_footer_text is not None:
            self.consent_to_process_footer_text = consent_to_process_footer_text
        self.privacy_text = privacy_text

    @property
    def type(self):
        """Gets the type of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501


        :return: The type of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LegalConsentOptionsExplicitConsentToProcess.


        :param type: The type of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["explicit_consent_to_process"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `type` ({0}), must be one of {1}".format(type, allowed_values))  # noqa: E501

        self._type = type

    @property
    def communication_consent_text(self):
        """Gets the communication_consent_text of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501


        :return: The communication_consent_text of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501
        :rtype: str
        """
        return self._communication_consent_text

    @communication_consent_text.setter
    def communication_consent_text(self, communication_consent_text):
        """Sets the communication_consent_text of this LegalConsentOptionsExplicitConsentToProcess.


        :param communication_consent_text: The communication_consent_text of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501
        :type: str
        """

        self._communication_consent_text = communication_consent_text

    @property
    def communications_checkboxes(self):
        """Gets the communications_checkboxes of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501


        :return: The communications_checkboxes of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501
        :rtype: list[LegalConsentCheckbox]
        """
        return self._communications_checkboxes

    @communications_checkboxes.setter
    def communications_checkboxes(self, communications_checkboxes):
        """Sets the communications_checkboxes of this LegalConsentOptionsExplicitConsentToProcess.


        :param communications_checkboxes: The communications_checkboxes of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501
        :type: list[LegalConsentCheckbox]
        """
        if self.local_vars_configuration.client_side_validation and communications_checkboxes is None:  # noqa: E501
            raise ValueError("Invalid value for `communications_checkboxes`, must not be `None`")  # noqa: E501

        self._communications_checkboxes = communications_checkboxes

    @property
    def consent_to_process_text(self):
        """Gets the consent_to_process_text of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501


        :return: The consent_to_process_text of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501
        :rtype: str
        """
        return self._consent_to_process_text

    @consent_to_process_text.setter
    def consent_to_process_text(self, consent_to_process_text):
        """Sets the consent_to_process_text of this LegalConsentOptionsExplicitConsentToProcess.


        :param consent_to_process_text: The consent_to_process_text of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501
        :type: str
        """

        self._consent_to_process_text = consent_to_process_text

    @property
    def consent_to_process_checkbox_label(self):
        """Gets the consent_to_process_checkbox_label of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501


        :return: The consent_to_process_checkbox_label of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501
        :rtype: str
        """
        return self._consent_to_process_checkbox_label

    @consent_to_process_checkbox_label.setter
    def consent_to_process_checkbox_label(self, consent_to_process_checkbox_label):
        """Sets the consent_to_process_checkbox_label of this LegalConsentOptionsExplicitConsentToProcess.


        :param consent_to_process_checkbox_label: The consent_to_process_checkbox_label of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501
        :type: str
        """

        self._consent_to_process_checkbox_label = consent_to_process_checkbox_label

    @property
    def consent_to_process_footer_text(self):
        """Gets the consent_to_process_footer_text of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501


        :return: The consent_to_process_footer_text of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501
        :rtype: str
        """
        return self._consent_to_process_footer_text

    @consent_to_process_footer_text.setter
    def consent_to_process_footer_text(self, consent_to_process_footer_text):
        """Sets the consent_to_process_footer_text of this LegalConsentOptionsExplicitConsentToProcess.


        :param consent_to_process_footer_text: The consent_to_process_footer_text of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501
        :type: str
        """

        self._consent_to_process_footer_text = consent_to_process_footer_text

    @property
    def privacy_text(self):
        """Gets the privacy_text of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501


        :return: The privacy_text of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501
        :rtype: str
        """
        return self._privacy_text

    @privacy_text.setter
    def privacy_text(self, privacy_text):
        """Sets the privacy_text of this LegalConsentOptionsExplicitConsentToProcess.


        :param privacy_text: The privacy_text of this LegalConsentOptionsExplicitConsentToProcess.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and privacy_text is None:  # noqa: E501
            raise ValueError("Invalid value for `privacy_text`, must not be `None`")  # noqa: E501

        self._privacy_text = privacy_text

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
        if not isinstance(other, LegalConsentOptionsExplicitConsentToProcess):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LegalConsentOptionsExplicitConsentToProcess):
            return True

        return self.to_dict() != other.to_dict()
