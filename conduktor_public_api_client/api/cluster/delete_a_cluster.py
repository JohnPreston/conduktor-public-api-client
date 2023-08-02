from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.not_found import NotFound
from ...models.server_error import ServerError
from ...models.unauthorized import Unauthorized
from ...types import Response


def _get_kwargs(
    technical_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "delete",
        "url": "/public/v1/clusters/{technicalId}".format(
            technicalId=technical_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, NotFound, ServerError, Unauthorized]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
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
) -> Response[Union[Any, NotFound, ServerError, Unauthorized]]:
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
) -> Response[Union[Any, NotFound, ServerError, Unauthorized]]:
    """
    Args:
        technical_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFound, ServerError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        technical_id=technical_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    technical_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, NotFound, ServerError, Unauthorized]]:
    """
    Args:
        technical_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFound, ServerError, Unauthorized]
    """

    return sync_detailed(
        technical_id=technical_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    technical_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, NotFound, ServerError, Unauthorized]]:
    """
    Args:
        technical_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFound, ServerError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        technical_id=technical_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    technical_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, NotFound, ServerError, Unauthorized]]:
    """
    Args:
        technical_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFound, ServerError, Unauthorized]
    """

    return (
        await asyncio_detailed(
            technical_id=technical_id,
            client=client,
        )
    ).parsed
