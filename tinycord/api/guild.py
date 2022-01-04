import typing
import asyncio

if typing.TYPE_CHECKING:
    from ..client import Client

from ..core import Router

class GuildAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client
        """The client."""

    async def guild_edit(self, guild_id: str, **data) -> dict:
        """
        Edit a guild.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        **data : `typing.Dict`
            The data that is used to edit the guild.

        Returns
        -------
        guild : `dict`
            The guild.
        """
        return await self.client.http.request(Router(f'/guilds/{guild_id}', 'PATCH'), json=data)

    async def guild_delete(self, guild_id: str) -> dict:
        """
        Delete a guild.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.

        Returns
        -------
        guild : `dict`
            The guild.
        """
        return await self.client.http.request(Router(f'/guilds/{guild_id}', 'DELETE'))