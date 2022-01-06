import typing

if typing.TYPE_CHECKING:
    from ..client import Client

from ..core import Router
from ..models import *
from .utils import reason as _reason

class GuildAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client
        """The client."""

    async def guild_get(self, guild_id: str):
        """
        Get a guild.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.

        Returns
        -------
        guild : `dict`
            The guild.
        """
        res =  await self.client.http.request(Router(f'/guilds/{guild_id}', 'GET'))
        return Guild(res)

    async def guild_edit(self, guild_id: str, reason: str = None , **data):
        """
        Edit a guild.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        **data : `typing.Dict`
            The data that is used to edit the guild.

        """
        await self.client.http.request(Router(f'/guilds/{guild_id}', 'PATCH'), json=data,
            headers=_reason(reason))

    async def guild_delete(self, guild_id: str):
        """
        Delete a guild.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.

        """
        await self.client.http.request(Router(f'/guilds/{guild_id}', 'DELETE'))

    async def guild_create_channel(self, guild_id: str, reason: str = None , **data):
        """
        Create a channel.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        **data : `typing.Dict`
            The data that is used to create the channel.

        """
        res = await self.client.http.request(Router(f'/guilds/{guild_id}/channels', 'POST'), json=data,
            headers=_reason(reason))

        return deserialize_channel(self.client, guild_id, res)

    async def guild_get_channels(self, guild_id: str):
        """
        Get channels.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.

        """
        res =  await self.client.http.request(Router(f'/guilds/{guild_id}/channels', 'GET'))

        return [deserialize_channel(self.client, guild_id, channel) for channel in res]
        
    async def guild_get_roles(self, guild_id: str):
        """
        Get roles.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.

        """
        res =  await self.client.http.request(Router(f'/guilds/{guild_id}/roles', 'GET'))

        return [Role(self.client, guild_id, role) for role in res]

    async def guild_get_members(self, guild_id: str):
        """
        Get members.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.

        """
        res =  await self.client.http.request(Router(f'/guilds/{guild_id}/members', 'GET'))

        return [Member(self.client, guild_id, member) for member in res]

    async def guild_member_edit(self, guild_id: str, user_id: str, reason: str = None , **data):
        """
        Edit a member.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        user_id : `str`
            The id of the user.
        **data : `typing.Dict`
            The data that is used to edit the member.

        """
        res = await self.client.http.request(Router(f'/guilds/{guild_id}/members/{user_id}', 'PATCH'), json=data,
            headers=_reason(reason))

        return Member(self.client, guild_id, res)

    async def guild_member_add_role(self, guild_id: str, user_id: str, role_id: str, reason: str = None):
        """
        Add a role to a member.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        user_id : `str`
            The id of the user.
        role_id : `str`
            The id of the role.
        reason : `str`
            The reason for the action.

        """
        await self.client.http.request(Router(f'/guilds/{guild_id}/members/{user_id}/roles/{role_id}', 'PUT'),
            headers=_reason(reason))

    async def guild_member_delete_role(self, guild_id: str, user_id: str, role_id: str, reason: str = None):
        """
        Delete a role from a member.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        user_id : `str`
            The id of the user.
        role_id : `str`
            The id of the role.
        reason : `str`
            The reason for the action.

        """
        await self.client.http.request(Router(f'/guilds/{guild_id}/members/{user_id}/roles/{role_id}', 'DELETE'),
            headers=_reason(reason))

    async def guild_get_bans(self, guild_id: str):
        """
        Get bans.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.

        """
        res =  await self.client.http.request(Router(f'/guilds/{guild_id}/bans', 'GET'))

        return {user['user']['id']: [User(self.client, user['user']), user['reason']] for user in res}

    async def guild_ban_member(self, guild_id: str, user_id: str, delete_message_days: int = None , reason: str = None):
        """
        Ban a member.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        user_id : `str`
            The id of the user.
        reason : `str`
            The reason for the action.

        """
        await self.client.http.request(Router(f'/guilds/{guild_id}/bans/{user_id}', 'PUT'), 
            json={'delete_message_days': delete_message_days},
            headers=_reason(reason))

    async def guild_kick_member(self, guild_id: str, user_id: str, reason: str = None):
        """
        Kick a member.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        user_id : `str`
            The id of the user.
        reason : `str`
            The reason for the action.

        """
        await self.client.http.request(Router(f'/guilds/{guild_id}/members/{user_id}', 'DELETE'),
            headers=_reason(reason))

    async def guild_get_ban(self, guild_id: str, user_id: str):
        """
        Get ban.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        user_id : `str`
            The id of the user.

        """
        res =  await self.client.http.request(Router(f'/guilds/{guild_id}/bans/{user_id}', 'GET'))

        return [ [User(self.client, res['user']), res['reason']] ]

    async def guild_unban(self, guild_id: str, user_id: str, reason: str = None):
        """
        Unban a member.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        user_id : `str`
            The id of the user.
        reason : `str`
            The reason for the action.

        """
        await self.client.http.request(Router(f'/guilds/{guild_id}/bans/{user_id}', 'DELETE'),
            headers=_reason(reason))

    async def guild_create_role(self, guild_id: str, reason: str = None , **data):
        """
        Create a role.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        **data : `typing.Dict`
            The data that is used to create the role.

        """
        res = await self.client.http.request(Router(f'/guilds/{guild_id}/roles', 'POST'), json=data,
            headers=_reason(reason))

        return Role(self.client, guild_id, res)

    async def guild_delete_role(self, guild_id: str, role_id: str):
        """
        Delete a role.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        role_id : `str`
            The id of the role.

        """
        await self.client.http.request(Router(f'/guilds/{guild_id}/roles/{role_id}', 'DELETE'))

    async def guild_edit_role(self, guild_id: str, role_id: str, reason: str = None , **data):
        """
        Edit a role.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        role_id : `str`
            The id of the role.
        **data : `typing.Dict`
            The data that is used to edit the role.

        """
        res = await self.client.http.request(Router(f'/guilds/{guild_id}/roles/{role_id}', 'PATCH'), json=data,
            headers=_reason(reason))

        return Role(self.client, guild_id, res)

    async def guild_get_role(self, guild_id: str, role_id: str):
        """
        Get a role.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        role_id : `str`
            The id of the role.

        """
        res =  await self.client.http.request(Router(f'/guilds/{guild_id}/roles/{role_id}', 'GET'))

        return Role(self.client, guild_id, res)

    async def guild_create_emoji(self, guild_id: str, reason: str = None , **data):
        """
        Create an emoji.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        **data : `typing.Dict`
            The data that is used to create the emoji.

        """
        res = await self.client.http.request(Router(f'/guilds/{guild_id}/emojis', 'POST'), json=data,
            headers=_reason(reason))

        return Emoji(self.client, guild_id, res)

    async def guild_delete_emoji(self, guild_id: str, emoji_id: str):
        """
        Delete an emoji.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        emoji_id : `str`
            The id of the emoji.

        """
        await self.client.http.request(Router(f'/guilds/{guild_id}/emojis/{emoji_id}', 'DELETE'))

    async def guild_create_sticker(self, guild_id: str, reason: str = None , **data):
        """
        Create a sticker.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        **data : `typing.Dict`
            The data that is used to create the sticker.

        """
        res = await self.client.http.request(Router(f'/guilds/{guild_id}/stickers', 'POST'), json=data,
            headers=_reason(reason))

        return Sticker(self.client, guild_id, res)

    async def guild_delete_sticker(self, guild_id: str, sticker_id: str):
        """
        Delete a sticker.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        sticker_id : `str`
            The id of the sticker.

        """
        await self.client.http.request(Router(f'/guilds/{guild_id}/stickers/{sticker_id}', 'DELETE'))

    async def guild_edit_sticker(self, guild_id: str, sticker_id: str, reason: str = None , **data):
        """
        Edit a sticker.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        sticker_id : `str`
            The id of the sticker.
        **data : `typing.Dict`
            The data that is used to edit the sticker.

        """
        res = await self.client.http.request(Router(f'/guilds/{guild_id}/stickers/{sticker_id}', 'PATCH'), json=data,
            headers=_reason(reason))

        return Sticker(self.client, guild_id, res)

    async def guild_edit_emoji(self, guild_id: str, emoji_id: str, reason: str = None , **data):
        """
        Edit an emoji.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        emoji_id : `str`
            The id of the emoji.
        **data : `typing.Dict`
            The data that is used to edit the emoji.

        """
        res = await self.client.http.request(Router(f'/guilds/{guild_id}/emojis/{emoji_id}', 'PATCH'), json=data,
            headers=_reason(reason))

        return Emoji(self.client, guild_id, res)

    async def guild_template_create(self, guild_id: str, name: str, description: str = None):
        """
        Create a guild template.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        name : `str`
            The name of the template.
        description : `str`
            The description of the template.
        """

        await self.client.http.request(Router(f'/guilds/{guild_id}/templates', 'POST'), json={'name': name, 'description': description})

    async def guild_template_delete(self, guild_id: str, template_id: str):
        """
        Delete a guild template.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        template_id : `str`
            The id of the template.
        """

        await self.client.http.request(Router(f'/guilds/{guild_id}/templates/{template_id}', 'DELETE'))

    async def guild_template_edit(self, guild_id: str, template_id: str, name: str, description: str = None):
        """
        Edit a guild template.

        Parameters
        ----------
        guild_id : `str`
            The id of the guild.
        template_id : `str`
            The id of the template.
        name : `str`
            The name of the template.
        description : `str`
            the description of the template.
        """

        await self.client.http.request(Router(f'/guilds/{guild_id}/templates/{template_id}', 'PATCH'), json={'name': name, 'description': description})