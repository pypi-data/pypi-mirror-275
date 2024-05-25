from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entity import Entity
from ...models.operation import Operation
from ...models.relationship_element import RelationshipElement
from ...models.result import Result
from ...models.submodel_element import SubmodelElement
from ...models.submodel_element_collection import SubmodelElementCollection
from ...models.submodel_element_list import SubmodelElementList
from ...types import Response


def _get_kwargs(
    submodel_identifier: str,
    *,
    body: Union[
        "Entity",
        "Operation",
        "RelationshipElement",
        "SubmodelElement",
        "SubmodelElementCollection",
        "SubmodelElementList",
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/submodels/{submodel_identifier}/submodel-elements",
    }

    _body: Dict[str, Any]
    if isinstance(body, SubmodelElement):
        _body = body.to_dict()
    elif isinstance(body, SubmodelElement):
        _body = body.to_dict()
    elif isinstance(body, Entity):
        _body = body.to_dict()
    elif isinstance(body, SubmodelElement):
        _body = body.to_dict()
    elif isinstance(body, Operation):
        _body = body.to_dict()
    elif isinstance(body, RelationshipElement):
        _body = body.to_dict()
    elif isinstance(body, SubmodelElementCollection):
        _body = body.to_dict()
    else:
        _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Result, SubmodelElement]]:
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = Result.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Result.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Result.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.CREATED:
        response_201 = SubmodelElement.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Result.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Result.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.OK:
        response_200 = Result.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Result.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Result, SubmodelElement]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    submodel_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        "Entity",
        "Operation",
        "RelationshipElement",
        "SubmodelElement",
        "SubmodelElementCollection",
        "SubmodelElementList",
    ],
) -> Response[Union[Result, SubmodelElement]]:
    """Creates a new submodel element

    Args:
        submodel_identifier (str):
        body (Union['Entity', 'Operation', 'RelationshipElement', 'SubmodelElement',
            'SubmodelElementCollection', 'SubmodelElementList']): Requested submodel element

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Result, SubmodelElement]]
    """

    kwargs = _get_kwargs(
        submodel_identifier=submodel_identifier,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    submodel_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        "Entity",
        "Operation",
        "RelationshipElement",
        "SubmodelElement",
        "SubmodelElementCollection",
        "SubmodelElementList",
    ],
) -> Optional[Union[Result, SubmodelElement]]:
    """Creates a new submodel element

    Args:
        submodel_identifier (str):
        body (Union['Entity', 'Operation', 'RelationshipElement', 'SubmodelElement',
            'SubmodelElementCollection', 'SubmodelElementList']): Requested submodel element

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Result, SubmodelElement]
    """

    return sync_detailed(
        submodel_identifier=submodel_identifier,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    submodel_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        "Entity",
        "Operation",
        "RelationshipElement",
        "SubmodelElement",
        "SubmodelElementCollection",
        "SubmodelElementList",
    ],
) -> Response[Union[Result, SubmodelElement]]:
    """Creates a new submodel element

    Args:
        submodel_identifier (str):
        body (Union['Entity', 'Operation', 'RelationshipElement', 'SubmodelElement',
            'SubmodelElementCollection', 'SubmodelElementList']): Requested submodel element

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Result, SubmodelElement]]
    """

    kwargs = _get_kwargs(
        submodel_identifier=submodel_identifier,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    submodel_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        "Entity",
        "Operation",
        "RelationshipElement",
        "SubmodelElement",
        "SubmodelElementCollection",
        "SubmodelElementList",
    ],
) -> Optional[Union[Result, SubmodelElement]]:
    """Creates a new submodel element

    Args:
        submodel_identifier (str):
        body (Union['Entity', 'Operation', 'RelationshipElement', 'SubmodelElement',
            'SubmodelElementCollection', 'SubmodelElementList']): Requested submodel element

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Result, SubmodelElement]
    """

    return (
        await asyncio_detailed(
            submodel_identifier=submodel_identifier,
            client=client,
            body=body,
        )
    ).parsed
