import typing
import asyncio

if typing.TYPE_CHECKING:
    from ..client import Client

from ..core import Router

class ChannelAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client
        """The client."""

    async def channel_get(self, channel_id: str) -> dict:
        """
        Get a channel.

        Parameters
        ----------
        channel_id : `str`
            The id of the channel.

        Returns
        -------
        channel : `dict`
            The channel.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}', 'GET'))

    async def channel_delete(self, channel_id: str) -> dict:
        """
        Delete a channel.

        Parameters
        ----------
        channel_id : `str`
            The id of the channel.

        Returns
        -------
        channel : `dict`
            The channel.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}', 'DELETE'))

    async def channel_edit(self, channel_id: str, **data) -> dict:
        """
        Edit a channel.

        Parameters
        ----------
        channel_id : `str`
            The id of the channel.
        **data : `typing.Dict`
            The data that is used to edit the channel.

        Returns
        -------
        channel : `dict`
            The channel.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}', 'PATCH'), json=data)