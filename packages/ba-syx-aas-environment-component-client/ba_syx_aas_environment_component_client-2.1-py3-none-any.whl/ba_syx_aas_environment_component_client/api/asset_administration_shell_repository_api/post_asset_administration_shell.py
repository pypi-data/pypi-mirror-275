from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_administration_shell import AssetAdministrationShell
from ...models.result import Result
from ...types import Response


def _get_kwargs(
    *,
    body: AssetAdministrationShell,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/shells",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AssetAdministrationShell, Result]]:
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = Result.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Result.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.CREATED:
        response_201 = AssetAdministrationShell.from_dict(response.json())

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
) -> Response[Union[AssetAdministrationShell, Result]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssetAdministrationShell,
) -> Response[Union[AssetAdministrationShell, Result]]:
    """Creates a new Asset Administration Shell

    Args:
        body (AssetAdministrationShell):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssetAdministrationShell, Result]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssetAdministrationShell,
) -> Optional[Union[AssetAdministrationShell, Result]]:
    """Creates a new Asset Administration Shell

    Args:
        body (AssetAdministrationShell):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssetAdministrationShell, Result]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssetAdministrationShell,
) -> Response[Union[AssetAdministrationShell, Result]]:
    """Creates a new Asset Administration Shell

    Args:
        body (AssetAdministrationShell):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssetAdministrationShell, Result]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssetAdministrationShell,
) -> Optional[Union[AssetAdministrationShell, Result]]:
    """Creates a new Asset Administration Shell

    Args:
        body (AssetAdministrationShell):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssetAdministrationShell, Result]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
