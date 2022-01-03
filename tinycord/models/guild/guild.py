import typing
import dataclasses

if typing.TYPE_CHECKING:
    from ...client import Client
    from ..user import Integration

from ..mixins import Hashable
from ...utils import Snowflake

from .role import Role
from .emoji import Emoji
from .sticker import Sticker
from ..channels import deserialize_channel, ThreadChannel, All
from .member import Member
from ..user import User, Voicestate
from .scheduled_event import ScheduledEvent

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
        id : `Snowflake`
            The ID of the guild.
        name : `str`
            The name of the guild.
        icon : `str`
            The icon of the guild.
        splash : `str`
            The splash of the guild.
        owner_id : `Snowflake`
            The ID of the owner of the guild.
        permissions : `int`
            The permissions of the guild.
        region : `str`
            The region of the guild.
        afk_channel_id : `Snowflake`
            The ID of the AFK channel.
        afk_timeout : `int`
            The timeout of the AFK channel.
        widget_enabled : `bool`
            Whether the widget is enabled or not.
        widget_channel_id : `Snowflake`
            The ID of the widget channel.
        verification_level : `int`
            The verification level of the guild.
        default_notification_level : `int`
            The default notification level of the guild.
        explicit_content_filter : `int`
            The explicit content filter of the guild.
        roles : `typing.List[Role]`
            The roles of the guild.
        emojis : `typing.List[Emoji]`
            The emojis of the guild.
        features : `typing.List[str]`
            The features of the guild.
        mfa_level : `int`
            The MFA level of the guild.
        application_id : `Snowflake`
            The ID of the application.
        system_channel_id : `Snowflake`
            The ID of the system channel.
        system_channel_flags : `int`
            The flags of the system channel.
        rules_channel_id : `Snowflake`
            The ID of the rules channel.
        joined_at : `datetime.datetime`
            The date and time the guild was joined.
        large : `bool`
            Whether the guild is large or not.
        unavailable : `bool`
            Whether the guild is unavailable or not.
        member_count : `int`
            The member count of the guild.
        max_presences : `int`
            The max presences of the guild.
        max_members : `int`
            The max members of the guild.
        vanity_url_code : `str`
            The vanity url code of the guild.
        description : `str`
            The description of the guild.
        banner : `str`
            The banner of the guild.
        premium_tier : `int`
            The premium tier of the guild.
        premium_subscription_count : `int`
            The premium subscription count of the guild.
        preferred_locale : `str`
            The preferred locale of the guild.
        public_updates_channel_id : `Snowflake`
            The ID of the public updates channel.
        max_video_channel_users : `int`
            The max video channel users of the guild.
        approximate_member_count : `int`
            The approximate member count of the guild.
        approximate_presence_count : `int`
            The approximate presence count of the guild.
        welcome_screen : `typing.Dict`
            The welcome screen of the guild.
        nfsw_enabled : `bool`
            Whether the guild is nfsw enabled or not.
        stage_instances : `typing.List[typing.Dict]`
            The stage instances of the guild.
        premium_subscription_count_new : `int`
            The premium subscription count of the guild.

        
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

        self.icon_hash: typing.Union[str, None] = data.get('icon_hash')
        """The icon hash of the guild."""

        self.splash: str = data.get('splash')
        """The splash of the guild."""

        self.discovery_splash: str = data.get('discovery_splash')
        """The discovery splash of the guild."""

        self.owner_id: Snowflake = Snowflake(
            data.get('owner_id'))
        """The ID of the owner of the guild."""

        self.permissions: typing.Union[int, None] = data.get('permissions')
        """The permissions of the guild."""

        self.region: str = data.get('region')
        """The region of the guild."""

        self.afk_channel_id: Snowflake = Snowflake(
            data.get('afk_channel_id'))
        """The ID of the AFK channel."""

        self.afk_timeout: int = data.get('afk_timeout')
        """The timeout of the AFK channel."""

        self.widget_enabled: typing.Union[bool, None] = data.get('widget_enabled')
        """Whether the widget is enabled or not."""

        self.widget_channel_id: typing.Union[Snowflake, None] = data.get('widget_channel_id')
        """The ID of the widget channel."""

        self.verification_level: int = data.get('verification_level')
        """The verification level of the guild."""

        self.default_message_notifications: int = data.get('default_message_notifications')
        """The default message notifications of the guild."""

        self.explicit_content_filter: int = data.get('explicit_content_filter')
        """The explicit content filter of the guild."""

        self.embed_channel_id: Snowflake = Snowflake(
            data.get('embed_channel_id'))
        """The ID of the embed channel."""

        self.channels: typing.Dict[str, "All"] = {
            channel['id'] : deserialize_channel(self.client, self.id , **channel) for channel in data.get('channels', [])}
        """The channels of the guild."""
        
        self.threads: typing.Dict[str, "ThreadChannel"] = {
            channel['id'] : ThreadChannel(self.client, self.id , channel) for channel in data.get('threads', [])}
        """The threads of the guild."""

        self.roles: typing.List[str, "Role"] = {
            role['id'] : Role(client, self.id, **role) for role in data.get('roles')}
        """The roles of the guild."""
        
        self.emojis: typing.Dict[str, "Emoji"] = {
            emoji['id'] : Emoji(client, self.id, **emoji) for emoji in data.get('emojis')}
        """The emojis of the guild."""
        
        self.stickers: typing.Dict[str, "Sticker"] = {
            sticker['id'] : Sticker(client, self.id, **sticker) for sticker in data.get('stickers')}
        """The stickers of the guild."""

        self.members: typing.Dict[str, "Member"] = {
            member['user']['id'] : Member(client, self.id, **member) for member in data.get('members')}
        """The members of the guild."""

        self.users: typing.Dict[str, "User"] = {
           user['user']['id'] : User(client, **user['user']) for user in data.get('members')}
        """The users of the guild."""

        self.voice_states: typing.Dict[str, "Voicestate"] = {
            voice_state['user_id'] : Voicestate(client, self.id , **voice_state) for voice_state in data.get('voice_states')}
        """The voice states of the guild."""
        
        self.features: typing.List[str] = data.get('features')
        """The features of the guild."""

        self.mfa_level: int = data.get('mfa_level')
        """The MFA level of the guild."""

        self.application_id: Snowflake = Snowflake(
            data.get('application_id'))
        """The ID of the application of the guild."""

        self.system_channel_id: Snowflake = Snowflake(
            data.get('system_channel_id'))
        """The ID of the system channel."""

        self.system_channel_flags: int = data.get('system_channel_flags')
        """The flags of the system channel."""

        self.rules_channel_id: Snowflake = Snowflake(
            data.get('rules_channel_id'))
        """The ID of the rules channel."""

        self.joined_at: typing.Union[str, None] = data.get('joined_at')
        """The time the guild was joined."""

        self.large: typing.Union[bool, None] = data.get('large')
        """Whether the guild is large or not."""

        self.unavailable: typing.Union[bool, None] = data.get('unavailable')
        """Whether the guild is unavailable or not."""

        self.member_count: typing.Union[int, None] = data.get('member_count')
        """The member count of the guild."""

        self.max_presences: typing.Union[int, None] = data.get('max_presences')
        """The max presences of the guild."""

        self.max_members: typing.Union[int, None] = data.get('max_members')
        """The max members of the guild."""

        self.vanity_url_code: typing.Union[str, None] = data.get('vanity_url_code')
        """The vanity url code of the guild."""

        self.description: typing.Union[str, None] = data.get('description')
        """The description of the guild."""

        self.banner: typing.Union[str, None] = data.get('banner')
        """The banner of the guild."""

        self.premium_tier: typing.Union[int, None] = data.get('premium_tier')
        """The premium tier of the guild."""

        self.premium_subscription_count: typing.Union[int, None] = data.get('premium_subscription_count')
        """The premium subscription count of the guild."""

        self.preferred_locale: typing.Union[str, None] = data.get('preferred_locale')
        """The preferred locale of the guild."""

        self.public_updates_channel_id: typing.Union[Snowflake, None] = data.get('public_updates_channel_id')
        """The ID of the public updates channel."""

        self.max_video_channel_users: typing.Union[int, None] = data.get('max_video_channel_users')
        """The max video channel users of the guild."""

        self.approximate_member_count: typing.Union[int, None] = data.get('approximate_member_count')
        """The approximate member count of the guild."""

        self.approximate_presence_count: typing.Union[int, None] = data.get('approximate_presence_count')
        """The approximate presence count of the guild."""
        
        self.welcome_screen: typing.Dict[str, typing.Any] = data.get('welcome_screen')
        """The welcome screen of the guild."""

        self.nfsw_enabled: typing.Union[bool, None] = data.get('nfsw_enabled')
        """Whether the guild is nfsw enabled or not."""
        
        self.stage_instances: typing.List[str] = data.get('stage_instances')
        """The stage instances of the guild."""
        
        self.guild_scheduled_events: typing.Dict[str, "ScheduledEvent"] = {
            event['id'] : ScheduledEvent(client, self.id, **event) for event in data.get('guild_scheduled_events')}
        """The guild scheduled events of the guild."""
        
        self.premium_progress_bar_enabled: typing.Union[bool, None] = data.get('premium_progress_bar_enabled')
        """Whether the guild has the premium progress bar enabled or not."""

        self.integrations: typing.List["Integration"] = {}
        """The integrations of the guild."""

        self.voice_server: typing.Dict[str, str] = None

    # Get methods
    
    def get_role(self, id: Snowflake) -> typing.Union["Role", None]:
        """Get a role of the guild.

        Parameters
        ----------
        id : :class:`Snowflake`
            The ID of the role.

        Returns
        -------
        :class:`Role`
            The role of the guild.
        """

        return self.roles.get(str(id), None)

    def get_emoji(self, id: Snowflake) -> typing.Union["Emoji", None]:
        """Get an emoji of the guild.

        Parameters
        ----------
        id : :class:`Snowflake`
            The ID of the emoji.

        Returns
        -------
        :class:`Emoji`
            The emoji of the guild.
        """

        return self.emojis.get(str(id), None)

    def get_member(self, id: Snowflake) -> typing.Union["Member", None]:
        """Get a member of the guild.

        Parameters
        ----------
        id : :class:`Snowflake`
            The ID of the member.

        Returns
        -------
        :class:`Member`
            The member of the guild.
        """

        return self.members.get(str(id), None)

    def get_user(self, id: Snowflake) -> typing.Union["User", None]:
        """Get a user of the guild.

        Parameters
        ----------
        id : :class:`Snowflake`
            The ID of the user.

        Returns
        -------
        :class:`User`
            The user of the guild.
        """

        return self.users.get(str(id), None)

    def get_channel(self, id: Snowflake) -> typing.Union["All", None]:
        """Get a channel of the guild.

        Parameters
        ----------
        id : :class:`Snowflake`
            The ID of the channel.

        Returns
        -------
        :class:`All`
            The channel of the guild.
        """

        return self.channels.get(str(id), None)

    def get_thread(self, id: Snowflake) -> typing.Union["ThreadChannel", None]:
        """Get a thread of the guild.

        Parameters
        ----------
        id : :class:`Snowflake`
            The ID of the thread.

        Returns
        -------
        :class:`TextChannel`
            The thread of the guild.
        """

        return self.threads.get(str(id), None)

    def get_integration(self, id: Snowflake) -> typing.Union["Integration", None]:
        """Get an integration of the guild.

        Parameters
        ----------
        id : :class:`Snowflake`
            The ID of the integration.

        Returns
        -------
        :class:`Integration`
            The integration of the guild.
        """

        return self.integrations.get(str(id), None)

    def get_scheduled_event(self, id: Snowflake) -> typing.Union["ScheduledEvent", None]:
        """Get a scheduled event of the guild.

        Parameters
        ----------
        id : :class:`Snowflake`
            The ID of the scheduled event.

        Returns
        -------
        :class:`ScheduledEvent`
            The scheduled event of the guild.
        """

        return self.guild_scheduled_events.get(str(id), None)

    def get_voice_state(self, id: Snowflake) -> typing.Union["Voicestate", None]:
        """
        Get a voice state of the guild.

        Parameters
        ----------
        id : :class:`Snowflake`
            The ID of the voice state.

        Returns
        -------
        :class:`Voicestate`
            The voice state of the guild.
        """

        return self.voice_states.get(str(id), None)