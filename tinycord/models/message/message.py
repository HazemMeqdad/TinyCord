import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client

from ..mixins import Hashable
from ...utils import Snowflake
from ..user import User

@dataclasses.dataclass(repr=False)
class Message(Hashable):
    """
        This is the User it used to represent a user.

        Parameters
        ----------
        client : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the message.
            
    """
    def __init__(self, client: "Client", **data) -> None:
        self.client = client
        """The main client."""

        self.id: Snowflake = Snowflake(
            data.get('id'))
        """The ID of the message."""

        self.channel_id: Snowflake = Snowflake(
            data.get('channel_id'))

        self.guild_id: typing.Union[Snowflake, None] = Snowflake(
            data.get('guild_id'))
        """The guild id."""

        self.author: "User" = User(client, 
            **data.get('author'))
        """The author of the message."""

        self.content: str = data.get('content')
        """The content of the message."""

        self.timestamp: str = data.get('timestamp')
        """The timestamp of the message."""

        self.edited_timestamp: str = data.get('edited_timestamp')
        """The edited timestamp of the message."""

        self.tts: bool = data.get('tts')
        """Whether the message is TTS or not."""

        self.mention_everyone: bool = data.get('mention_everyone')
        """Whether the message mentions everyone or not."""

        self.mentions: typing.Union[typing.List[str], None] = data.get('mentions', [])
        """The mentions of the message."""

        self.mention_roles: typing.List = data.get('mention_roles')
        """The mention roles of the message."""

        self.mention_channels: typing.Union[typing.List[str], None] = data.get('mention_channels', [])
        """The mention channels of the message."""

        self.attachments: typing.List = data.get('attachments')
        """The attachments of the message."""

        self.embeds: typing.List = data.get('embeds')
        """The embeds of the message."""

        self.reactions: typing.List = data.get('reactions', [])
        """The reactions of the message."""

        self.nonce: typing.Union[int, str] = data.get('nonce', [])
        """The nonce of the message."""

        self.pinned: bool = data.get('pinned')
        """Whether the message is pinned or not."""

        self.webhook_id: typing.Union[Snowflake, None] = Snowflake(
            data.get('webhook_id'))
        """The webhook ID of the message."""

        self.type: int = data.get('type')
        """The type of the message."""

        self.activity: typing.Union[typing.Dict[str,str], None] = data.get('activity', {})
        """The activity of the message."""

        self.application: typing.Union[typing.Dict[str,str], None] = data.get('application', {})
        """The application of the message."""

        self.application_id: typing.Union[Snowflake, None] = Snowflake(
            data.get('application_id'))
        """The application ID of the message."""

        self.message_reference: typing.Union[typing.Dict[str,str], None] = data.get('message_reference', {})        
        """The message reference of the message."""

        self.flags: typing.List = data.get('flags', [])
        """The flags of the message."""
        
        self.interaction: typing.Union[int, None] = data.get('interaction_count', [])
        """The interaction of the message."""

        self.thread: typing.Dict[str, typing.Any] = data.get('thread', {})
        """The thread of the message."""
        
        self.components: typing.Dict[str, typing.Any] = data.get('components', {})
        """The components of the message."""
        
        self.sticker_items: typing.Dict[str, typing.Any] = data.get('sticker_items', {})
        """The sticker items of the message."""
        
        self.stickers: typing.Union[str, None] = data.get('stickers', [])
        """The stickers of the message."""