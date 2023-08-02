from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.public_shared_cluster_response import PublicSharedClusterResponse
from ...models.server_error import ServerError
from ...models.unauthorized import Unauthorized
from ...models.upsert_shared_cluster_request import UpsertSharedClusterRequest
from ...types import Response


def _get_kwargs(
    technical_id: str,
    *,
    json_body: UpsertSharedClusterRequest,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/public/v1/clusters/{technicalId}".format(
            technicalId=technical_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[BadRequest, PublicSharedClusterResponse, ServerError, Unauthorized]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PublicSharedClusterResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = BadRequest.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Unauthorized.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ServerError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[BadRequest, PublicSharedClusterResponse, ServerError, Unauthorized]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    technical_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpsertSharedClusterRequest,
) -> Response[
    Union[BadRequest, PublicSharedClusterResponse, ServerError, Unauthorized]
]:
    """
    Create or update a cluster inside the organization
    The technical is mandatory. if it matches an existing cluster, it will be updated, otherwise it will
    be created.
    The slugs of the kafka connects must be unique within the cluster.

    Args:
        technical_id (str):
        json_body (UpsertSharedClusterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, PublicSharedClusterResponse, ServerError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        technical_id=technical_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    technical_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpsertSharedClusterRequest,
) -> Optional[
    Union[BadRequest, PublicSharedClusterResponse, ServerError, Unauthorized]
]:
    """
    Create or update a cluster inside the organization
    The technical is mandatory. if it matches an existing cluster, it will be updated, otherwise it will
    be created.
    The slugs of the kafka connects must be unique within the cluster.

    Args:
        technical_id (str):
        json_body (UpsertSharedClusterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, PublicSharedClusterResponse, ServerError, Unauthorized]
    """

    return sync_detailed(
        technical_id=technical_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    technical_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpsertSharedClusterRequest,
) -> Response[
    Union[BadRequest, PublicSharedClusterResponse, ServerError, Unauthorized]
]:
    """
    Create or update a cluster inside the organization
    The technical is mandatory. if it matches an existing cluster, it will be updated, otherwise it will
    be created.
    The slugs of the kafka connects must be unique within the cluster.

    Args:
        technical_id (str):
        json_body (UpsertSharedClusterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, PublicSharedClusterResponse, ServerError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        technical_id=technical_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    technical_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpsertSharedClusterRequest,
) -> Optional[
    Union[BadRequest, PublicSharedClusterResponse, ServerError, Unauthorized]
]:
    """
    Create or update a cluster inside the organization
    The technical is mandatory. if it matches an existing cluster, it will be updated, otherwise it will
    be created.
    The slugs of the kafka connects must be unique within the cluster.

    Args:
        technical_id (str):
        json_body (UpsertSharedClusterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, PublicSharedClusterResponse, ServerError, Unauthorized]
    """

    return (
        await asyncio_detailed(
            technical_id=technical_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
