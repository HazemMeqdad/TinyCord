import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client

from .channel import BaseChannel
from ..mixins import Hashable
from ...utils import Snowflake

@dataclasses.dataclass(repr=False)
class NewsChannel(BaseChannel,Hashable):
    """
        This is the NewsChannel it used to represent a news channel.

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
        nsfw : `bool`
            Whether the channel is nsfw or not.
        default_auto_archive_duration : `int`
            The default auto archive duration.
    """
    def __init__(self, client: "Client", guild_id: Snowflake , **data) -> None:
        self.topic: str = data.get('topic')
        """The topic of the channel."""

        self.nsfw: bool = data.get('nsfw')
        """Whether the channel is nsfw or not."""
        
        self.default_auto_archive_duration: int = data.get('default_auto_archive_duration')
        """The default auto archive duration."""
        
        super().__init__(client, guild_id, **data)
        """The base channel."""

        