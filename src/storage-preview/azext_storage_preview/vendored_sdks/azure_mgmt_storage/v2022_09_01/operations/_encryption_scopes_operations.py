# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_put_request(
    resource_group_name: str, account_name: str, encryption_scope_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-09-01"))  # type: Literal["2022-09-01"]
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/encryptionScopes/{encryptionScopeName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "accountName": _SERIALIZER.url("account_name", account_name, "str", max_length=24, min_length=3),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "encryptionScopeName": _SERIALIZER.url(
            "encryption_scope_name", encryption_scope_name, "str", max_length=63, min_length=3
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_patch_request(
    resource_group_name: str, account_name: str, encryption_scope_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-09-01"))  # type: Literal["2022-09-01"]
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/encryptionScopes/{encryptionScopeName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "accountName": _SERIALIZER.url("account_name", account_name, "str", max_length=24, min_length=3),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "encryptionScopeName": _SERIALIZER.url(
            "encryption_scope_name", encryption_scope_name, "str", max_length=63, min_length=3
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str, account_name: str, encryption_scope_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-09-01"))  # type: Literal["2022-09-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/encryptionScopes/{encryptionScopeName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "accountName": _SERIALIZER.url("account_name", account_name, "str", max_length=24, min_length=3),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "encryptionScopeName": _SERIALIZER.url(
            "encryption_scope_name", encryption_scope_name, "str", max_length=63, min_length=3
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_request(
    resource_group_name: str,
    account_name: str,
    subscription_id: str,
    *,
    maxpagesize: Optional[int] = None,
    filter: Optional[str] = None,
    include: Optional[Union[str, _models.ListEncryptionScopesInclude]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-09-01"))  # type: Literal["2022-09-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/encryptionScopes",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "accountName": _SERIALIZER.url("account_name", account_name, "str", max_length=24, min_length=3),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if maxpagesize is not None:
        _params["$maxpagesize"] = _SERIALIZER.query("maxpagesize", maxpagesize, "int", maximum=5000, minimum=1)
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if include is not None:
        _params["$include"] = _SERIALIZER.query("include", include, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class EncryptionScopesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.storage.v2022_09_01.StorageManagementClient`'s
        :attr:`encryption_scopes` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def put(
        self,
        resource_group_name: str,
        account_name: str,
        encryption_scope_name: str,
        encryption_scope: _models.EncryptionScope,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.EncryptionScope:
        """Synchronously creates or updates an encryption scope under the specified storage account. If an
        encryption scope is already created and a subsequent request is issued with different
        properties, the encryption scope properties will be updated per the specified request.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number. Required.
        :type encryption_scope_name: str
        :param encryption_scope: Encryption scope properties to be used for the create or update.
         Required.
        :type encryption_scope: ~azure.mgmt.storage.v2022_09_01.models.EncryptionScope
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2022_09_01.models.EncryptionScope
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def put(
        self,
        resource_group_name: str,
        account_name: str,
        encryption_scope_name: str,
        encryption_scope: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.EncryptionScope:
        """Synchronously creates or updates an encryption scope under the specified storage account. If an
        encryption scope is already created and a subsequent request is issued with different
        properties, the encryption scope properties will be updated per the specified request.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number. Required.
        :type encryption_scope_name: str
        :param encryption_scope: Encryption scope properties to be used for the create or update.
         Required.
        :type encryption_scope: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2022_09_01.models.EncryptionScope
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def put(
        self,
        resource_group_name: str,
        account_name: str,
        encryption_scope_name: str,
        encryption_scope: Union[_models.EncryptionScope, IO],
        **kwargs: Any
    ) -> _models.EncryptionScope:
        """Synchronously creates or updates an encryption scope under the specified storage account. If an
        encryption scope is already created and a subsequent request is issued with different
        properties, the encryption scope properties will be updated per the specified request.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number. Required.
        :type encryption_scope_name: str
        :param encryption_scope: Encryption scope properties to be used for the create or update. Is
         either a model type or a IO type. Required.
        :type encryption_scope: ~azure.mgmt.storage.v2022_09_01.models.EncryptionScope or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2022_09_01.models.EncryptionScope
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-09-01"))  # type: Literal["2022-09-01"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.EncryptionScope]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(encryption_scope, (IO, bytes)):
            _content = encryption_scope
        else:
            _json = self._serialize.body(encryption_scope, "EncryptionScope")

        request = build_put_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            encryption_scope_name=encryption_scope_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.put.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("EncryptionScope", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("EncryptionScope", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/encryptionScopes/{encryptionScopeName}"}  # type: ignore

    @overload
    def patch(
        self,
        resource_group_name: str,
        account_name: str,
        encryption_scope_name: str,
        encryption_scope: _models.EncryptionScope,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.EncryptionScope:
        """Update encryption scope properties as specified in the request body. Update fails if the
        specified encryption scope does not already exist.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number. Required.
        :type encryption_scope_name: str
        :param encryption_scope: Encryption scope properties to be used for the update. Required.
        :type encryption_scope: ~azure.mgmt.storage.v2022_09_01.models.EncryptionScope
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2022_09_01.models.EncryptionScope
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def patch(
        self,
        resource_group_name: str,
        account_name: str,
        encryption_scope_name: str,
        encryption_scope: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.EncryptionScope:
        """Update encryption scope properties as specified in the request body. Update fails if the
        specified encryption scope does not already exist.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number. Required.
        :type encryption_scope_name: str
        :param encryption_scope: Encryption scope properties to be used for the update. Required.
        :type encryption_scope: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2022_09_01.models.EncryptionScope
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def patch(
        self,
        resource_group_name: str,
        account_name: str,
        encryption_scope_name: str,
        encryption_scope: Union[_models.EncryptionScope, IO],
        **kwargs: Any
    ) -> _models.EncryptionScope:
        """Update encryption scope properties as specified in the request body. Update fails if the
        specified encryption scope does not already exist.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number. Required.
        :type encryption_scope_name: str
        :param encryption_scope: Encryption scope properties to be used for the update. Is either a
         model type or a IO type. Required.
        :type encryption_scope: ~azure.mgmt.storage.v2022_09_01.models.EncryptionScope or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2022_09_01.models.EncryptionScope
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-09-01"))  # type: Literal["2022-09-01"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.EncryptionScope]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(encryption_scope, (IO, bytes)):
            _content = encryption_scope
        else:
            _json = self._serialize.body(encryption_scope, "EncryptionScope")

        request = build_patch_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            encryption_scope_name=encryption_scope_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.patch.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("EncryptionScope", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    patch.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/encryptionScopes/{encryptionScopeName}"}  # type: ignore

    @distributed_trace
    def get(
        self, resource_group_name: str, account_name: str, encryption_scope_name: str, **kwargs: Any
    ) -> _models.EncryptionScope:
        """Returns the properties for the specified encryption scope.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param encryption_scope_name: The name of the encryption scope within the specified storage
         account. Encryption scope names must be between 3 and 63 characters in length and use numbers,
         lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and
         followed by a letter or number. Required.
        :type encryption_scope_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EncryptionScope or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2022_09_01.models.EncryptionScope
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-09-01"))  # type: Literal["2022-09-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.EncryptionScope]

        request = build_get_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            encryption_scope_name=encryption_scope_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("EncryptionScope", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/encryptionScopes/{encryptionScopeName}"}  # type: ignore

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        account_name: str,
        maxpagesize: Optional[int] = None,
        filter: Optional[str] = None,
        include: Optional[Union[str, _models.ListEncryptionScopesInclude]] = None,
        **kwargs: Any
    ) -> Iterable["_models.EncryptionScope"]:
        """Lists all the encryption scopes available under the specified storage account.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param maxpagesize: Optional, specifies the maximum number of encryption scopes that will be
         included in the list response. Default value is None.
        :type maxpagesize: int
        :param filter: Optional. When specified, only encryption scope names starting with the filter
         will be listed. Default value is None.
        :type filter: str
        :param include: Optional, when specified, will list encryption scopes with the specific state.
         Defaults to All. Known values are: "All", "Enabled", and "Disabled". Default value is None.
        :type include: str or ~azure.mgmt.storage.v2022_09_01.models.ListEncryptionScopesInclude
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either EncryptionScope or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.storage.v2022_09_01.models.EncryptionScope]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-09-01"))  # type: Literal["2022-09-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.EncryptionScopeListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    subscription_id=self._config.subscription_id,
                    maxpagesize=maxpagesize,
                    filter=filter,
                    include=include,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("EncryptionScopeListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/encryptionScopes"}  # type: ignore
