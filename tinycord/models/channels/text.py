import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client

from .channel import BaseChannel
from ..message import Message
from ..mixins import Hashable
from ...utils import Snowflake

@dataclasses.dataclass(repr=False)
class TextChannel(BaseChannel,Hashable):
    """
        This is the TextChannel it used to represent a text channel.

        Parameters
        ----------
        client : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the channel.

        Attributes
        ----------
        topic : `str`
            The topic of the channel.
        last_message_id : `Snowflake`
            The ID of the last message.
        last_pin_timestamp : `str`
            The timestamp of the last pin.
        rate_limit_per_user : `int`
            The rate limit per user.
        nsfw : `bool`
            Whether the channel is nsfw or not.
        parent_id : `Snowflake`
            The ID of the parent channel.
        last_pin_timestamp : `str`
            The timestamp of the last pin.
    """
    def __init__(self, client: "Client", guild_id: Snowflake , **data) -> None:
        self.topic: str = data.get('topic')
        """The topic of the channel."""

        self.last_message_id: Snowflake = Snowflake(
            data.get('last_message_id'))
        """The ID of the last message."""

        self.last_pin_timestamp: str = data.get('last_pin_timestamp')
        """The timestamp of the last pin."""

        self.rate_limit_per_user: int = data.get('rate_limit_per_user')
        """The rate limit per user."""

        self.nsfw: bool = data.get('nsfw')
        """Whether the channel is nsfw or not."""

        self.parent_id: Snowflake = Snowflake(
            data.get('parent_id'))
        """The ID of the parent channel."""

        self.last_pin_timestamp: str = data.get('last_pin_timestamp')
        """The timestamp of the last pin."""

        super().__init__(client, guild_id, **data)
        """The base channel."""

    async def send(self, content: str, **kwargs) -> "Message":
        """
            This is used to send a message to the channel.

            Parameters
            ----------
            content : `str`
                The content of the message.

            Returns
            -------
            `Message`
                The message that was sent.
        """

        kwargs.update({'content': content})
        kwargs.update({'guild_id': self.guild_id})

        return await self.client.api.channel_messages_create(
            self.id, **kwargs)