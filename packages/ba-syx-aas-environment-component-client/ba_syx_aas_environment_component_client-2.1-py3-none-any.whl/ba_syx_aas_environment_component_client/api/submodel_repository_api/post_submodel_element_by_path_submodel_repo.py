from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entity import Entity
from ...models.operation import Operation
from ...models.post_submodel_element_by_path_submodel_repo_extent import PostSubmodelElementByPathSubmodelRepoExtent
from ...models.post_submodel_element_by_path_submodel_repo_level import PostSubmodelElementByPathSubmodelRepoLevel
from ...models.relationship_element import RelationshipElement
from ...models.result import Result
from ...models.submodel_element import SubmodelElement
from ...models.submodel_element_collection import SubmodelElementCollection
from ...models.submodel_element_list import SubmodelElementList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    submodel_identifier: str,
    id_short_path: str,
    *,
    body: Union[
        "Entity",
        "Operation",
        "RelationshipElement",
        "SubmodelElement",
        "SubmodelElementCollection",
        "SubmodelElementList",
    ],
    level: Union[Unset, PostSubmodelElementByPathSubmodelRepoLevel] = PostSubmodelElementByPathSubmodelRepoLevel.DEEP,
    extent: Union[
        Unset, PostSubmodelElementByPathSubmodelRepoExtent
    ] = PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    json_level: Union[Unset, str] = UNSET
    if not isinstance(level, Unset):
        json_level = level.value

    params["level"] = json_level

    json_extent: Union[Unset, str] = UNSET
    if not isinstance(extent, Unset):
        json_extent = extent.value

    params["extent"] = json_extent

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/submodels/{submodel_identifier}/submodel-elements/{id_short_path}",
        "params": params,
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
    id_short_path: str,
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
    level: Union[Unset, PostSubmodelElementByPathSubmodelRepoLevel] = PostSubmodelElementByPathSubmodelRepoLevel.DEEP,
    extent: Union[
        Unset, PostSubmodelElementByPathSubmodelRepoExtent
    ] = PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE,
) -> Response[Union[Result, SubmodelElement]]:
    """Creates a new submodel element at a specified path within submodel elements hierarchy

    Args:
        submodel_identifier (str):
        id_short_path (str):
        level (Union[Unset, PostSubmodelElementByPathSubmodelRepoLevel]):  Default:
            PostSubmodelElementByPathSubmodelRepoLevel.DEEP.
        extent (Union[Unset, PostSubmodelElementByPathSubmodelRepoExtent]):  Default:
            PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE.
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
        id_short_path=id_short_path,
        body=body,
        level=level,
        extent=extent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    submodel_identifier: str,
    id_short_path: str,
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
    level: Union[Unset, PostSubmodelElementByPathSubmodelRepoLevel] = PostSubmodelElementByPathSubmodelRepoLevel.DEEP,
    extent: Union[
        Unset, PostSubmodelElementByPathSubmodelRepoExtent
    ] = PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE,
) -> Optional[Union[Result, SubmodelElement]]:
    """Creates a new submodel element at a specified path within submodel elements hierarchy

    Args:
        submodel_identifier (str):
        id_short_path (str):
        level (Union[Unset, PostSubmodelElementByPathSubmodelRepoLevel]):  Default:
            PostSubmodelElementByPathSubmodelRepoLevel.DEEP.
        extent (Union[Unset, PostSubmodelElementByPathSubmodelRepoExtent]):  Default:
            PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE.
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
        id_short_path=id_short_path,
        client=client,
        body=body,
        level=level,
        extent=extent,
    ).parsed


async def asyncio_detailed(
    submodel_identifier: str,
    id_short_path: str,
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
    level: Union[Unset, PostSubmodelElementByPathSubmodelRepoLevel] = PostSubmodelElementByPathSubmodelRepoLevel.DEEP,
    extent: Union[
        Unset, PostSubmodelElementByPathSubmodelRepoExtent
    ] = PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE,
) -> Response[Union[Result, SubmodelElement]]:
    """Creates a new submodel element at a specified path within submodel elements hierarchy

    Args:
        submodel_identifier (str):
        id_short_path (str):
        level (Union[Unset, PostSubmodelElementByPathSubmodelRepoLevel]):  Default:
            PostSubmodelElementByPathSubmodelRepoLevel.DEEP.
        extent (Union[Unset, PostSubmodelElementByPathSubmodelRepoExtent]):  Default:
            PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE.
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
        id_short_path=id_short_path,
        body=body,
        level=level,
        extent=extent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    submodel_identifier: str,
    id_short_path: str,
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
    level: Union[Unset, PostSubmodelElementByPathSubmodelRepoLevel] = PostSubmodelElementByPathSubmodelRepoLevel.DEEP,
    extent: Union[
        Unset, PostSubmodelElementByPathSubmodelRepoExtent
    ] = PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE,
) -> Optional[Union[Result, SubmodelElement]]:
    """Creates a new submodel element at a specified path within submodel elements hierarchy

    Args:
        submodel_identifier (str):
        id_short_path (str):
        level (Union[Unset, PostSubmodelElementByPathSubmodelRepoLevel]):  Default:
            PostSubmodelElementByPathSubmodelRepoLevel.DEEP.
        extent (Union[Unset, PostSubmodelElementByPathSubmodelRepoExtent]):  Default:
            PostSubmodelElementByPathSubmodelRepoExtent.WITHOUTBLOBVALUE.
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
            id_short_path=id_short_path,
            client=client,
            body=body,
            level=level,
            extent=extent,
        )
    ).parsed
