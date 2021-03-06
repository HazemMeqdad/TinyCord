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
    def __init__(self, client: "Client", guild_id: Snowflake, **data) -> None:
        self.bitrate: int = data.get('bitrate')
        """The bitrate of the channel."""

        self.user_limit: int = data.get('user_limit')
        """The user limit of the channel."""
        
        self.rtc_region: str = data.get('rtc_region')
        """The region of the channel."""

        super().__init__(client, guild_id, **data)
        """The base channel."""

    async def connect(self, self_mute: bool = False, self_deaf: bool = True) -> None:
        """
            This function is used to connect to the voice channel.

            Parameters
            ----------
            gateway : `Gateway`
                The gateway to connect to.
        """
        await self.guild.shard.voice_connect(self.guild_id, self.id, self_mute, self_deaf)

    async def disconnect(self) -> None:
        """
            This function is used to disconnect from the voice channel.
        """
        await self.guild.shard.voice_disconnect(self.guild_id)
