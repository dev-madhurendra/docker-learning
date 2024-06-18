import aiohttp
import async_timeout
import logging

from config.apigateway_config import settings

async def make_request(
    url: str,
    method: str,
    data: dict = None,
    headers: dict = None
):
    if not data:
        data = {}

    try:
        with async_timeout.timeout(settings.GATEWAY_TIMEOUT):
            async with aiohttp.ClientSession() as session:
                request = getattr(session, method)
                async with request(url, json=data, headers=headers) as response:
                    response_data = await response.json()
                    return response_data, response.status
    except aiohttp.ClientConnectorError as e:
        logging.error(f"Connection Error: Unable to connect to the service. Error: {e}")
        raise
    except aiohttp.ContentTypeError as e:
        logging.error(f"Content Type Error: Response content is not valid JSON. Error: {e}")
        raise
