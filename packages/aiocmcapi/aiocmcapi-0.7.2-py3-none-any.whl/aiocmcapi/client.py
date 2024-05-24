from aiohttp import ClientSession

from .exceptions import EndpointNotFound

class BaseClient:
    def __init__(self, api_key: str):
        self._session = ClientSession(
            base_url="http://pro-api.coinmarketcap.com",
            headers={
                "X-CMC_PRO_API_KEY": api_key
            }
        )
    
    async def close_session(self):
        await self._session.connector.close()
        await self._session.close()

class Client(BaseClient):
    async def get(
        self,
        endpoint: str,
        params: dict = None,
        close: bool = False
    ) -> dict:
        async with self._session.get(
            url=endpoint,
            params=params
        ) as r:
            json = await r.json()
            if close:
                await self.close_session()
            
            try:
                if json['statusCode'] == 404:
                    await self.close_session()
                    raise EndpointNotFound(endpoint)
            except KeyError:
                return json