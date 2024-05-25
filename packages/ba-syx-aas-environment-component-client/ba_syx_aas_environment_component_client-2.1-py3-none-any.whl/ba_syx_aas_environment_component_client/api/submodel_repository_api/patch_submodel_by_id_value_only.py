from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entity import Entity
from ...models.operation import Operation
from ...models.patch_submodel_by_id_value_only_level import PatchSubmodelByIdValueOnlyLevel
from ...models.relationship_element import RelationshipElement
from ...models.result import Result
from ...models.submodel_element import SubmodelElement
from ...models.submodel_element_collection import SubmodelElementCollection
from ...models.submodel_element_list import SubmodelElementList
from ...models.submodel_value_only import SubmodelValueOnly
from ...types import UNSET, Response, Unset


def _get_kwargs(
    submodel_identifier: str,
    *,
    body: List[
        Union[
            "Entity",
            "Operation",
            "RelationshipElement",
            "SubmodelElement",
            "SubmodelElementCollection",
            "SubmodelElementList",
        ]
    ],
    level: Union[Unset, PatchSubmodelByIdValueOnlyLevel] = PatchSubmodelByIdValueOnlyLevel.DEEP,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    json_level: Union[Unset, str] = UNSET
    if not isinstance(level, Unset):
        json_level = level.value

    params["level"] = json_level

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/submodels/{submodel_identifier}/$value",
        "params": params,
    }

    _body = []
    for body_item_data in body:
        body_item: Dict[str, Any]
        if isinstance(body_item_data, SubmodelElement):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, SubmodelElement):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, Entity):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, SubmodelElement):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, Operation):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, RelationshipElement):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, SubmodelElementCollection):
            body_item = body_item_data.to_dict()
        else:
            body_item = body_item_data.to_dict()

        _body.append(body_item)

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Result, SubmodelValueOnly]]:
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Result.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Result.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Result.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = SubmodelValueOnly.from_dict(response.json())

        return response_204
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Result.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Result.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Result, SubmodelValueOnly]]:
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
    body: List[
        Union[
            "Entity",
            "Operation",
            "RelationshipElement",
            "SubmodelElement",
            "SubmodelElementCollection",
            "SubmodelElementList",
        ]
    ],
    level: Union[Unset, PatchSubmodelByIdValueOnlyLevel] = PatchSubmodelByIdValueOnlyLevel.DEEP,
) -> Response[Union[Result, SubmodelValueOnly]]:
    """Updates the values of an existing Submodel

    Args:
        submodel_identifier (str):
        level (Union[Unset, PatchSubmodelByIdValueOnlyLevel]):  Default:
            PatchSubmodelByIdValueOnlyLevel.DEEP.
        body (List[Union['Entity', 'Operation', 'RelationshipElement', 'SubmodelElement',
            'SubmodelElementCollection', 'SubmodelElementList']]): Submodel object in its ValueOnly
            representation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Result, SubmodelValueOnly]]
    """

    kwargs = _get_kwargs(
        submodel_identifier=submodel_identifier,
        body=body,
        level=level,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    submodel_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List[
        Union[
            "Entity",
            "Operation",
            "RelationshipElement",
            "SubmodelElement",
            "SubmodelElementCollection",
            "SubmodelElementList",
        ]
    ],
    level: Union[Unset, PatchSubmodelByIdValueOnlyLevel] = PatchSubmodelByIdValueOnlyLevel.DEEP,
) -> Optional[Union[Result, SubmodelValueOnly]]:
    """Updates the values of an existing Submodel

    Args:
        submodel_identifier (str):
        level (Union[Unset, PatchSubmodelByIdValueOnlyLevel]):  Default:
            PatchSubmodelByIdValueOnlyLevel.DEEP.
        body (List[Union['Entity', 'Operation', 'RelationshipElement', 'SubmodelElement',
            'SubmodelElementCollection', 'SubmodelElementList']]): Submodel object in its ValueOnly
            representation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Result, SubmodelValueOnly]
    """

    return sync_detailed(
        submodel_identifier=submodel_identifier,
        client=client,
        body=body,
        level=level,
    ).parsed


async def asyncio_detailed(
    submodel_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List[
        Union[
            "Entity",
            "Operation",
            "RelationshipElement",
            "SubmodelElement",
            "SubmodelElementCollection",
            "SubmodelElementList",
        ]
    ],
    level: Union[Unset, PatchSubmodelByIdValueOnlyLevel] = PatchSubmodelByIdValueOnlyLevel.DEEP,
) -> Response[Union[Result, SubmodelValueOnly]]:
    """Updates the values of an existing Submodel

    Args:
        submodel_identifier (str):
        level (Union[Unset, PatchSubmodelByIdValueOnlyLevel]):  Default:
            PatchSubmodelByIdValueOnlyLevel.DEEP.
        body (List[Union['Entity', 'Operation', 'RelationshipElement', 'SubmodelElement',
            'SubmodelElementCollection', 'SubmodelElementList']]): Submodel object in its ValueOnly
            representation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Result, SubmodelValueOnly]]
    """

    kwargs = _get_kwargs(
        submodel_identifier=submodel_identifier,
        body=body,
        level=level,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    submodel_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List[
        Union[
            "Entity",
            "Operation",
            "RelationshipElement",
            "SubmodelElement",
            "SubmodelElementCollection",
            "SubmodelElementList",
        ]
    ],
    level: Union[Unset, PatchSubmodelByIdValueOnlyLevel] = PatchSubmodelByIdValueOnlyLevel.DEEP,
) -> Optional[Union[Result, SubmodelValueOnly]]:
    """Updates the values of an existing Submodel

    Args:
        submodel_identifier (str):
        level (Union[Unset, PatchSubmodelByIdValueOnlyLevel]):  Default:
            PatchSubmodelByIdValueOnlyLevel.DEEP.
        body (List[Union['Entity', 'Operation', 'RelationshipElement', 'SubmodelElement',
            'SubmodelElementCollection', 'SubmodelElementList']]): Submodel object in its ValueOnly
            representation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Result, SubmodelValueOnly]
    """

    return (
        await asyncio_detailed(
            submodel_identifier=submodel_identifier,
            client=client,
            body=body,
            level=level,
        )
    ).parsed
