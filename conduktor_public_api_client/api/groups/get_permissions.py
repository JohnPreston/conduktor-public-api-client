from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
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
    group_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/public/v1/groups/{groupId}/permissions".format(
            groupId=group_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        List[
            Union[
                "Cluster",
                "ConsumerGroup",
                "KafkaConnect1",
                "Platform",
                "Subject",
                "Topic",
            ]
        ],
        NotFound,
        ServerError,
        Unauthorized,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(
                data: object,
            ) -> Union[
                "Cluster",
                "ConsumerGroup",
                "KafkaConnect1",
                "Platform",
                "Subject",
                "Topic",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_resource_permissions_type_0 = Cluster.from_dict(
                        data
                    )

                    return componentsschemas_resource_permissions_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_resource_permissions_type_1 = (
                        ConsumerGroup.from_dict(data)
                    )

                    return componentsschemas_resource_permissions_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_resource_permissions_type_2 = (
                        KafkaConnect1.from_dict(data)
                    )

                    return componentsschemas_resource_permissions_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_resource_permissions_type_3 = Platform.from_dict(
                        data
                    )

                    return componentsschemas_resource_permissions_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_resource_permissions_type_4 = Subject.from_dict(
                        data
                    )

                    return componentsschemas_resource_permissions_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_resource_permissions_type_5 = Topic.from_dict(data)

                return componentsschemas_resource_permissions_type_5

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[
    Union[
        List[
            Union[
                "Cluster",
                "ConsumerGroup",
                "KafkaConnect1",
                "Platform",
                "Subject",
                "Topic",
            ]
        ],
        NotFound,
        ServerError,
        Unauthorized,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        List[
            Union[
                "Cluster",
                "ConsumerGroup",
                "KafkaConnect1",
                "Platform",
                "Subject",
                "Topic",
            ]
        ],
        NotFound,
        ServerError,
        Unauthorized,
    ]
]:
    """Get group's permissions

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List[Union['Cluster', 'ConsumerGroup', 'KafkaConnect1', 'Platform', 'Subject', 'Topic']], NotFound, ServerError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        List[
            Union[
                "Cluster",
                "ConsumerGroup",
                "KafkaConnect1",
                "Platform",
                "Subject",
                "Topic",
            ]
        ],
        NotFound,
        ServerError,
        Unauthorized,
    ]
]:
    """Get group's permissions

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List[Union['Cluster', 'ConsumerGroup', 'KafkaConnect1', 'Platform', 'Subject', 'Topic']], NotFound, ServerError, Unauthorized]
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        List[
            Union[
                "Cluster",
                "ConsumerGroup",
                "KafkaConnect1",
                "Platform",
                "Subject",
                "Topic",
            ]
        ],
        NotFound,
        ServerError,
        Unauthorized,
    ]
]:
    """Get group's permissions

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List[Union['Cluster', 'ConsumerGroup', 'KafkaConnect1', 'Platform', 'Subject', 'Topic']], NotFound, ServerError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        List[
            Union[
                "Cluster",
                "ConsumerGroup",
                "KafkaConnect1",
                "Platform",
                "Subject",
                "Topic",
            ]
        ],
        NotFound,
        ServerError,
        Unauthorized,
    ]
]:
    """Get group's permissions

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List[Union['Cluster', 'ConsumerGroup', 'KafkaConnect1', 'Platform', 'Subject', 'Topic']], NotFound, ServerError, Unauthorized]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
