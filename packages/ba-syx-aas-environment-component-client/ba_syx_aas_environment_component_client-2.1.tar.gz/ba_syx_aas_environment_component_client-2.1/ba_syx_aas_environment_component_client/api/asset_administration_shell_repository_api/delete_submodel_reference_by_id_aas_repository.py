from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.result import Result
from ...types import Response


def _get_kwargs(
    aas_identifier: str,
    submodel_identifier: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/shells/{aas_identifier}/submodel-refs/{submodel_identifier}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Result]]:
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Result.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Result.from_dict(response.json())

        return response_404
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
) -> Response[Union[Any, Result]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    aas_identifier: str,
    submodel_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Result]]:
    """Deletes the submodel reference from the Asset Administration Shell. Does not delete the submodel
    itself!

    Args:
        aas_identifier (str):
        submodel_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Result]]
    """

    kwargs = _get_kwargs(
        aas_identifier=aas_identifier,
        submodel_identifier=submodel_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    aas_identifier: str,
    submodel_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Result]]:
    """Deletes the submodel reference from the Asset Administration Shell. Does not delete the submodel
    itself!

    Args:
        aas_identifier (str):
        submodel_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Result]
    """

    return sync_detailed(
        aas_identifier=aas_identifier,
        submodel_identifier=submodel_identifier,
        client=client,
    ).parsed


async def asyncio_detailed(
    aas_identifier: str,
    submodel_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Result]]:
    """Deletes the submodel reference from the Asset Administration Shell. Does not delete the submodel
    itself!

    Args:
        aas_identifier (str):
        submodel_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Result]]
    """

    kwargs = _get_kwargs(
        aas_identifier=aas_identifier,
        submodel_identifier=submodel_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    aas_identifier: str,
    submodel_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Result]]:
    """Deletes the submodel reference from the Asset Administration Shell. Does not delete the submodel
    itself!

    Args:
        aas_identifier (str):
        submodel_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Result]
    """

    return (
        await asyncio_detailed(
            aas_identifier=aas_identifier,
            submodel_identifier=submodel_identifier,
            client=client,
        )
    ).parsed
