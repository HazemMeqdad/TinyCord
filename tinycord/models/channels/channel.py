import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client
    from ..guild import Guild

from ..mixins import Hashable
from ...utils import Snowflake

@dataclasses.dataclass(repr=False)
class BaseChannel(Hashable):
    """
        This is the BaseChannel class that is used to make other types of channels easier to use.
        It is used to make other types of channels easier to use by providing a more readable interface.

        Parameters
        ----------
        client : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the channel.

        Attributes
        ----------
        client : `Client`
            The main client.
        guild_id : `Snowflake`
            The ID of the guild.
        id : `Snowflake`
            The ID of the channel.
        name : `str`
            The name of the channel.
        type : `str`
            The type of the channel.
        position : `int`
            The position of the channel.
        permission_overwrites : `typing.List`
            The permission overwrites of the channel.
        parent_id : `Snowflake`
            The ID of the parent channel.
    """
    def __init__(self, client: "Client", guild_id: Snowflake , **data) -> None:
        self.client = client
        """The main client."""

        self.guild_id: Snowflake = guild_id
        """The ID of the guild."""

        self.id: Snowflake = Snowflake(
            data.get('id'))
        """The ID of the channel."""

        self.name: str = data.get('name')
        """The name of the channel."""

        self.type: str = data.get('type')
        """The type of the channel."""

        self.position: int = data.get('position')
        """The position of the channel."""

        self.permission_overwrites: typing.List[
            typing.Dict[str,str]] = data.get('permission_overwrites')
        """The permission overwrites of the channel."""

        self.parent_id: Snowflake = Snowflake(
            data.get('parent_id'))
        """The ID of the parent channel."""

    @property
    def guild(self) -> typing.Union["Guild", None]:
        """The guild of the channel."""

        return self.client.get_guild(self.guild_id)

    async def edit(self, reason: str = None, **kwargs) -> None:
        """
            Edits the channel.

            Parameters
            ----------
            **kwargs
                The attributes that are used to edit the channel.
        """
        await self.client.api.channel_edit(self.id, reason , **kwargs)

    async def delete(self, reason: str = None) -> None:
        """
            Deletes the channel.
        """
        await self.client.api.channel_delete(self.id, reason)