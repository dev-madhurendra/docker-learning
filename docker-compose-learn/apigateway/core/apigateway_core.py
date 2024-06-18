import aiohttp
import functools
from importlib import import_module
from fastapi import Request, Response, HTTPException, status
from typing import List
from connect_services.apigateway_network import make_request

def route(
    request_method, 
    path: str, 
    status_code: int,
    payload_key: str, 
    service_url: str,
    authentication_required: bool = False,
    response_model: str = None,
    response_list: bool = False
):
    if response_model:
        response_model = import_function(response_model)
        if response_list:
            response_model = List[response_model]

    app_any = request_method(
        path, 
        status_code=status_code,
        response_model=response_model
    )

    def wrapper(f):
        @app_any
        @functools.wraps(f)
        async def inner(request: Request, response: Response, **kwargs):
            service_headers = {}

            if authentication_required:
                pass

            scope = request.scope

            method = scope['method'].lower()
            path = scope['path']
            payload_obj = kwargs.get(payload_key)
            payload = payload_obj.dict() if payload_obj else {}

            url = f'{service_url}{path}'

            try:
                resp_data, status_code_from_service = await make_request(
                    url=url,
                    method=method,
                    data=payload,
                    headers=service_headers,
                )
            except aiohttp.client_exceptions.ClientConnectorError:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail='Service is unavailable.',
                    headers={'WWW-Authenticate': 'Bearer'},
                )
            except aiohttp.client_exceptions.ContentTypeError:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail='Service error.',
                    headers={'WWW-Authenticate': 'Bearer'},
                )

            response.status_code = status_code_from_service

            return resp_data

    return wrapper


def import_function(method_path):
    module, method = method_path.rsplit('.', 1)
    mod = import_module(module)
    return getattr(mod, method, lambda *args, **kwargs: None)
