from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.cluster import Cluster
from ...models.consumer_group import ConsumerGroup
from ...models.kafka_connect_1 import KafkaConnect1
from ...models.not_found import NotFound
from ...models.platform import Platform
from ...models.server_error import ServerError
from ...models.subject import Subject
from ...models.topic import Topic
from ...models.unauthorized import Unauthorized
from ...types import Response


def _get_kwargs(
    email: str,
    *,
    json_body: List[
        Union[
            "Cluster", "ConsumerGroup", "KafkaConnect1", "Platform", "Subject", "Topic"
        ]
    ],
) -> Dict[str, Any]:
    pass

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item: Dict[str, Any]

        if isinstance(json_body_item_data, Cluster):
            json_body_item = json_body_item_data.to_dict()

        elif isinstance(json_body_item_data, ConsumerGroup):
            json_body_item = json_body_item_data.to_dict()

        elif isinstance(json_body_item_data, KafkaConnect1):
            json_body_item = json_body_item_data.to_dict()

        elif isinstance(json_body_item_data, Platform):
            json_body_item = json_body_item_data.to_dict()

        elif isinstance(json_body_item_data, Subject):
            json_body_item = json_body_item_data.to_dict()

        else:
            json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

    return {
        "method": "put",
        "url": "/public/v1/users/{email}/permissions".format(
            email=email,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BadRequest, NotFound, ServerError, Unauthorized]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = BadRequest.from_dict(response.json())

        return response_400
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
) -> Response[Union[Any, BadRequest, NotFound, ServerError, Unauthorized]]:
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
    json_body: List[
        Union[
            "Cluster", "ConsumerGroup", "KafkaConnect1", "Platform", "Subject", "Topic"
        ]
    ],
) -> Response[Union[Any, BadRequest, NotFound, ServerError, Unauthorized]]:
    """Set permissions to user

    Args:
        email (str):
        json_body (List[Union['Cluster', 'ConsumerGroup', 'KafkaConnect1', 'Platform', 'Subject',
            'Topic']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BadRequest, NotFound, ServerError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        email=email,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    email: str,
    *,
    client: AuthenticatedClient,
    json_body: List[
        Union[
            "Cluster", "ConsumerGroup", "KafkaConnect1", "Platform", "Subject", "Topic"
        ]
    ],
) -> Optional[Union[Any, BadRequest, NotFound, ServerError, Unauthorized]]:
    """Set permissions to user

    Args:
        email (str):
        json_body (List[Union['Cluster', 'ConsumerGroup', 'KafkaConnect1', 'Platform', 'Subject',
            'Topic']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BadRequest, NotFound, ServerError, Unauthorized]
    """

    return sync_detailed(
        email=email,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    email: str,
    *,
    client: AuthenticatedClient,
    json_body: List[
        Union[
            "Cluster", "ConsumerGroup", "KafkaConnect1", "Platform", "Subject", "Topic"
        ]
    ],
) -> Response[Union[Any, BadRequest, NotFound, ServerError, Unauthorized]]:
    """Set permissions to user

    Args:
        email (str):
        json_body (List[Union['Cluster', 'ConsumerGroup', 'KafkaConnect1', 'Platform', 'Subject',
            'Topic']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BadRequest, NotFound, ServerError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        email=email,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    email: str,
    *,
    client: AuthenticatedClient,
    json_body: List[
        Union[
            "Cluster", "ConsumerGroup", "KafkaConnect1", "Platform", "Subject", "Topic"
        ]
    ],
) -> Optional[Union[Any, BadRequest, NotFound, ServerError, Unauthorized]]:
    """Set permissions to user

    Args:
        email (str):
        json_body (List[Union['Cluster', 'ConsumerGroup', 'KafkaConnect1', 'Platform', 'Subject',
            'Topic']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BadRequest, NotFound, ServerError, Unauthorized]
    """

    return (
        await asyncio_detailed(
            email=email,
            client=client,
            json_body=json_body,
        )
    ).parsed
