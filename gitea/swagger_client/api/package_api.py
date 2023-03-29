# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PackageApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_package(self, owner, type, name, version, **kwargs):  # noqa: E501
        """Delete a package  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_package(owner, type, name, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: owner of the package (required)
        :param str type: type of the package (required)
        :param str name: name of the package (required)
        :param str version: version of the package (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_package_with_http_info(
                owner, type, name, version, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_package_with_http_info(
                owner, type, name, version, **kwargs
            )  # noqa: E501
            return data

    def delete_package_with_http_info(
        self, owner, type, name, version, **kwargs
    ):  # noqa: E501
        """Delete a package  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_package_with_http_info(owner, type, name, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: owner of the package (required)
        :param str type: type of the package (required)
        :param str name: name of the package (required)
        :param str version: version of the package (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["owner", "type", "name", "version"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_package" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and (
            "owner" not in params or params["owner"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `owner` when calling `delete_package`"
            )  # noqa: E501
        # verify the required parameter 'type' is set
        if self.api_client.client_side_validation and (
            "type" not in params or params["type"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `type` when calling `delete_package`"
            )  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and (
            "name" not in params or params["name"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `name` when calling `delete_package`"
            )  # noqa: E501
        # verify the required parameter 'version' is set
        if self.api_client.client_side_validation and (
            "version" not in params or params["version"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `version` when calling `delete_package`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "owner" in params:
            path_params["owner"] = params["owner"]  # noqa: E501
        if "type" in params:
            path_params["type"] = params["type"]  # noqa: E501
        if "name" in params:
            path_params["name"] = params["name"]  # noqa: E501
        if "version" in params:
            path_params["version"] = params["version"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "text/html"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json", "text/plain"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = [
            "AccessToken",
            "AuthorizationHeaderToken",
            "BasicAuth",
            "SudoHeader",
            "SudoParam",
            "TOTPHeader",
            "Token",
        ]  # noqa: E501

        return self.api_client.call_api(
            "/packages/{owner}/{type}/{name}/{version}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_package(self, owner, type, name, version, **kwargs):  # noqa: E501
        """Gets a package  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_package(owner, type, name, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: owner of the package (required)
        :param str type: type of the package (required)
        :param str name: name of the package (required)
        :param str version: version of the package (required)
        :return: Package
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_package_with_http_info(
                owner, type, name, version, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_package_with_http_info(
                owner, type, name, version, **kwargs
            )  # noqa: E501
            return data

    def get_package_with_http_info(
        self, owner, type, name, version, **kwargs
    ):  # noqa: E501
        """Gets a package  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_package_with_http_info(owner, type, name, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: owner of the package (required)
        :param str type: type of the package (required)
        :param str name: name of the package (required)
        :param str version: version of the package (required)
        :return: Package
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["owner", "type", "name", "version"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_package" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and (
            "owner" not in params or params["owner"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `owner` when calling `get_package`"
            )  # noqa: E501
        # verify the required parameter 'type' is set
        if self.api_client.client_side_validation and (
            "type" not in params or params["type"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `type` when calling `get_package`"
            )  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and (
            "name" not in params or params["name"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `name` when calling `get_package`"
            )  # noqa: E501
        # verify the required parameter 'version' is set
        if self.api_client.client_side_validation and (
            "version" not in params or params["version"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `version` when calling `get_package`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "owner" in params:
            path_params["owner"] = params["owner"]  # noqa: E501
        if "type" in params:
            path_params["type"] = params["type"]  # noqa: E501
        if "name" in params:
            path_params["name"] = params["name"]  # noqa: E501
        if "version" in params:
            path_params["version"] = params["version"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json", "text/plain"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = [
            "AccessToken",
            "AuthorizationHeaderToken",
            "BasicAuth",
            "SudoHeader",
            "SudoParam",
            "TOTPHeader",
            "Token",
        ]  # noqa: E501

        return self.api_client.call_api(
            "/packages/{owner}/{type}/{name}/{version}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Package",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def list_package_files(self, owner, type, name, version, **kwargs):  # noqa: E501
        """Gets all files of a package  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_package_files(owner, type, name, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: owner of the package (required)
        :param str type: type of the package (required)
        :param str name: name of the package (required)
        :param str version: version of the package (required)
        :return: list[PackageFile]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_package_files_with_http_info(
                owner, type, name, version, **kwargs
            )  # noqa: E501
        else:
            (data) = self.list_package_files_with_http_info(
                owner, type, name, version, **kwargs
            )  # noqa: E501
            return data

    def list_package_files_with_http_info(
        self, owner, type, name, version, **kwargs
    ):  # noqa: E501
        """Gets all files of a package  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_package_files_with_http_info(owner, type, name, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: owner of the package (required)
        :param str type: type of the package (required)
        :param str name: name of the package (required)
        :param str version: version of the package (required)
        :return: list[PackageFile]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["owner", "type", "name", "version"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_package_files" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and (
            "owner" not in params or params["owner"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `owner` when calling `list_package_files`"
            )  # noqa: E501
        # verify the required parameter 'type' is set
        if self.api_client.client_side_validation and (
            "type" not in params or params["type"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `type` when calling `list_package_files`"
            )  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and (
            "name" not in params or params["name"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `name` when calling `list_package_files`"
            )  # noqa: E501
        # verify the required parameter 'version' is set
        if self.api_client.client_side_validation and (
            "version" not in params or params["version"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `version` when calling `list_package_files`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "owner" in params:
            path_params["owner"] = params["owner"]  # noqa: E501
        if "type" in params:
            path_params["type"] = params["type"]  # noqa: E501
        if "name" in params:
            path_params["name"] = params["name"]  # noqa: E501
        if "version" in params:
            path_params["version"] = params["version"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json", "text/plain"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = [
            "AccessToken",
            "AuthorizationHeaderToken",
            "BasicAuth",
            "SudoHeader",
            "SudoParam",
            "TOTPHeader",
            "Token",
        ]  # noqa: E501

        return self.api_client.call_api(
            "/packages/{owner}/{type}/{name}/{version}/files",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[PackageFile]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def list_packages(self, owner, **kwargs):  # noqa: E501
        """Gets all packages of an owner  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_packages(owner, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: owner of the packages (required)
        :param int page: page number of results to return (1-based)
        :param int limit: page size of results
        :param str type: package type filter
        :param str q: name filter
        :return: list[Package]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_packages_with_http_info(owner, **kwargs)  # noqa: E501
        else:
            (data) = self.list_packages_with_http_info(owner, **kwargs)  # noqa: E501
            return data

    def list_packages_with_http_info(self, owner, **kwargs):  # noqa: E501
        """Gets all packages of an owner  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_packages_with_http_info(owner, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: owner of the packages (required)
        :param int page: page number of results to return (1-based)
        :param int limit: page size of results
        :param str type: package type filter
        :param str q: name filter
        :return: list[Package]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["owner", "page", "limit", "type", "q"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_packages" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and (
            "owner" not in params or params["owner"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `owner` when calling `list_packages`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "owner" in params:
            path_params["owner"] = params["owner"]  # noqa: E501

        query_params = []
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501
        if "type" in params:
            query_params.append(("type", params["type"]))  # noqa: E501
        if "q" in params:
            query_params.append(("q", params["q"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json", "text/plain"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = [
            "AccessToken",
            "AuthorizationHeaderToken",
            "BasicAuth",
            "SudoHeader",
            "SudoParam",
            "TOTPHeader",
            "Token",
        ]  # noqa: E501

        return self.api_client.call_api(
            "/packages/{owner}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[Package]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
