from typing import Any

from .exceptions import NoDataResponse
from .client import Client

class CurrencyMeta:
    def __init__(self, cmc_id: int):
        self.cmc_id = cmc_id

    async def update(self, client: Client):
        # 'async with' raises AttributeError: __aenter__
        r = await client.get(
            endpoint="/v2/cryptocurrency/info",
            params={'id': self.cmc_id},
            close=True
        )

        try:
            self.data = r['data'][str(self.cmc_id)]
        except KeyError:
            raise NoDataResponse(status=r['status'])
        
    def __getattr__(self, __name: str) -> Any:
        return self.data[__name]

class Currency:
    def __init__(self, cmc_id: int):
        self.meta = CurrencyMeta(cmc_id)
        self.cmc_id = cmc_id

    async def update(self, client: Client):
        # 'async with' raises AttributeError: __aenter__
        r = await client.get(
            endpoint="/v2/cryptocurrency/quotes/latest",
            params={'id': self.cmc_id}
        )
        await self.meta.update(client)

        try:
            self.data = r['data'][str(self.cmc_id)]
        except KeyError:
            raise NoDataResponse(status=r['status'])

    def __getattr__(self, __name: str) -> Any:
        return self.data[__name]

class CurrenciesList:
    def __init__(self, cmc_ids: list):
        self.currencies: list = []

        for cmc_id in cmc_ids:
            self.currencies.append(Currency(cmc_id))

    async def update(self, api_key: str):
        for currency in self.currencies:
            client = Client(api_key)
            await currency.update(client)
    
    def __getitem__(self, c_list_id: int):
        return self.currencies[c_list_id]