from .abc import HTTPClient
from .aiohttp_client import AiohttpClient # Default client
from ..types import endpoint, GET, POST, DOWNLOAD
from collections.abc import AsyncIterator
from typing import Any, Awaitable, Optional
from urllib.parse import urlencode # For encoding queries

class CurseHTTP:
    def __init__(self, api_key: str, client: HTTPClient = AiohttpClient):
        base_url = "https://api.curseforge.com"
        self._client = client(base_url=base_url)
        self._headers = self._client.headers
        self._headers.add('x-api-key', api_key)
    
    async def get(self, endpoint: str):
        return await self._client.get(endpoint)

    async def post(self, endpoint: str, data: dict):
        return await self._client.post(endpoint, data=data)

    async def download(self, endpoint: str, chunk_size: int) -> AsyncIterator:
        return await self._client.download(endpoint)

    async def close(self):
        await self._client.close()

    async def api(
        self,
        endpoint: endpoint,
        data: Optional[object] = None,
        params: Optional[dict] = None,
        query: Optional[dict] = None,
        chunk_size: Optional[int] = None):

        """
        Calls base curseforge url + endpoint.endpoint_url with endpoint.method (POST, GET, DOWNLOAD)
        Constructs queries from query dict and passes parameters (if POST)

        :param endpoint:  Endpoint class with `endpoint` string, request method and endpoint description inside it. Predefined in `endpoints` variable.
        :param data: Data sent to server, POST only. (cf_post)
        :param params: `!!MANDATORY!!` Params to substitute in endpoint string
        :param query: Url query
        """

        method = endpoint.method
        endpoint = endpoint.endpoint
        if query:
            query = urlencode(query)
        if params:
            endpoint = endpoint.format(**params)
        endpoint = endpoint + query
        if method == GET:
            return(await self.get(endpoint))
        if method == POST:
            return(await self.post(endpoint, data))
        if method == DOWNLOAD:
            return(await self.download(endpoint, chunk_size))
