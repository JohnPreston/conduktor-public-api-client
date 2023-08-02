from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.not_found import NotFound
from ...models.public_with_all_details_and_group import PublicWithAllDetailsAndGroup
from ...models.server_error import ServerError
from ...models.unauthorized import Unauthorized
from ...types import Response


def _get_kwargs(
    email: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/public/v1/users/{email}".format(
            email=email,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[NotFound, PublicWithAllDetailsAndGroup, ServerError, Unauthorized]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PublicWithAllDetailsAndGroup.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Unauthorized.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = NotFound.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ServerError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[NotFound, PublicWithAllDetailsAndGroup, ServerError, Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    email: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[NotFound, PublicWithAllDetailsAndGroup, ServerError, Unauthorized]]:
    """Get a user by email

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NotFound, PublicWithAllDetailsAndGroup, ServerError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        email=email,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    email: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[NotFound, PublicWithAllDetailsAndGroup, ServerError, Unauthorized]]:
    """Get a user by email

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NotFound, PublicWithAllDetailsAndGroup, ServerError, Unauthorized]
    """

    return sync_detailed(
        email=email,
        client=client,
    ).parsed


async def asyncio_detailed(
    email: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[NotFound, PublicWithAllDetailsAndGroup, ServerError, Unauthorized]]:
    """Get a user by email

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[NotFound, PublicWithAllDetailsAndGroup, ServerError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        email=email,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    email: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[NotFound, PublicWithAllDetailsAndGroup, ServerError, Unauthorized]]:
    """Get a user by email

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[NotFound, PublicWithAllDetailsAndGroup, ServerError, Unauthorized]
    """

    return (
        await asyncio_detailed(
            email=email,
            client=client,
        )
    ).parsed
