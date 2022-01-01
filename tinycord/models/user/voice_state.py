import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client

from ..mixins import Hashable
from ...utils import Snowflake

@dataclasses.dataclass(repr=False)
class Voicestate:
    """
        This is the VoiceState it used to represent a voice state.

        Parameters
        ----------
        client : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the voice state.

        Attributes
        ----------
        guild_id : `typing.Union[Snowflake, None]`
            The guild id.
        channel_id : `typing.Union[Snowflake, None]`
            The channel id.
        user_id : `Snowflake`
            The user id.
        session_id : `str`
            The session id.
        deaf : `bool`
            Whether the user is deafened or not.
        mute : `bool`
            Whether the user is muted or not.
        self_deaf : `bool`
            Whether the user is self deafened or not.
        self_mute : `bool`
            Whether the user is self muted or not.
        self_stream : `typing.Union[bool, None]`
            Whether the user is streaming or not.
        self_video : `bool`
            Whether the user is broadcasting or not.
        suppress : `bool`
            Whether the user is suppressed or not.
        request_to_speak_timestamp : `typing.Union[int, None]`
            The timestamp of when the user requested to speak.
    """
    def __init__(self, client: "Client", **data) -> None:
        self.client = client
        """The main client."""
        
        self.guild_id: typing.Union[Snowflake, None] = data.get('guild_id')
        """The guild id."""

        self.channel_id: typing.Union[Snowflake, None] = data.get('channel_id')
        """The channel id."""

        self.user_id: Snowflake = data.get('user_id')
        """The user id."""

        self.session_id: str = data.get('session_id')
        """The session id."""

        self.deaf: bool = data.get('deaf')
        """Whether the user is deafened or not."""

        self.mute: bool = data.get('mute')
        """Whether the user is muted or not."""

        self.self_deaf: bool = data.get('self_deaf')
        """Whether the user is self deafened or not."""

        self.self_mute: bool = data.get('self_mute')
        """Whether the user is self muted or not."""

        self.self_stream: typing.Union[bool, None] = data.get('self_stream')
        """Whether the user is streaming or not."""

        self.self_video: bool = data.get('self_video')
        """Whether the user is broadcasting or not."""

        self.suppress: bool = data.get('suppress')
        """Whether the user is suppressed or not."""
        
        self.request_to_speak_timestamp: typing.Union[int, None] = data.get('request_to_speak_timestamp')
        """The timestamp of when the user requested to speak."""