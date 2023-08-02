from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_group_response import CreateGroupResponse
from ...models.public_create_group_request import PublicCreateGroupRequest
from ...models.server_error import ServerError
from ...models.unauthorized import Unauthorized
from ...types import Response


def _get_kwargs(
    *,
    json_body: PublicCreateGroupRequest,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/public/v1/groups",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateGroupResponse, ServerError, Unauthorized]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateGroupResponse.from_dict(response.json())

        return response_201
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
) -> Response[Union[CreateGroupResponse, ServerError, Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: PublicCreateGroupRequest,
) -> Response[Union[CreateGroupResponse, ServerError, Unauthorized]]:
    """Create a new group in the organization

    Args:
        json_body (PublicCreateGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateGroupResponse, ServerError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: PublicCreateGroupRequest,
) -> Optional[Union[CreateGroupResponse, ServerError, Unauthorized]]:
    """Create a new group in the organization

    Args:
        json_body (PublicCreateGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateGroupResponse, ServerError, Unauthorized]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: PublicCreateGroupRequest,
) -> Response[Union[CreateGroupResponse, ServerError, Unauthorized]]:
    """Create a new group in the organization

    Args:
        json_body (PublicCreateGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateGroupResponse, ServerError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: PublicCreateGroupRequest,
) -> Optional[Union[CreateGroupResponse, ServerError, Unauthorized]]:
    """Create a new group in the organization

    Args:
        json_body (PublicCreateGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateGroupResponse, ServerError, Unauthorized]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
