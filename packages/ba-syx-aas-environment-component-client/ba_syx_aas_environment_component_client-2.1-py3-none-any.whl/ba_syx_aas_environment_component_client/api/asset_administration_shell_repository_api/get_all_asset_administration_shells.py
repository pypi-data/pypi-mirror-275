from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_64_url_encoded_cursor import Base64UrlEncodedCursor
from ...models.get_all_asset_administration_shells_limit import GetAllAssetAdministrationShellsLimit
from ...models.get_asset_administration_shells_result import GetAssetAdministrationShellsResult
from ...models.result import Result
from ...models.specific_asset_id import SpecificAssetId
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset_ids: Union[Unset, List["SpecificAssetId"]] = UNSET,
    id_short: Union[Unset, str] = UNSET,
    limit: Union[Unset, GetAllAssetAdministrationShellsLimit] = UNSET,
    cursor: Union[Unset, "Base64UrlEncodedCursor"] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_asset_ids: Union[Unset, List[Dict[str, Any]]] = UNSET
    if not isinstance(asset_ids, Unset):
        json_asset_ids = []
        for asset_ids_item_data in asset_ids:
            asset_ids_item = asset_ids_item_data.to_dict()
            json_asset_ids.append(asset_ids_item)

    params["assetIds"] = json_asset_ids

    params["idShort"] = id_short

    json_limit: Union[Unset, str] = UNSET
    if not isinstance(limit, Unset):
        json_limit = limit.value

    params["limit"] = json_limit

    json_cursor: Union[Unset, Dict[str, Any]] = UNSET
    if not isinstance(cursor, Unset):
        json_cursor = cursor.to_dict()
    if not isinstance(json_cursor, Unset):
        params.update(json_cursor)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/shells",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetAssetAdministrationShellsResult, Result]]:
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Result.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.OK:
        response_200 = GetAssetAdministrationShellsResult.from_dict(response.json())

        return response_200
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


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetAssetAdministrationShellsResult, Result]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    asset_ids: Union[Unset, List["SpecificAssetId"]] = UNSET,
    id_short: Union[Unset, str] = UNSET,
    limit: Union[Unset, GetAllAssetAdministrationShellsLimit] = UNSET,
    cursor: Union[Unset, "Base64UrlEncodedCursor"] = UNSET,
) -> Response[Union[GetAssetAdministrationShellsResult, Result]]:
    """Returns all Asset Administration Shells

    Args:
        asset_ids (Union[Unset, List['SpecificAssetId']]):
        id_short (Union[Unset, str]):
        limit (Union[Unset, GetAllAssetAdministrationShellsLimit]):
        cursor (Union[Unset, Base64UrlEncodedCursor]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetAssetAdministrationShellsResult, Result]]
    """

    kwargs = _get_kwargs(
        asset_ids=asset_ids,
        id_short=id_short,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    asset_ids: Union[Unset, List["SpecificAssetId"]] = UNSET,
    id_short: Union[Unset, str] = UNSET,
    limit: Union[Unset, GetAllAssetAdministrationShellsLimit] = UNSET,
    cursor: Union[Unset, "Base64UrlEncodedCursor"] = UNSET,
) -> Optional[Union[GetAssetAdministrationShellsResult, Result]]:
    """Returns all Asset Administration Shells

    Args:
        asset_ids (Union[Unset, List['SpecificAssetId']]):
        id_short (Union[Unset, str]):
        limit (Union[Unset, GetAllAssetAdministrationShellsLimit]):
        cursor (Union[Unset, Base64UrlEncodedCursor]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetAssetAdministrationShellsResult, Result]
    """

    return sync_detailed(
        client=client,
        asset_ids=asset_ids,
        id_short=id_short,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    asset_ids: Union[Unset, List["SpecificAssetId"]] = UNSET,
    id_short: Union[Unset, str] = UNSET,
    limit: Union[Unset, GetAllAssetAdministrationShellsLimit] = UNSET,
    cursor: Union[Unset, "Base64UrlEncodedCursor"] = UNSET,
) -> Response[Union[GetAssetAdministrationShellsResult, Result]]:
    """Returns all Asset Administration Shells

    Args:
        asset_ids (Union[Unset, List['SpecificAssetId']]):
        id_short (Union[Unset, str]):
        limit (Union[Unset, GetAllAssetAdministrationShellsLimit]):
        cursor (Union[Unset, Base64UrlEncodedCursor]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetAssetAdministrationShellsResult, Result]]
    """

    kwargs = _get_kwargs(
        asset_ids=asset_ids,
        id_short=id_short,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    asset_ids: Union[Unset, List["SpecificAssetId"]] = UNSET,
    id_short: Union[Unset, str] = UNSET,
    limit: Union[Unset, GetAllAssetAdministrationShellsLimit] = UNSET,
    cursor: Union[Unset, "Base64UrlEncodedCursor"] = UNSET,
) -> Optional[Union[GetAssetAdministrationShellsResult, Result]]:
    """Returns all Asset Administration Shells

    Args:
        asset_ids (Union[Unset, List['SpecificAssetId']]):
        id_short (Union[Unset, str]):
        limit (Union[Unset, GetAllAssetAdministrationShellsLimit]):
        cursor (Union[Unset, Base64UrlEncodedCursor]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetAssetAdministrationShellsResult, Result]
    """

    return (
        await asyncio_detailed(
            client=client,
            asset_ids=asset_ids,
            id_short=id_short,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
