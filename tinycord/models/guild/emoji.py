import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client

from ..mixins import Hashable
from ...utils import Snowflake

@dataclasses.dataclass(repr=False)
class Emoji(Hashable):
    """
        This is the Emoji it used to represent a emoji.

        Parameters
        ----------
        client : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the emoji.

        Attributes
        ----------
        id : `Snowflake`
            The ID of the emoji.
        name : `str`
            The name of the emoji.
        roles : `typing.Union[typing.List[Snowflake], None]`
            The roles of the emoji.
        available : `bool`
            Whether the emoji is available or not.
        animated : `bool`
            Whether the emoji is animated or not.

    """
    def __init__(self, client: "Client", guild_id: Snowflake, **data) -> None:
        self.client = client
        """The main client."""

        self.guild_id: Snowflake = guild_id
        """The ID of the guild."""

        self.id: Snowflake = Snowflake(
            data.get('id'))
        """The ID of the role."""

        self.name: str = data.get('name')
        """The name of the role."""

        self.roles: typing.Union[typing.List[Snowflake], None] = data.get('roles')
        """The roles of the emoji."""
        
        self.available: bool = data.get('available')
        """Whether the emoji is available or not."""
        
        self.animated: bool = data.get('animated')
        """Whether the emoji is animated or not."""