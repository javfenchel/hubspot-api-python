# coding: utf-8

"""
    Feedback Submissions

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.objects.feedback_submissions.api_client import ApiClient
from hubspot.crm.objects.feedback_submissions.exceptions import (
    ApiTypeError,
    ApiValueError,
)


class BatchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def post_crm_v3_objects_feedback_submissions_batch_archive(self, batch_input_simple_public_object_id, **kwargs):  # noqa: E501
        """Archive a batch of feedback submissions by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_crm_v3_objects_feedback_submissions_batch_archive(batch_input_simple_public_object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchInputSimplePublicObjectId batch_input_simple_public_object_id: (required)
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
        return self.post_crm_v3_objects_feedback_submissions_batch_archive_with_http_info(batch_input_simple_public_object_id, **kwargs)  # noqa: E501

    def post_crm_v3_objects_feedback_submissions_batch_archive_with_http_info(self, batch_input_simple_public_object_id, **kwargs):  # noqa: E501
        """Archive a batch of feedback submissions by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_crm_v3_objects_feedback_submissions_batch_archive_with_http_info(batch_input_simple_public_object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchInputSimplePublicObjectId batch_input_simple_public_object_id: (required)
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

        all_params = ["batch_input_simple_public_object_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method post_crm_v3_objects_feedback_submissions_batch_archive" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'batch_input_simple_public_object_id' is set
        if self.api_client.client_side_validation and (
            "batch_input_simple_public_object_id" not in local_var_params or local_var_params["batch_input_simple_public_object_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_input_simple_public_object_id` when calling `post_crm_v3_objects_feedback_submissions_batch_archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_simple_public_object_id" in local_var_params:
            body_params = local_var_params["batch_input_simple_public_object_id"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/objects/feedback submissions/batch/archive",
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

    def post_crm_v3_objects_feedback_submissions_batch_create(self, batch_input_simple_public_object_input_for_create, **kwargs):  # noqa: E501
        """Create a batch of feedback submissions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_crm_v3_objects_feedback_submissions_batch_create(batch_input_simple_public_object_input_for_create, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchInputSimplePublicObjectInputForCreate batch_input_simple_public_object_input_for_create: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: BatchResponseSimplePublicObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.post_crm_v3_objects_feedback_submissions_batch_create_with_http_info(batch_input_simple_public_object_input_for_create, **kwargs)  # noqa: E501

    def post_crm_v3_objects_feedback_submissions_batch_create_with_http_info(self, batch_input_simple_public_object_input_for_create, **kwargs):  # noqa: E501
        """Create a batch of feedback submissions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_crm_v3_objects_feedback_submissions_batch_create_with_http_info(batch_input_simple_public_object_input_for_create, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchInputSimplePublicObjectInputForCreate batch_input_simple_public_object_input_for_create: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(BatchResponseSimplePublicObject, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["batch_input_simple_public_object_input_for_create"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method post_crm_v3_objects_feedback_submissions_batch_create" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'batch_input_simple_public_object_input_for_create' is set
        if self.api_client.client_side_validation and (
            "batch_input_simple_public_object_input_for_create" not in local_var_params or local_var_params["batch_input_simple_public_object_input_for_create"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_input_simple_public_object_input_for_create` when calling `post_crm_v3_objects_feedback_submissions_batch_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_simple_public_object_input_for_create" in local_var_params:
            body_params = local_var_params["batch_input_simple_public_object_input_for_create"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/objects/feedback submissions/batch/create",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BatchResponseSimplePublicObject",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_crm_v3_objects_feedback_submissions_batch_read(self, batch_read_input_simple_public_object_id, **kwargs):  # noqa: E501
        """Read a batch of feedback submissions by internal ID, or unique property values  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_crm_v3_objects_feedback_submissions_batch_read(batch_read_input_simple_public_object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchReadInputSimplePublicObjectId batch_read_input_simple_public_object_id: (required)
        :param bool archived: Whether to return only results that have been archived.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: BatchResponseSimplePublicObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.post_crm_v3_objects_feedback_submissions_batch_read_with_http_info(batch_read_input_simple_public_object_id, **kwargs)  # noqa: E501

    def post_crm_v3_objects_feedback_submissions_batch_read_with_http_info(self, batch_read_input_simple_public_object_id, **kwargs):  # noqa: E501
        """Read a batch of feedback submissions by internal ID, or unique property values  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_crm_v3_objects_feedback_submissions_batch_read_with_http_info(batch_read_input_simple_public_object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchReadInputSimplePublicObjectId batch_read_input_simple_public_object_id: (required)
        :param bool archived: Whether to return only results that have been archived.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(BatchResponseSimplePublicObject, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "batch_read_input_simple_public_object_id",
            "archived",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method post_crm_v3_objects_feedback_submissions_batch_read" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'batch_read_input_simple_public_object_id' is set
        if self.api_client.client_side_validation and (
            "batch_read_input_simple_public_object_id" not in local_var_params or local_var_params["batch_read_input_simple_public_object_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_read_input_simple_public_object_id` when calling `post_crm_v3_objects_feedback_submissions_batch_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "archived" in local_var_params and local_var_params["archived"] is not None:  # noqa: E501
            query_params.append(("archived", local_var_params["archived"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_read_input_simple_public_object_id" in local_var_params:
            body_params = local_var_params["batch_read_input_simple_public_object_id"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/objects/feedback submissions/batch/read",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BatchResponseSimplePublicObject",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_crm_v3_objects_feedback_submissions_batch_update(self, batch_input_simple_public_object_batch_input, **kwargs):  # noqa: E501
        """Update a batch of feedback submissions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_crm_v3_objects_feedback_submissions_batch_update(batch_input_simple_public_object_batch_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchInputSimplePublicObjectBatchInput batch_input_simple_public_object_batch_input: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: BatchResponseSimplePublicObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.post_crm_v3_objects_feedback_submissions_batch_update_with_http_info(batch_input_simple_public_object_batch_input, **kwargs)  # noqa: E501

    def post_crm_v3_objects_feedback_submissions_batch_update_with_http_info(self, batch_input_simple_public_object_batch_input, **kwargs):  # noqa: E501
        """Update a batch of feedback submissions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_crm_v3_objects_feedback_submissions_batch_update_with_http_info(batch_input_simple_public_object_batch_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchInputSimplePublicObjectBatchInput batch_input_simple_public_object_batch_input: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(BatchResponseSimplePublicObject, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["batch_input_simple_public_object_batch_input"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method post_crm_v3_objects_feedback_submissions_batch_update" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'batch_input_simple_public_object_batch_input' is set
        if self.api_client.client_side_validation and (
            "batch_input_simple_public_object_batch_input" not in local_var_params or local_var_params["batch_input_simple_public_object_batch_input"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_input_simple_public_object_batch_input` when calling `post_crm_v3_objects_feedback_submissions_batch_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_simple_public_object_batch_input" in local_var_params:
            body_params = local_var_params["batch_input_simple_public_object_batch_input"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/objects/feedback submissions/batch/update",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BatchResponseSimplePublicObject",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
