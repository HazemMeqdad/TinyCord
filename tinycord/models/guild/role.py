import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client

from ..mixins import Hashable
from ...utils import Snowflake, Permission

@dataclasses.dataclass(repr=False)
class Role(Hashable):
    """
        This is the Role it used to represent a role.

        Parameters
        ----------
        client : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the role.

        Attributes
        ----------
        id : `Snowflake`
            The ID of the role.
        name : `str`
            The name of the role.
        color : `str`
            The color of the role.
        hoist : `str`
            Whether the role is hoisted or not.
        position : `str`
            The position of the role.
        permissions : `str`
            The permissions of the role.
        managed : `bool`
            Whether the role is managed or not.
        mentionable : `str`
            Whether the role is mentionable or not.
        created_at : `str`
            The created at of the role.
        tags : `typing.Dict[str, typing.Any]`
            The tags of the role.
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

        self.color: str = data.get('color')
        """The color of the role."""

        self.hoist: str = data.get('hoist')
        """Whether the role is hoisted or not."""

        self.position: str = data.get('position')
        """The position of the role."""

        self.permissions: typing.List[str] = Permission(
            data.get('permissions')).compute()
        """The permissions of the role."""

        self.managed: bool = data.get('managed')
        """Whether the role is managed or not."""

        self.mentionable: str = data.get('mentionable')
        """Whether the role is mentionable or not."""

        self.created_at: str = data.get('created_at')
        """The created at of the role."""

        self.tags: typing.Dict[str, typing.Any] = data.get('tags')
        """The tags of the role."""

    async def edit(self, reason: str = None, **kwargs) -> None:
        """
            Edits the role.

            Parameters
            ----------
            reason : `str`
                The reason for editing the role.
            **kwargs : `typing.Dict`
                The data that is used to edit the role.
        """

        await self.client.api.guild_edit_role(self.guild_id, self.id, reason, **kwargs)

    async def delete(self, reason: str = None) -> None:
        """
            Deletes the role.

            Parameters
            ----------
            reason : `str`
                The reason for deleting the role.
        """

        await self.client.api.guild_delete_role(self.guild_id, self.id, reason)

    @property
    def is_default(self) -> bool:
        """
            Whether the role is the default role.

            Returns
            -------
            `bool`
                Whether the role is the default role.
        """

        return self.name == "@everyone"