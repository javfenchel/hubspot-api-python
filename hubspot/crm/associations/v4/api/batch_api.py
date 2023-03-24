# coding: utf-8

"""
    CrmPublicAssociationsServiceV4

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.associations.v4.api_client import ApiClient
from hubspot.crm.associations.v4.exceptions import ApiTypeError, ApiValueError


class BatchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, from_object_type, to_object_type, batch_input_public_association_multi_archive, **kwargs):  # noqa: E501
        """Delete  # noqa: E501

        Batch delete associations for objects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive(from_object_type, to_object_type, batch_input_public_association_multi_archive, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param BatchInputPublicAssociationMultiArchive batch_input_public_association_multi_archive: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.archive_with_http_info(from_object_type, to_object_type, batch_input_public_association_multi_archive, **kwargs)  # noqa: E501

    def archive_with_http_info(self, from_object_type, to_object_type, batch_input_public_association_multi_archive, **kwargs):  # noqa: E501
        """Delete  # noqa: E501

        Batch delete associations for objects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_with_http_info(from_object_type, to_object_type, batch_input_public_association_multi_archive, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param BatchInputPublicAssociationMultiArchive batch_input_public_association_multi_archive: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "from_object_type",
            "to_object_type",
            "batch_input_public_association_multi_archive",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method archive" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'from_object_type' is set
        if self.api_client.client_side_validation and ("from_object_type" not in local_var_params or local_var_params["from_object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `from_object_type` when calling `archive`")  # noqa: E501
        # verify the required parameter 'to_object_type' is set
        if self.api_client.client_side_validation and ("to_object_type" not in local_var_params or local_var_params["to_object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_type` when calling `archive`")  # noqa: E501
        # verify the required parameter 'batch_input_public_association_multi_archive' is set
        if self.api_client.client_side_validation and (
            "batch_input_public_association_multi_archive" not in local_var_params or local_var_params["batch_input_public_association_multi_archive"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_input_public_association_multi_archive` when calling `archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "from_object_type" in local_var_params:
            path_params["fromObjectType"] = local_var_params["from_object_type"]  # noqa: E501
        if "to_object_type" in local_var_params:
            path_params["toObjectType"] = local_var_params["to_object_type"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_public_association_multi_archive" in local_var_params:
            body_params = local_var_params["batch_input_public_association_multi_archive"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v4/associations/{fromObjectType}/{toObjectType}/batch/archive",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def archive_labels(self, from_object_type, to_object_type, batch_input_public_association_multi_post, **kwargs):  # noqa: E501
        """Delete Specific Labels  # noqa: E501

        Batch delete specific association labels for objects. Deleting an unlabeled association will also delete all labeled associations between those two objects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_labels(from_object_type, to_object_type, batch_input_public_association_multi_post, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param BatchInputPublicAssociationMultiPost batch_input_public_association_multi_post: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.archive_labels_with_http_info(from_object_type, to_object_type, batch_input_public_association_multi_post, **kwargs)  # noqa: E501

    def archive_labels_with_http_info(self, from_object_type, to_object_type, batch_input_public_association_multi_post, **kwargs):  # noqa: E501
        """Delete Specific Labels  # noqa: E501

        Batch delete specific association labels for objects. Deleting an unlabeled association will also delete all labeled associations between those two objects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_labels_with_http_info(from_object_type, to_object_type, batch_input_public_association_multi_post, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param BatchInputPublicAssociationMultiPost batch_input_public_association_multi_post: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "from_object_type",
            "to_object_type",
            "batch_input_public_association_multi_post",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method archive_labels" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'from_object_type' is set
        if self.api_client.client_side_validation and ("from_object_type" not in local_var_params or local_var_params["from_object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `from_object_type` when calling `archive_labels`")  # noqa: E501
        # verify the required parameter 'to_object_type' is set
        if self.api_client.client_side_validation and ("to_object_type" not in local_var_params or local_var_params["to_object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_type` when calling `archive_labels`")  # noqa: E501
        # verify the required parameter 'batch_input_public_association_multi_post' is set
        if self.api_client.client_side_validation and (
            "batch_input_public_association_multi_post" not in local_var_params or local_var_params["batch_input_public_association_multi_post"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_input_public_association_multi_post` when calling `archive_labels`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "from_object_type" in local_var_params:
            path_params["fromObjectType"] = local_var_params["from_object_type"]  # noqa: E501
        if "to_object_type" in local_var_params:
            path_params["toObjectType"] = local_var_params["to_object_type"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_public_association_multi_post" in local_var_params:
            body_params = local_var_params["batch_input_public_association_multi_post"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v4/associations/{fromObjectType}/{toObjectType}/batch/labels/archive",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def create(self, from_object_type, to_object_type, batch_input_public_association_multi_post, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        Batch create associations for objects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(from_object_type, to_object_type, batch_input_public_association_multi_post, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param BatchInputPublicAssociationMultiPost batch_input_public_association_multi_post: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: BatchResponseLabelsBetweenObjectPair
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.create_with_http_info(from_object_type, to_object_type, batch_input_public_association_multi_post, **kwargs)  # noqa: E501

    def create_with_http_info(self, from_object_type, to_object_type, batch_input_public_association_multi_post, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        Batch create associations for objects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(from_object_type, to_object_type, batch_input_public_association_multi_post, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param BatchInputPublicAssociationMultiPost batch_input_public_association_multi_post: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(BatchResponseLabelsBetweenObjectPair, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "from_object_type",
            "to_object_type",
            "batch_input_public_association_multi_post",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method create" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'from_object_type' is set
        if self.api_client.client_side_validation and ("from_object_type" not in local_var_params or local_var_params["from_object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `from_object_type` when calling `create`")  # noqa: E501
        # verify the required parameter 'to_object_type' is set
        if self.api_client.client_side_validation and ("to_object_type" not in local_var_params or local_var_params["to_object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_type` when calling `create`")  # noqa: E501
        # verify the required parameter 'batch_input_public_association_multi_post' is set
        if self.api_client.client_side_validation and (
            "batch_input_public_association_multi_post" not in local_var_params or local_var_params["batch_input_public_association_multi_post"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_input_public_association_multi_post` when calling `create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "from_object_type" in local_var_params:
            path_params["fromObjectType"] = local_var_params["from_object_type"]  # noqa: E501
        if "to_object_type" in local_var_params:
            path_params["toObjectType"] = local_var_params["to_object_type"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_public_association_multi_post" in local_var_params:
            body_params = local_var_params["batch_input_public_association_multi_post"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v4/associations/{fromObjectType}/{toObjectType}/batch/create",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BatchResponseLabelsBetweenObjectPair",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def create_default(self, from_object_type, to_object_type, batch_input_public_default_association_multi_post, **kwargs):  # noqa: E501
        """Create Default Associations  # noqa: E501

        Create the default (most generic) association type between two object types  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_default(from_object_type, to_object_type, batch_input_public_default_association_multi_post, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param BatchInputPublicDefaultAssociationMultiPost batch_input_public_default_association_multi_post: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: BatchResponsePublicDefaultAssociation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.create_default_with_http_info(from_object_type, to_object_type, batch_input_public_default_association_multi_post, **kwargs)  # noqa: E501

    def create_default_with_http_info(self, from_object_type, to_object_type, batch_input_public_default_association_multi_post, **kwargs):  # noqa: E501
        """Create Default Associations  # noqa: E501

        Create the default (most generic) association type between two object types  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_default_with_http_info(from_object_type, to_object_type, batch_input_public_default_association_multi_post, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param BatchInputPublicDefaultAssociationMultiPost batch_input_public_default_association_multi_post: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(BatchResponsePublicDefaultAssociation, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "from_object_type",
            "to_object_type",
            "batch_input_public_default_association_multi_post",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method create_default" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'from_object_type' is set
        if self.api_client.client_side_validation and ("from_object_type" not in local_var_params or local_var_params["from_object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `from_object_type` when calling `create_default`")  # noqa: E501
        # verify the required parameter 'to_object_type' is set
        if self.api_client.client_side_validation and ("to_object_type" not in local_var_params or local_var_params["to_object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_type` when calling `create_default`")  # noqa: E501
        # verify the required parameter 'batch_input_public_default_association_multi_post' is set
        if self.api_client.client_side_validation and (
            "batch_input_public_default_association_multi_post" not in local_var_params or local_var_params["batch_input_public_default_association_multi_post"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_input_public_default_association_multi_post` when calling `create_default`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "from_object_type" in local_var_params:
            path_params["fromObjectType"] = local_var_params["from_object_type"]  # noqa: E501
        if "to_object_type" in local_var_params:
            path_params["toObjectType"] = local_var_params["to_object_type"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_public_default_association_multi_post" in local_var_params:
            body_params = local_var_params["batch_input_public_default_association_multi_post"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v4/associations/{fromObjectType}/{toObjectType}/batch/associate/default",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BatchResponsePublicDefaultAssociation",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_page(self, from_object_type, to_object_type, batch_input_public_fetch_associations_batch_request, **kwargs):  # noqa: E501
        """Read  # noqa: E501

        Batch read associations for objects to specific object type. The 'after' field in a returned paging object  can be added alongside the 'id' to retrieve the next page of associations from that objectId. The 'link' field is deprecated and should be ignored.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page(from_object_type, to_object_type, batch_input_public_fetch_associations_batch_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param BatchInputPublicFetchAssociationsBatchRequest batch_input_public_fetch_associations_batch_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: BatchResponsePublicAssociationMultiWithLabel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_page_with_http_info(from_object_type, to_object_type, batch_input_public_fetch_associations_batch_request, **kwargs)  # noqa: E501

    def get_page_with_http_info(self, from_object_type, to_object_type, batch_input_public_fetch_associations_batch_request, **kwargs):  # noqa: E501
        """Read  # noqa: E501

        Batch read associations for objects to specific object type. The 'after' field in a returned paging object  can be added alongside the 'id' to retrieve the next page of associations from that objectId. The 'link' field is deprecated and should be ignored.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page_with_http_info(from_object_type, to_object_type, batch_input_public_fetch_associations_batch_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param BatchInputPublicFetchAssociationsBatchRequest batch_input_public_fetch_associations_batch_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(BatchResponsePublicAssociationMultiWithLabel, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "from_object_type",
            "to_object_type",
            "batch_input_public_fetch_associations_batch_request",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_page" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'from_object_type' is set
        if self.api_client.client_side_validation and ("from_object_type" not in local_var_params or local_var_params["from_object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `from_object_type` when calling `get_page`")  # noqa: E501
        # verify the required parameter 'to_object_type' is set
        if self.api_client.client_side_validation and ("to_object_type" not in local_var_params or local_var_params["to_object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_type` when calling `get_page`")  # noqa: E501
        # verify the required parameter 'batch_input_public_fetch_associations_batch_request' is set
        if self.api_client.client_side_validation and (
            "batch_input_public_fetch_associations_batch_request" not in local_var_params or local_var_params["batch_input_public_fetch_associations_batch_request"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_input_public_fetch_associations_batch_request` when calling `get_page`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "from_object_type" in local_var_params:
            path_params["fromObjectType"] = local_var_params["from_object_type"]  # noqa: E501
        if "to_object_type" in local_var_params:
            path_params["toObjectType"] = local_var_params["to_object_type"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_public_fetch_associations_batch_request" in local_var_params:
            body_params = local_var_params["batch_input_public_fetch_associations_batch_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v4/associations/{fromObjectType}/{toObjectType}/batch/read",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BatchResponsePublicAssociationMultiWithLabel",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
