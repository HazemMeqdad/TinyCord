import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client

from ..mixins import Hashable
from ...utils import Snowflake

from .role import Role

@dataclasses.dataclass(repr=False)
class Guild(Hashable):
    """
        This is the Guild class is represent the guilds that are created by the client.
        It simplfies and parses the data that is returned from the API.
        It does provide a contorl interface to the guild.

        Parameters
        ----------
        client : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the guild.

        Attributes
        ----------
        NOT FINISHED YET
    """
    def __init__(self, client: "Client", **data) -> None:
        self.client = client
        """The main client."""

        self.id: Snowflake = Snowflake(
            data.get('id'))
        """The ID of the guild."""

        self.name: str = data.get('name')
        """The name of the guild."""

        self.icon: str = data.get('icon')
        """The icon of the guild."""

        self.splash: str = data.get('splash')
        """The splash of the guild."""

        self.owner_id: Snowflake = Snowflake(
            data.get('owner_id'))
        """The ID of the owner of the guild."""

        self.region: str = data.get('region')
        """The region of the guild."""

        self.afk_channel_id: Snowflake = Snowflake(
            data.get('afk_channel_id'))
        """The ID of the AFK channel."""

        self.afk_timeout: int = data.get('afk_timeout')
        """The timeout of the AFK channel."""

        self.embed_enabled: bool = data.get('embed_enabled')
        """Whether the embed is enabled or not."""

        self.embed_channel_id: Snowflake = Snowflake(
            data.get('embed_channel_id'))
        """The ID of the embed channel."""

        self.verification_level: int = data.get('verification_level')
        """The verification level of the guild."""

        self.default_message_notifications: int = data.get('default_message_notifications')
        """The default message notifications of the guild."""

        self.explicit_content_filter: int = data.get('explicit_content_filter')
        """The explicit content filter of the guild."""

        self.roles: typing.List[Role] = [
            Role(client, self.id, **role) for role in data.get('roles')]
        """The roles of the guild."""
