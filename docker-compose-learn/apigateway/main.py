from ast import Dict
from fastapi import FastAPI, status, Request, Response

from config.apigateway_config import settings
from core.apigateway_core import route

app = FastAPI()

@route(
    request_method=app.get,
    path='/api/users',
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.USER_SERVICE_URL,
    authentication_required=False,
    response_model='datastructures.users.User',
    response_list=True,
)
async def get_users(request: Request, response: Response):
    pass

@route(
    request_method=app.get,
    path='/api/tools',
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.TOOL_INTEGRATION_SERVICE_URL,
    authentication_required=False,
    response_model='datastructures.tools.Tool',
    response_list=True,
)
async def get_tools(request: Request, response: Response):
    pass

@route(
    request_method=app.get,
    path='/api/employees',
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.EMPLOYEE_SECURITY_SERVICE_URL,
    authentication_required=False,
    response_model='datastructures.employees.Employee',
    response_list=True,
)
async def get_employees(request: Request, response: Response):
    pass

