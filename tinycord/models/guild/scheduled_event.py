import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client

from ..mixins import Hashable
from ...utils import Snowflake

@dataclasses.dataclass(repr=False)
class ScheduledEvent(Hashable):
    """
        This represents a scheduled event.

        Parameters
        ----------
        client : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the sticker.

    """
    def __init__(self, client: "Client", guild_id: Snowflake = None, **data) -> None:
        self.client = client
        """The main client."""

        self.guild_id: Snowflake = guild_id
        """The ID of the guild."""

        self.channel_id: Snowflake = Snowflake(
            data.get('channel_id'))
        """The ID of the channel."""

        self.creator_id: Snowflake = Snowflake(
            data.get('creator_id'))
        """The ID of the creator."""

        self.name: str = data.get('name')
        """The name of the scheduled event."""

        self.description: typing.Union[str, None] = data.get('description')
        """The description of the scheduled event."""

        self.scheduled_start: int = data.get('scheduled_start')
        """The scheduled start of the scheduled event."""

        self.scheduled_end: int = data.get('scheduled_end')
        """The scheduled end of the scheduled event."""
        
        self.privacy: int = data.get('privacy')
        """The privacy of the scheduled event."""

        self.status: int = data.get('status')
        """The status of the scheduled event."""

        self.enitity_type: int = data.get('entity_type')
        """The entity type of the scheduled event."""

        self.enitity_id: typing.Union[Snowflake, None] = Snowflake(
            data.get('entity_id'))
        """The ID of the entity."""

        self.enitity_meta: typing.Union[str, None] = data.get('entity_meta')
        """The meta of the entity."""

        self.user_count: typing.Union[int, None] = data.get('user_count')
        """The user count of the scheduled event."""




