from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.create_certificate_from_file_request import (
    CreateCertificateFromFileRequest,
)
from ...models.decoded_certificate import DecodedCertificate
from ...models.server_error import ServerError
from ...models.unauthorized import Unauthorized
from ...types import Response


def _get_kwargs(
    *,
    multipart_data: CreateCertificateFromFileRequest,
) -> Dict[str, Any]:
    pass

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/public/v1/certificates/file",
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, List["DecodedCertificate"], ServerError, Unauthorized]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = DecodedCertificate.from_dict(response_201_item_data)

            response_201.append(response_201_item)

        return response_201
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
) -> Response[Union[BadRequest, List["DecodedCertificate"], ServerError, Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateCertificateFromFileRequest,
) -> Response[Union[BadRequest, List["DecodedCertificate"], ServerError, Unauthorized]]:
    """Import certificates in the organization from a file (.crt, .pem. or .jks)

    Args:
        multipart_data (CreateCertificateFromFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, List['DecodedCertificate'], ServerError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateCertificateFromFileRequest,
) -> Optional[Union[BadRequest, List["DecodedCertificate"], ServerError, Unauthorized]]:
    """Import certificates in the organization from a file (.crt, .pem. or .jks)

    Args:
        multipart_data (CreateCertificateFromFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, List['DecodedCertificate'], ServerError, Unauthorized]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateCertificateFromFileRequest,
) -> Response[Union[BadRequest, List["DecodedCertificate"], ServerError, Unauthorized]]:
    """Import certificates in the organization from a file (.crt, .pem. or .jks)

    Args:
        multipart_data (CreateCertificateFromFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, List['DecodedCertificate'], ServerError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateCertificateFromFileRequest,
) -> Optional[Union[BadRequest, List["DecodedCertificate"], ServerError, Unauthorized]]:
    """Import certificates in the organization from a file (.crt, .pem. or .jks)

    Args:
        multipart_data (CreateCertificateFromFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, List['DecodedCertificate'], ServerError, Unauthorized]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
