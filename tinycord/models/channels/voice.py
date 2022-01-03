import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client

from .channel import BaseChannel
from ..mixins import Hashable
from ...utils import Snowflake

@dataclasses.dataclass(repr=False)
class VoiceChannel(BaseChannel,Hashable):
    """
        This is the VoiceChannel it used to represent a voice channel.

        Parameters
        ----------
        client : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the channel.

        Attributes
        ----------
        bitrate : `int`
            The bitrate of the channel.
        user_limit : `int`
            The user limit of the channel.
        rtc_region : `str`
            The region of the channel.
    """
    def __init__(self, client: "Client", guild_id: Snowflake , **data) -> None:
        self.bitrate: int = data.get('bitrate')
        """The bitrate of the channel."""

        self.user_limit: int = data.get('user_limit')
        """The user limit of the channel."""
        
        self.rtc_region: str = data.get('rtc_region')
        """The region of the channel."""

        super().__init__(client, guild_id, **data)
        """The base channel."""

    async def connect(self, muted: bool = False, deafed: bool = True) -> None:
        """
            |coro|
            Connects to the voice channel.

            Parameters
            ----------
            muted : `bool`
                Whether the bot should be muted or not.
            deafed : `bool`
                Whether the bot should be deafed or not.
        """
        
        await self.client.gw.send(4, {
            'guild_id': self.guild_id,
            'channel_id': self.id,
            'self_mute': muted,
            'self_deaf': deafed,
        })

    async def disconnect(self) -> None:
        """
            |coro|
            Disconnects from the voice channel.
        """

        await self.client.gw.send(4, {
            'guild_id': self.guild_id,
            'channel_id': None,
            'self_mute': False,
            'self_deaf': False,
        })
        