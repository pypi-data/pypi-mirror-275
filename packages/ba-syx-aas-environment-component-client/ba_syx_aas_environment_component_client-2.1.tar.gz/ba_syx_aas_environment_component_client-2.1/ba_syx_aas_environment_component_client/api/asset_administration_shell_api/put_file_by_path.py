from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_file_by_path_body import PutFileByPathBody
from ...models.result import Result
from ...types import UNSET, Response


def _get_kwargs(
    submodel_identifier: str,
    id_short_path: str,
    *,
    body: PutFileByPathBody,
    file_name: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["fileName"] = file_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/submodels/{submodel_identifier}/submodel-elements/{id_short_path}/attachment",
        "params": params,
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Result]]:
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
        response_204 = cast(Any, None)
        return response_204
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
    submodel_identifier: str,
    id_short_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutFileByPathBody,
    file_name: str,
) -> Response[Union[Any, Result]]:
    """Uploads file content to an existing submodel element at a specified path within submodel elements
    hierarchy

    Args:
        submodel_identifier (str):
        id_short_path (str):
        file_name (str):
        body (PutFileByPathBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Result]]
    """

    kwargs = _get_kwargs(
        submodel_identifier=submodel_identifier,
        id_short_path=id_short_path,
        body=body,
        file_name=file_name,
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
    body: PutFileByPathBody,
    file_name: str,
) -> Optional[Union[Any, Result]]:
    """Uploads file content to an existing submodel element at a specified path within submodel elements
    hierarchy

    Args:
        submodel_identifier (str):
        id_short_path (str):
        file_name (str):
        body (PutFileByPathBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Result]
    """

    return sync_detailed(
        submodel_identifier=submodel_identifier,
        id_short_path=id_short_path,
        client=client,
        body=body,
        file_name=file_name,
    ).parsed


async def asyncio_detailed(
    submodel_identifier: str,
    id_short_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutFileByPathBody,
    file_name: str,
) -> Response[Union[Any, Result]]:
    """Uploads file content to an existing submodel element at a specified path within submodel elements
    hierarchy

    Args:
        submodel_identifier (str):
        id_short_path (str):
        file_name (str):
        body (PutFileByPathBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Result]]
    """

    kwargs = _get_kwargs(
        submodel_identifier=submodel_identifier,
        id_short_path=id_short_path,
        body=body,
        file_name=file_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    submodel_identifier: str,
    id_short_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutFileByPathBody,
    file_name: str,
) -> Optional[Union[Any, Result]]:
    """Uploads file content to an existing submodel element at a specified path within submodel elements
    hierarchy

    Args:
        submodel_identifier (str):
        id_short_path (str):
        file_name (str):
        body (PutFileByPathBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Result]
    """

    return (
        await asyncio_detailed(
            submodel_identifier=submodel_identifier,
            id_short_path=id_short_path,
            client=client,
            body=body,
            file_name=file_name,
        )
    ).parsed
