import typing

if typing.TYPE_CHECKING:
    from ....client import Client

from ...guild import Emoji
from ....utils import Snowflake

class ReactionGateway:
    def __init__(self, client: "Client" , **data) -> None:
        self.client = client
        """The main client."""
        
        self.guild_id = Snowflake( data.get('guild_id'))
        """The guild id."""

        self.channel_id = data.get('channel_id',None)
        """The channel id."""

        self.message_id = data.get('message_id',None)
        """The message id."""

        self.user_id = data.get('user_id',None)
        """The user id."""

        self.emoji = data.get('emoji')
        """The emoji."""