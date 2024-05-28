from abc import ABCMeta, abstractmethod
from .abc import HTTPClient
from collections.abc import AsyncIterator
from typing import Any, Optional
import aiohttp
from aiohttp.client import DEFAULT_TIMEOUT, ClientTimeout


class AiohttpClient(HTTPClient):
    """An aiohttp impl for HTTPClient"""
    def __init__(self, base_url: str, timeout: ClientTimeout = DEFAULT_TIMEOUT) -> None:
        _headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self._sess = aiohttp.ClientSession(
            base_url=base_url,
            headers=_headers,
            timeout=timeout,
            trust_env=True,
            raise_for_status=True
        )
        self._sess.trace_configs

    @property
    def headers(self):
        return self._sess.headers

    async def close(self):
        await self._sess.close()

    async def get(self, url: str):
        res = await self._sess.get(url)
        return await res.json()

    async def post(self, url: str, data: Optional[dict] = None):
        res = await self._sess.post(url, data=data)
        return await res.json()

    async def download(self, url: str, chunk_size: int) -> AsyncIterator[bytes]:
        res = await self._sess.get(url, allow_redirects=True)
        return res.content.iter_chunked(chunk_size)

    @property
    def session(self):
        return self._sess