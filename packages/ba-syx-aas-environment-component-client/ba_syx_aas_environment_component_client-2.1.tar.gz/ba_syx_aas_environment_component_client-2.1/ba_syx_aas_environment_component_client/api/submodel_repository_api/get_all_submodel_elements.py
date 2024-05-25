from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_64_url_encoded_cursor import Base64UrlEncodedCursor
from ...models.get_all_submodel_elements_extent import GetAllSubmodelElementsExtent
from ...models.get_all_submodel_elements_level import GetAllSubmodelElementsLevel
from ...models.get_all_submodel_elements_limit import GetAllSubmodelElementsLimit
from ...models.result import Result
from ...types import UNSET, Response, Unset


def _get_kwargs(
    submodel_identifier: str,
    *,
    limit: Union[Unset, GetAllSubmodelElementsLimit] = UNSET,
    cursor: Union[Unset, "Base64UrlEncodedCursor"] = UNSET,
    level: Union[Unset, GetAllSubmodelElementsLevel] = GetAllSubmodelElementsLevel.DEEP,
    extent: Union[Unset, GetAllSubmodelElementsExtent] = GetAllSubmodelElementsExtent.WITHOUTBLOBVALUE,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_limit: Union[Unset, str] = UNSET
    if not isinstance(limit, Unset):
        json_limit = limit.value

    params["limit"] = json_limit

    json_cursor: Union[Unset, Dict[str, Any]] = UNSET
    if not isinstance(cursor, Unset):
        json_cursor = cursor.to_dict()
    if not isinstance(json_cursor, Unset):
        params.update(json_cursor)

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
        "method": "get",
        "url": f"/submodels/{submodel_identifier}/submodel-elements",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Result]:
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Result.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.OK:
        response_200 = Result.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Result.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Result.from_dict(response.json())

        return response_500
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Result]:
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
    limit: Union[Unset, GetAllSubmodelElementsLimit] = UNSET,
    cursor: Union[Unset, "Base64UrlEncodedCursor"] = UNSET,
    level: Union[Unset, GetAllSubmodelElementsLevel] = GetAllSubmodelElementsLevel.DEEP,
    extent: Union[Unset, GetAllSubmodelElementsExtent] = GetAllSubmodelElementsExtent.WITHOUTBLOBVALUE,
) -> Response[Result]:
    """Returns all submodel elements including their hierarchy

    Args:
        submodel_identifier (str):
        limit (Union[Unset, GetAllSubmodelElementsLimit]):
        cursor (Union[Unset, Base64UrlEncodedCursor]):
        level (Union[Unset, GetAllSubmodelElementsLevel]):  Default:
            GetAllSubmodelElementsLevel.DEEP.
        extent (Union[Unset, GetAllSubmodelElementsExtent]):  Default:
            GetAllSubmodelElementsExtent.WITHOUTBLOBVALUE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Result]
    """

    kwargs = _get_kwargs(
        submodel_identifier=submodel_identifier,
        limit=limit,
        cursor=cursor,
        level=level,
        extent=extent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    submodel_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, GetAllSubmodelElementsLimit] = UNSET,
    cursor: Union[Unset, "Base64UrlEncodedCursor"] = UNSET,
    level: Union[Unset, GetAllSubmodelElementsLevel] = GetAllSubmodelElementsLevel.DEEP,
    extent: Union[Unset, GetAllSubmodelElementsExtent] = GetAllSubmodelElementsExtent.WITHOUTBLOBVALUE,
) -> Optional[Result]:
    """Returns all submodel elements including their hierarchy

    Args:
        submodel_identifier (str):
        limit (Union[Unset, GetAllSubmodelElementsLimit]):
        cursor (Union[Unset, Base64UrlEncodedCursor]):
        level (Union[Unset, GetAllSubmodelElementsLevel]):  Default:
            GetAllSubmodelElementsLevel.DEEP.
        extent (Union[Unset, GetAllSubmodelElementsExtent]):  Default:
            GetAllSubmodelElementsExtent.WITHOUTBLOBVALUE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Result
    """

    return sync_detailed(
        submodel_identifier=submodel_identifier,
        client=client,
        limit=limit,
        cursor=cursor,
        level=level,
        extent=extent,
    ).parsed


async def asyncio_detailed(
    submodel_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, GetAllSubmodelElementsLimit] = UNSET,
    cursor: Union[Unset, "Base64UrlEncodedCursor"] = UNSET,
    level: Union[Unset, GetAllSubmodelElementsLevel] = GetAllSubmodelElementsLevel.DEEP,
    extent: Union[Unset, GetAllSubmodelElementsExtent] = GetAllSubmodelElementsExtent.WITHOUTBLOBVALUE,
) -> Response[Result]:
    """Returns all submodel elements including their hierarchy

    Args:
        submodel_identifier (str):
        limit (Union[Unset, GetAllSubmodelElementsLimit]):
        cursor (Union[Unset, Base64UrlEncodedCursor]):
        level (Union[Unset, GetAllSubmodelElementsLevel]):  Default:
            GetAllSubmodelElementsLevel.DEEP.
        extent (Union[Unset, GetAllSubmodelElementsExtent]):  Default:
            GetAllSubmodelElementsExtent.WITHOUTBLOBVALUE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Result]
    """

    kwargs = _get_kwargs(
        submodel_identifier=submodel_identifier,
        limit=limit,
        cursor=cursor,
        level=level,
        extent=extent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    submodel_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, GetAllSubmodelElementsLimit] = UNSET,
    cursor: Union[Unset, "Base64UrlEncodedCursor"] = UNSET,
    level: Union[Unset, GetAllSubmodelElementsLevel] = GetAllSubmodelElementsLevel.DEEP,
    extent: Union[Unset, GetAllSubmodelElementsExtent] = GetAllSubmodelElementsExtent.WITHOUTBLOBVALUE,
) -> Optional[Result]:
    """Returns all submodel elements including their hierarchy

    Args:
        submodel_identifier (str):
        limit (Union[Unset, GetAllSubmodelElementsLimit]):
        cursor (Union[Unset, Base64UrlEncodedCursor]):
        level (Union[Unset, GetAllSubmodelElementsLevel]):  Default:
            GetAllSubmodelElementsLevel.DEEP.
        extent (Union[Unset, GetAllSubmodelElementsExtent]):  Default:
            GetAllSubmodelElementsExtent.WITHOUTBLOBVALUE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Result
    """

    return (
        await asyncio_detailed(
            submodel_identifier=submodel_identifier,
            client=client,
            limit=limit,
            cursor=cursor,
            level=level,
            extent=extent,
        )
    ).parsed
