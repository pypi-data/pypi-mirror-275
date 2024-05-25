from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.result import Result
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    aas_ids: Union[Unset, List[str]] = UNSET,
    submodel_ids: Union[Unset, List[str]] = UNSET,
    include_concept_descriptions: Union[Unset, str] = "true",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_aas_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(aas_ids, Unset):
        json_aas_ids = aas_ids

    params["aasIds"] = json_aas_ids

    json_submodel_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(submodel_ids, Unset):
        json_submodel_ids = submodel_ids

    params["submodelIds"] = json_submodel_ids

    params["includeConceptDescriptions"] = include_concept_descriptions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/serialization",
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
    *,
    client: Union[AuthenticatedClient, Client],
    aas_ids: Union[Unset, List[str]] = UNSET,
    submodel_ids: Union[Unset, List[str]] = UNSET,
    include_concept_descriptions: Union[Unset, str] = "true",
) -> Response[Result]:
    """Returns an appropriate serialization based on the specified format (see SerializationFormat)

    Args:
        aas_ids (Union[Unset, List[str]]):
        submodel_ids (Union[Unset, List[str]]):
        include_concept_descriptions (Union[Unset, str]):  Default: 'true'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Result]
    """

    kwargs = _get_kwargs(
        aas_ids=aas_ids,
        submodel_ids=submodel_ids,
        include_concept_descriptions=include_concept_descriptions,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    aas_ids: Union[Unset, List[str]] = UNSET,
    submodel_ids: Union[Unset, List[str]] = UNSET,
    include_concept_descriptions: Union[Unset, str] = "true",
) -> Optional[Result]:
    """Returns an appropriate serialization based on the specified format (see SerializationFormat)

    Args:
        aas_ids (Union[Unset, List[str]]):
        submodel_ids (Union[Unset, List[str]]):
        include_concept_descriptions (Union[Unset, str]):  Default: 'true'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Result
    """

    return sync_detailed(
        client=client,
        aas_ids=aas_ids,
        submodel_ids=submodel_ids,
        include_concept_descriptions=include_concept_descriptions,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    aas_ids: Union[Unset, List[str]] = UNSET,
    submodel_ids: Union[Unset, List[str]] = UNSET,
    include_concept_descriptions: Union[Unset, str] = "true",
) -> Response[Result]:
    """Returns an appropriate serialization based on the specified format (see SerializationFormat)

    Args:
        aas_ids (Union[Unset, List[str]]):
        submodel_ids (Union[Unset, List[str]]):
        include_concept_descriptions (Union[Unset, str]):  Default: 'true'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Result]
    """

    kwargs = _get_kwargs(
        aas_ids=aas_ids,
        submodel_ids=submodel_ids,
        include_concept_descriptions=include_concept_descriptions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    aas_ids: Union[Unset, List[str]] = UNSET,
    submodel_ids: Union[Unset, List[str]] = UNSET,
    include_concept_descriptions: Union[Unset, str] = "true",
) -> Optional[Result]:
    """Returns an appropriate serialization based on the specified format (see SerializationFormat)

    Args:
        aas_ids (Union[Unset, List[str]]):
        submodel_ids (Union[Unset, List[str]]):
        include_concept_descriptions (Union[Unset, str]):  Default: 'true'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Result
    """

    return (
        await asyncio_detailed(
            client=client,
            aas_ids=aas_ids,
            submodel_ids=submodel_ids,
            include_concept_descriptions=include_concept_descriptions,
        )
    ).parsed
