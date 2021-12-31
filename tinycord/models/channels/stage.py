import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client

from .channel import BaseChannel
from ..mixins import Hashable
from ...utils import Snowflake

@dataclasses.dataclass(repr=False)
class StageChannel(BaseChannel,Hashable):
    """
        This is the StageChannel it used to represent a stage channel.

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
        privacy_level : `str`
            The privacy level of the channel.
        discoverable_disabled : `bool`
            Whether the channel is discoverable or not.
    """
    def __init__(self, client: "Client", guild_id: Snowflake , **data) -> None:
        self.topic: str = data.get('topic')
        """The topic of the channel."""

        self.privacy_level: str = data.get('privacy_level')
        
        self.discoverable_disabled: bool = data.get('discoverable_disabled')
        """Whether the channel is discoverable or not."""
        
        super(BaseChannel, self).__init__(client, guild_id, **data)
        """The base channel."""

        