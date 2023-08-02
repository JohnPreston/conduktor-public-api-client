from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.server_error import ServerError
from ...models.unauthorized import Unauthorized
from ...types import Response


def _get_kwargs(
    certificate_id: int,
) -> Dict[str, Any]:
    pass

    return {
        "method": "delete",
        "url": "/public/v1/certificates/{certificateId}".format(
            certificateId=certificate_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ServerError, Unauthorized]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
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
) -> Response[Union[Any, ServerError, Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    certificate_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ServerError, Unauthorized]]:
    """Delete a certificate from the organization

    Args:
        certificate_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ServerError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        certificate_id=certificate_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    certificate_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ServerError, Unauthorized]]:
    """Delete a certificate from the organization

    Args:
        certificate_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ServerError, Unauthorized]
    """

    return sync_detailed(
        certificate_id=certificate_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    certificate_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ServerError, Unauthorized]]:
    """Delete a certificate from the organization

    Args:
        certificate_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ServerError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        certificate_id=certificate_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    certificate_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ServerError, Unauthorized]]:
    """Delete a certificate from the organization

    Args:
        certificate_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ServerError, Unauthorized]
    """

    return (
        await asyncio_detailed(
            certificate_id=certificate_id,
            client=client,
        )
    ).parsed
