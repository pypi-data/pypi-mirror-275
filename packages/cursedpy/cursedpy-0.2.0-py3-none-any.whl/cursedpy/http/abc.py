from abc import ABCMeta, abstractmethod
from collections.abc import AsyncIterator
from typing import Any, Optional
import aiohttp
from aiohttp.client import DEFAULT_TIMEOUT, ClientTimeout


# Thx, https://github.com/Stinky-c/curse-api <3, i didn't even know about abstract classes in python before this moment
# Mb one time i should read PEP
# I probably should have a way to add new http libraryes, yeah..
# HTTPX sucks
class HTTPClient(metaclass=ABCMeta):
    """required types"""

    def __init__(self, api_key: str, base_url: str) -> None:
        ...

    @property
    def headers(self):
        ...

    @abstractmethod
    async def close(self):
        ...

    @abstractmethod
    async def get(self, url: str):
        ...

    @abstractmethod
    async def post(self, url: str, data: Optional[dict] = None):
        ...

    @abstractmethod
    async def download(self, url: str, chunk_size: int) -> AsyncIterator[bytes]:
        ...