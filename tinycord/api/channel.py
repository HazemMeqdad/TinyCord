import typing
import json

if typing.TYPE_CHECKING:
    from ..client import Client

from ..models import *
from ..core import Router
from .utils import reason as _reason

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

    async def channel_delete(self, channel_id: str, reason: str = None) -> dict:
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
        return await self.client.http.request(Router(f'/channels/{channel_id}', 'DELETE'),
            headers=_reason(reason))

    async def channel_edit(self, channel_id: str, reason: str = None , **data) -> dict:
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
        return await self.client.http.request(Router(f'/channels/{channel_id}', 'PATCH'), json=data,
            headers=_reason(reason))

    async def channel_start_typing(self, channel_id: str) -> dict:
        """
        Start typing in a channel.

        Returns
        -------
        typing : `dict`
            The typing.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}/typing', 'POST'))

    async def channel_messages_list(self, channel_id: str) -> typing.List["Message"]:
        """
        Get a list of messages.

        Returns
        -------
        messages : `list`
            The messages.
        """
        res =  await self.client.http.request(Router(f'/channels/{channel_id}/messages', 'GET'))

        return [Message(self.client, message) for message in res]

    async def channel_messages_get(self, channel_id: str, message_id: str) -> "Message":
        """
        Get a message.

        Returns
        -------
        message : `dict`
            The message.
        """
        res =  await self.client.http.request(Router(f'/channels/{channel_id}/messages/{message_id}', 'GET'))
        
        return Message(self.client, res)

    async def channel_messages_create(self, channel_id: str, **data) -> "Message":
        """
        Create a message.

        Returns
        -------
        message : `dict`
            The message.
        """

        res =  await self.client.http.request(
            Router(f'/channels/{channel_id}/messages', 'POST'), 
            data=json.dumps({'payload_json': json.dumps(data),'files': data.get('files', [])}), 
            headers={'Content-Type': 'application/json'}
        )

        res.update({'guild_id': data.get('guild_id', None)})
        
        return Message(self.client, **res)

    async def channel_messages_delete(self, channel_id: str, message_id: str, reason: str = None):
        """
        Delete a message.

        Returns
        -------
        message : `dict`
            The message.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}/messages/{message_id}', 'DELETE'), 
            headers=_reason(reason))

    async def channel_messages_bulk_delete(self, channel_id: str, message_ids: typing.List[str], reason: str = None):
        """
        Bulk delete messages.

        Returns
        -------
        message : `dict`
            The message.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}/messages/bulk-delete', 'POST'), json=message_ids,
            headers=_reason(reason))

    async def channel_messages_edit(self, channel_id: str, message_id: str, reason: str = None, **data):
        """
        Edit a message.

        Returns
        -------
        message : `dict`
            The message.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}/messages/{message_id}', 'PATCH'), json=data,
            headers=_reason(reason))

    async def channel_messages_pin(self, channel_id: str, message_id: str, reason: str = None):
        """
        Pin a message.

        Returns
        -------
        message : `dict`
            The message.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}/messages/{message_id}/pin', 'PUT'),
            headers=_reason(reason))
    
    async def channel_messages_unpin(self, channel_id: str, message_id: str, reason: str = None):
        """
        Unpin a message.

        Returns
        -------
        message : `dict`
            The message.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}/messages/{message_id}/pin', 'DELETE'),
            headers=_reason(reason))

    async def channel_messages_reactions_get(self, channel_id: str, message_id: str, emoji: "Emoji"):
        """
        Get a message's reactions.

        Returns
        -------
        message : `dict`
            The message.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}/messages/{message_id}/reactions/{emoji.name}:{emoji.id}', 'GET'))

    async def channel_messages_reactions_create_me(self, channel_id: str, message_id: str, emoji: "Emoji"):
        """
        Create a reaction.

        Returns
        -------
        message : `dict`
            The message.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}/messages/{message_id}/reactions/{emoji.name}:{emoji.id}/@me', 'PUT'))

    async def channel_messages_reactions_delete_me(self, channel_id: str, message_id: str, emoji: "Emoji", reason: str = None):
        """
        Delete a reaction.

        Returns
        -------
        message : `dict`
            The message.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}/messages/{message_id}/reactions/{emoji.name}:{emoji.id}/@me', 'DELETE'),
            headers=_reason(reason))

    async def channel_messages_reactions_delete(self, channel_id: str, message_id: str, emoji: "Emoji", user_id: str, reason: str = None):
        """
        Delete a reaction.

        Returns
        -------
        message : `dict`
            The message.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}/messages/{message_id}/reactions/{emoji.name}:{emoji.id}/{user_id}', 'DELETE'),
            headers=_reason(reason))

    async def channel_messages_reactions_delete_all(self, channel_id: str, message_id: str, emoji: "Emoji", reason: str = None):
        """
        Delete all reactions.

        Returns
        -------
        message : `dict`
            The message.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}/messages/{message_id}/reactions/{emoji.name}:{emoji.id}', 'DELETE'),
            headers=_reason(reason))

    async def channel_messages_reactions_list(self, channel_id: str, message_id: str):
        """
        Get a message's reactions.

        Returns
        -------
        message : `dict`
            The message.
        """
        res =  await self.client.http.request(Router(f'/channels/{channel_id}/messages/{message_id}/reactions', 'GET'))

        return [Reaction(self.client, reaction) for reaction in res]

    async def channel_edit_permission(self, channel_id: str, overwrite_id: str, reason: str = None , **data):
        """
        Edit a channel permission.

        Returns
        -------
        overwrite : `dict`
            The overwrite.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}/permissions/{overwrite_id}', 'PUT'), json=data,
            reason=_reason(reason))

    async def channel_delete_permission(self, channel_id: str, overwrite_id: str, reason: str = None):
        """
        Delete a channel permission.

        Returns
        -------
        overwrite : `dict`
            The overwrite.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}/permissions/{overwrite_id}', 'DELETE'),
            reason=_reason(reason))

    async def channel_invite_create(self, channel_id: str, **data):
        """
        Create an invite.

        Returns
        -------
        invite : `dict`
            The invite.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}/invites', 'POST'), json=data)

    async def channel_invite_delete(self, channel_id: str, invite_code: str):
        """
        Delete an invite.

        Returns
        -------
        invite : `dict`
            The invite.
        """
        return await self.client.http.request(Router(f'/channels/{channel_id}/invites/{invite_code}', 'DELETE'))

    async def channel_invite_list(self, channel_id: str):
        """
        Get a channel's invites.

        Returns
        -------
        invites : `list`
            The invites.
        """
        res =  await self.client.http.request(Router(f'/channels/{channel_id}/invites', 'GET'))

        return [Invite(self.client, invite) for invite in res]

    async def create_dm(self, recipient_id: str):
        """
        Create a direct message channel.

        Returns
        -------
        channel : `dict`
            The channel.
        """
        return await self.client.http.request(Router('/users/@me/channels', 'POST'), json={"recipient_id": recipient_id})

    async def thread_join(self, thread_id: str):
        """
        Join a thread.

        Returns
        -------
        thread : `dict`
            The thread.
        """
        return await self.client.http.request(Router(f'/channels/{thread_id}/thread-members/@me', 'PUT'))

    async def thread_leave(self, thread_id: str):
        """
        Leave a thread.

        Returns
        -------
        thread : `dict`
            The thread.
        """
        return await self.client.http.request(Router(f'/channels/{thread_id}/thread-members/@me', 'DELETE'))