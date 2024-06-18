import os

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES: int = 360
    USER_SERVICE_URL: str = os.environ.get('USER_SERVICE_URL')
    TOOL_INTEGRATION_SERVICE_URL: str = os.environ.get('TOOL_INTEGRATION_SERVICE_URL')
    EMPLOYEE_SECURITY_SERVICE_URL: str = os.environ.get('EMPLOYEE_SECURITY_SERVICE_URL')
    GATEWAY_TIMEOUT: int = 59


settings = Settings()
