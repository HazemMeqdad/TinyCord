import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client

from .channel import BaseChannel
from ..mixins import Hashable
from ...utils import Snowflake

@dataclasses.dataclass(repr=False)
class DMChannel(BaseChannel,Hashable):
    """
        This is the DMChannel it used to represent a direct message channel.

        Parameters
        ----------
        client : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the channel.

        Attributes
        ----------
        recipients : `typing.List[typing.Dict]`
            The recipients of the channel.
    """
    def __init__(self, client: "Client", guild_id: Snowflake , **data) -> None:
        self.recipients: typing.List[typing.Dict] = data.get('recipients')
        """The recipients of the channel."""
        
        super(BaseChannel, self).__init__(client, guild_id, **data)
        """The base channel."""

        