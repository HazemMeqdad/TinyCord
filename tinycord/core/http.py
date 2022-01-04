import typing
import aiohttp
import asyncio
import sys

if typing.TYPE_CHECKING:
    from ..client import Client

from .router import Router

class HTTPClient:
    """
        The following functions are used to make requests to the gateway.
        They handle ratelimits and other errors. The way this works is that
        The client will try to make a request. If it fails, it will check if
        the error is a ratelimit. If it is, it will wait for the ratelimit
        to expire and then try again.
        
        Parameters
        ----------
        client: `Client`
            The client that is making the request.
    """
    def __init__(self, client: "Client") -> None:
        self.client = client
        """ The client that is making the request. """

        self.session = aiohttp.ClientSession()
        """ The session that is used to make the request. """

        self.loop = asyncio.get_event_loop()
        """ The event loop that is used to make the request. """

        self.headers = {
            'Authorization': self.client.token,
        }
        """ The headers that are used to make the request. """

        self.lock = asyncio.Lock(
           **({"loop": self.loop} if sys.version_info[:2] < (3, 8) else {})
        )
        """ The lock that is used to make the request. """

    async def request(self, route: "Router", **kwargs):
        """
            This function is used to make a request to the gateway.

            Parameters
            ----------
            url: `str`
                The url to make the request to.
            method: `str`
                The method to use.
        """
        if 'headers' in kwargs and kwargs['headers']:
            for k, v in kwargs['headers'].items():
                self.headers[k] = v

        response = await self.session.request(
            url=route.path,
            method=route.method,
            
            headers=self.headers,

            **kwargs
        )

        if response.status == 429:
            retry_after = response.headers.get('Retry-After')

            async with self.lock.acquire():
                
                await self.ratelimit(float(retry_after), route, **kwargs)
            
            self.lock.release()

        return await response.json()

    async def ratelimit(self, retry_after: float, route: "Router", **kwargs):
        """
            This function is used to handle ratelimits.

            Parameters
            ----------
            retry_after: `float`
                The amount of time to wait before trying again.
        """
        await asyncio.sleep(retry_after if type(retry_after) == float else float(retry_after))

        return await self.request(
            route,
            **kwargs,
        )