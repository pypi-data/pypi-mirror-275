from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_64_url_encoded_cursor import Base64UrlEncodedCursor
from ...models.get_all_concept_descriptions_limit import GetAllConceptDescriptionsLimit
from ...models.result import Result
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id_short: Union[Unset, str] = UNSET,
    is_case_of: Union[Unset, str] = UNSET,
    data_specification_ref: Union[Unset, str] = UNSET,
    limit: Union[Unset, GetAllConceptDescriptionsLimit] = UNSET,
    cursor: Union[Unset, "Base64UrlEncodedCursor"] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["idShort"] = id_short

    params["isCaseOf"] = is_case_of

    params["dataSpecificationRef"] = data_specification_ref

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
        "url": "/concept-descriptions",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Result]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Result.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Result.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Result.from_dict(response.json())

        return response_500
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
    *,
    client: Union[AuthenticatedClient, Client],
    id_short: Union[Unset, str] = UNSET,
    is_case_of: Union[Unset, str] = UNSET,
    data_specification_ref: Union[Unset, str] = UNSET,
    limit: Union[Unset, GetAllConceptDescriptionsLimit] = UNSET,
    cursor: Union[Unset, "Base64UrlEncodedCursor"] = UNSET,
) -> Response[Result]:
    """Returns all Concept Descriptions

    Args:
        id_short (Union[Unset, str]):
        is_case_of (Union[Unset, str]):
        data_specification_ref (Union[Unset, str]):
        limit (Union[Unset, GetAllConceptDescriptionsLimit]):
        cursor (Union[Unset, Base64UrlEncodedCursor]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Result]
    """

    kwargs = _get_kwargs(
        id_short=id_short,
        is_case_of=is_case_of,
        data_specification_ref=data_specification_ref,
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
    id_short: Union[Unset, str] = UNSET,
    is_case_of: Union[Unset, str] = UNSET,
    data_specification_ref: Union[Unset, str] = UNSET,
    limit: Union[Unset, GetAllConceptDescriptionsLimit] = UNSET,
    cursor: Union[Unset, "Base64UrlEncodedCursor"] = UNSET,
) -> Optional[Result]:
    """Returns all Concept Descriptions

    Args:
        id_short (Union[Unset, str]):
        is_case_of (Union[Unset, str]):
        data_specification_ref (Union[Unset, str]):
        limit (Union[Unset, GetAllConceptDescriptionsLimit]):
        cursor (Union[Unset, Base64UrlEncodedCursor]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Result
    """

    return sync_detailed(
        client=client,
        id_short=id_short,
        is_case_of=is_case_of,
        data_specification_ref=data_specification_ref,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    id_short: Union[Unset, str] = UNSET,
    is_case_of: Union[Unset, str] = UNSET,
    data_specification_ref: Union[Unset, str] = UNSET,
    limit: Union[Unset, GetAllConceptDescriptionsLimit] = UNSET,
    cursor: Union[Unset, "Base64UrlEncodedCursor"] = UNSET,
) -> Response[Result]:
    """Returns all Concept Descriptions

    Args:
        id_short (Union[Unset, str]):
        is_case_of (Union[Unset, str]):
        data_specification_ref (Union[Unset, str]):
        limit (Union[Unset, GetAllConceptDescriptionsLimit]):
        cursor (Union[Unset, Base64UrlEncodedCursor]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Result]
    """

    kwargs = _get_kwargs(
        id_short=id_short,
        is_case_of=is_case_of,
        data_specification_ref=data_specification_ref,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    id_short: Union[Unset, str] = UNSET,
    is_case_of: Union[Unset, str] = UNSET,
    data_specification_ref: Union[Unset, str] = UNSET,
    limit: Union[Unset, GetAllConceptDescriptionsLimit] = UNSET,
    cursor: Union[Unset, "Base64UrlEncodedCursor"] = UNSET,
) -> Optional[Result]:
    """Returns all Concept Descriptions

    Args:
        id_short (Union[Unset, str]):
        is_case_of (Union[Unset, str]):
        data_specification_ref (Union[Unset, str]):
        limit (Union[Unset, GetAllConceptDescriptionsLimit]):
        cursor (Union[Unset, Base64UrlEncodedCursor]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Result
    """

    return (
        await asyncio_detailed(
            client=client,
            id_short=id_short,
            is_case_of=is_case_of,
            data_specification_ref=data_specification_ref,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
