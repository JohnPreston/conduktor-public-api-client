from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.server_error import ServerError
from ...models.tls_test_request import TlsTestRequest
from ...models.tls_test_response import TlsTestResponse
from ...models.unauthorized import Unauthorized
from ...types import Response


def _get_kwargs(
    *,
    json_body: TlsTestRequest,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/public/v1/certificates/tls-test",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, ServerError, TlsTestResponse, Unauthorized]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TlsTestResponse.from_dict(response.json())

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
) -> Response[Union[BadRequest, ServerError, TlsTestResponse, Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: TlsTestRequest,
) -> Response[Union[BadRequest, ServerError, TlsTestResponse, Unauthorized]]:
    """Test a tcp target with the organization's certificates (Kafka uses the TLS/TCP protocol)

    Args:
        json_body (TlsTestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, ServerError, TlsTestResponse, Unauthorized]]
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
    json_body: TlsTestRequest,
) -> Optional[Union[BadRequest, ServerError, TlsTestResponse, Unauthorized]]:
    """Test a tcp target with the organization's certificates (Kafka uses the TLS/TCP protocol)

    Args:
        json_body (TlsTestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, ServerError, TlsTestResponse, Unauthorized]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: TlsTestRequest,
) -> Response[Union[BadRequest, ServerError, TlsTestResponse, Unauthorized]]:
    """Test a tcp target with the organization's certificates (Kafka uses the TLS/TCP protocol)

    Args:
        json_body (TlsTestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, ServerError, TlsTestResponse, Unauthorized]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: TlsTestRequest,
) -> Optional[Union[BadRequest, ServerError, TlsTestResponse, Unauthorized]]:
    """Test a tcp target with the organization's certificates (Kafka uses the TLS/TCP protocol)

    Args:
        json_body (TlsTestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, ServerError, TlsTestResponse, Unauthorized]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
