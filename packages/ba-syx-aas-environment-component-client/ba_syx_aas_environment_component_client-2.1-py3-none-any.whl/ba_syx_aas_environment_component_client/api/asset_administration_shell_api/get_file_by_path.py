from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.result import Result
from ...types import Response


def _get_kwargs(
    submodel_identifier: str,
    id_short_path: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/attachment",
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
    submodel_identifier: str,
    id_short_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Result]:
    """Downloads file content from a specific submodel element from the Submodel at a specified path

    Args:
        submodel_identifier (str):
        id_short_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Result]
    """

    kwargs = _get_kwargs(
        submodel_identifier=submodel_identifier,
        id_short_path=id_short_path,
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
) -> Optional[Result]:
    """Downloads file content from a specific submodel element from the Submodel at a specified path

    Args:
        submodel_identifier (str):
        id_short_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Result
    """

    return sync_detailed(
        submodel_identifier=submodel_identifier,
        id_short_path=id_short_path,
        client=client,
    ).parsed


async def asyncio_detailed(
    submodel_identifier: str,
    id_short_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Result]:
    """Downloads file content from a specific submodel element from the Submodel at a specified path

    Args:
        submodel_identifier (str):
        id_short_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Result]
    """

    kwargs = _get_kwargs(
        submodel_identifier=submodel_identifier,
        id_short_path=id_short_path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    submodel_identifier: str,
    id_short_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Result]:
    """Downloads file content from a specific submodel element from the Submodel at a specified path

    Args:
        submodel_identifier (str):
        id_short_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Result
    """

    return (
        await asyncio_detailed(
            submodel_identifier=submodel_identifier,
            id_short_path=id_short_path,
            client=client,
        )
    ).parsed
