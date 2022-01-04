import typing
import asyncio

if typing.TYPE_CHECKING:
    from ..client import Client

from ..core import Router
from ..models import User

class UserAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client
        """The client."""

    async def user_get(self, user_id: str):
        """
        Get a user.
        Parameters
        ----------
        user_id : `str`
            The id of the user.
        Returns
        -------
        user : `dict`
            The user.
        """
        res = await self.client.http.request(Router(f'/users/{user_id}', 'GET'))
        return User(res)

    async def user_edit(self, user_id: str, **data):
        """
        Edit a user.
        Parameters
        ----------
        user_id : `str`
            The id of the user.
        **data : `typing.Dict`
            The data that is used to edit the user.
        """
        await self.client.http.request(Router(f'/users/{user_id}', 'PATCH'), json=data)

    async def user_guild_leave(self, user_id: str, guild_id: str):
        """
        Leave a guild.
        Parameters
        ----------
        user_id : `str`
            The id of the user.
        guild_id : `str`
            The id of the guild.
        """
        await self.client.http.request(Router(f'/users/{user_id}/guilds/{guild_id}', 'DELETE'))