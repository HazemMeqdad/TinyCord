import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client

from ..mixins import Hashable
from ...utils import Snowflake

@dataclasses.dataclass(repr=False)
class Sticker(Hashable):
    """
        This is the Sticker it used to represent a sticker.

        Parameters
        ----------
        client : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the sticker.

        Attributes
        ----------
        id : `Snowflake`
            The ID of the sticker.
        pack_id : `Snowflake`
            The ID of the sticker.
        name : `str`
            The name of the sticker.
        description : `str`
            The description of the sticker.
        tags : `typing.Union[typing.List[Snowflake], None]`
            The tags of the sticker.
        type : `typing.Union[typing.List[Snowflake], None]`
            The type of the sticker.
        format_type : `typing.Union[typing.List[Snowflake], None]`
            The format type of the sticker.
        available : `bool`
            Whether the sticker is available or not.
        user : `typing.Union[typing.List[Snowflake], None]`
            The user of the sticker.
        sort_value : `int`
            The sort value of the sticker.
    """
    def __init__(self, client: "Client", guild_id: Snowflake = None, **data) -> None:
        self.client = client
        """The main client."""

        self.guild_id: Snowflake = guild_id
        """The ID of the guild."""

        self.id: Snowflake = Snowflake(
            data.get('id'))
        """The ID of the sticker."""

        self.pack_id: Snowflake = Snowflake(
            data.get('pack_id'))
        """The ID of the sticker."""

        self.name: str = data.get('name')
        """The name of the sticker."""

        self.description: str = data.get('description')
        """The description of the sticker."""

        self.tags: typing.Dict[str, typing.Any] = data.get('tags')
        """The tags of the sticker."""
        
        self.type: typing.Dict[str, typing.Any] = data.get('type')
        """The type of the sticker."""

        self.format_type: typing.Dict[str, typing.Any] = data.get('format_type')
        """The format type of the sticker."""
        
        self.available: bool = data.get('available')
        """Whether the sticker is available or not."""
        
        self.user: typing.Dict[str, typing.Any] = data.get('user')
        """The user of the sticker."""

        self.sort_value: int = data.get('sort_value')
        """The sort value of the sticker."""

    async def edit(self, reason: str = None, **kwargs) -> None:
        """
            Edits the sticker.

            Parameters
            ----------
            reason : `str`
                The reason for editing the sticker.
            **kwargs : `typing.Any`
                The data that is used to edit the sticker.
        """
        await self.client.api.guild_edit_sticker(self.guild_id, self.id, reason, **kwargs)

    async def delete(self, reason: str = None) -> None:
        """
            Deletes the sticker.

            Parameters
            ----------
            reason : `str`
                The reason for deleting the sticker.
        """
        await self.client.api.guild_delete_sticker(self.guild_id, self.id, reason)