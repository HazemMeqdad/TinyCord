import typing
import aiohttp
import asyncio

if typing.TYPE_CHECKING:
    from ..client import Client

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

        self.headers = {
            'Authorization': self.client.token,
        }
        """ The headers that are used to make the request. """

    async def request(self, url: str , method: str, **kwargs):
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

        url = f'https://discord.com/api/v9{url}'

        response = await self.session.request(
            method,
            url,
            headers=self.headers,
            **kwargs
        )

        if response.status == 429:
            await self.ratelimit(response.headers['Retry-After'], url, method, **kwargs)

        return await response.json()

    async def ratelimit(self, retry_after: float, url: str, method: str, **kwargs):
        """
            This function is used to handle ratelimits.

            Parameters
            ----------
            retry_after: `float`
                The amount of time to wait before trying again.
        """
        await asyncio.sleep(retry_after if type(retry_after) == float else float(retry_after))

        return await self.request(
            url=url,
            method=method,
            **kwargs,
        )