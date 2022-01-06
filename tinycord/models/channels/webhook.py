import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client

from ..user import User
from ..mixins import Hashable
from ...utils import Snowflake

@dataclasses.dataclass(repr=False)
class Webhook(Hashable):
    """
        This is the VoiceChannel it used to represent a voice channel.

        Parameters
        ----------
        client : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the channel.

    """
    def __init__(self, client: "Client", guild_id: Snowflake, **data) -> None:
        self.id: int = Snowflake(
            data.get('id'))
        """The ID of the webhook."""

        self.type: int = data.get('type')
        """The type of the webhook."""

        self.guild_id: int = Snowflake(
            data.get('guild_id'))
        """The guild id of the webhook."""

        self.channel_id: int = Snowflake(
            data.get('channel_id'))
        """The channel id of the webhook."""

        self.user: typing.Union[None, 'User'] = (User(client, **data.get('user')) if 
            'user' in data else None)
        """The user of the webhook."""

        self.name: str = data.get('name')
        """The name of the webhook."""

        self.avatar: typing.Union[None, str] = data.get('avatar')
        """The avatar of the webhook."""

        self.token: typing.Union[None, str] = data.get('token')
        """The token of the webhook."""