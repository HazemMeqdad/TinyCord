import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client
    from ..guild import Guild, Role
    from ..user import Voicestate

from ..mixins import Hashable
from ...utils import Snowflake
from ..user import User

@dataclasses.dataclass(repr=False)
class Member(User, Hashable):
    """
        The member is a part from a guild.
        It's basically a member from a guild.
        It contains all the information about the member.

        Parameters
        ----------
        client : `Client`
            The main client.
        **data : `typing.Dict`
            The data that is used to create the member.

        Attributes
        ----------
        roles_ids : `typing.List[Snowflake]`
            The roles of the member.
        nick : `typing.Union[str, None]`
            The nickname of the member.
        avatar : `typing.Union[str, None]`
            The avatar of the member.
        joined_at : `str`
            The date the member joined the guild.
        deaf : `bool`
            Whether the member is deafened or not.
        mute : `bool`
            Whether the member is muted or not.
    """
    def __init__(self, client: "Client", guild_id: Snowflake , **data) -> None:

        self.client = client
        """The main client."""

        self.guild_id: Snowflake = guild_id
        """The ID of the guild."""

        self.roles_ids: typing.List[Snowflake] = [
            Snowflake(role) for role in data.get('roles')]
        """The roles of the member."""

        self.nick: typing.Union[str, None] = data.get('nick')
        """The nickname of the member."""

        self.avatar: typing.Union[str, None] = data.get('avatar')
        """The avatar of the member."""

        self.joined_at: str = data.get('joined_at')
        """The date the member joined the guild."""

        self.deaf: bool = data.get('deaf')
        """Whether the member is deafened or not."""

        self.mute: bool = data.get('mute')
        """Whether the member is muted or not."""

        super().__init__(client, **data.get('user'))

    @property
    def guild(self) -> typing.Union["Guild", None]:
        """The guild of the member."""

        return self.client.get_guild(self.guild_id)

    @property
    def voice_state(self) -> typing.Union["Voicestate", None]:
        """The voice state of the member."""

        return self.guild.get_voice_state(self.id)

    @property
    def roles(self) -> typing.List["Role"]:
        """The roles of the member."""

        return [self.guild.get_role(role_id) for role_id in self.roles_ids]
        
    @property
    def top_role(self) -> "Role":
        """The top role of the member."""

        return max(self.roles, key=lambda role: int(role.position))

    @property
    def all_permissions(self) -> typing.List[str]:
        """The permissions of the member."""

        return [ permission for permission in [role.permissions for role in self.roles] ]

    @property
    def display_hex_color(self) -> str:
        """The display hex color of the member."""

        return self.top_role.color

    @property
    def display_name(self) -> str:
        """The display name of the member."""

        return self.nick if self.nick else self.name

    @property
    def mention(self) -> str:
        """The mention of the member."""

        return f'<@{self.id}>'

    async def edit(self, reason: str = None, **kwargs) -> None:
        """
            Edits the member.

            Parameters
            ----------
            reason : `typing.Union[str, None]`
                The reason for the edit.
            **kwargs
                The key-value pairs to edit.
        """

        await self.client.api.guild_member_edit(self.guild_id, self.id, reason, **kwargs)

    async def add_role(self, role_id: Snowflake, reason: str = None) -> None:
        """
            Adds a role to the member.

            Parameters
            ----------
            role_id : `Snowflake`
                The ID of the role.
            reason : `typing.Union[str, None]`
                The reason for the edit.
        """

        await self.client.api.guild_member_add_role(self.guild_id, self.id, role_id, reason)

    async def remove_role(self, role_id: Snowflake, reason: str = None) -> None:
        """
            Removes a role from the member.

            Parameters
            ----------
            role_id : `Snowflake`
                The ID of the role.
            reason : `typing.Union[str, None]`
                The reason for the edit.
        """

        await self.client.api.guild_member_delete_role(self.guild_id, self.id, role_id, reason)

    async def kick(self, reason: str = None) -> None:
        """
            Kicks the member.

            Parameters
            ----------
            reason : `typing.Union[str, None]`
                The reason for the kick.
        """

        await self.client.api.guild_kick_member(self.guild_id, self.id, reason)

    async def ban(self, reason: str = None) -> None:
        """
            Bans the member.

            Parameters
            ----------
            reason : `typing.Union[str, None]`
                The reason for the ban.
        """

        await self.client.api.guild_ban_member(self.guild_id, self.id, reason)

    async def unban(self, reason: str = None) -> None:
        """
            Unbans the member.

            Parameters
            ----------
            reason : `typing.Union[str, None]`
                The reason for the unban.
        """

        await self.client.api.guild_unban(self.guild_id, self.id, reason)