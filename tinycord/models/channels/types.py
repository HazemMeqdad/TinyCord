from enum import IntEnum, unique
import typing
from ..mixins import EnumMixin

@unique
class Channeltypes(EnumMixin, IntEnum):
    """
        This is the channel types enum.
    """
    GUILD_TEXT = 0
    DM = 1
    GUILD_VOICE = 2
    GROUP_DM = 3
    GUILD_CATEGORY = 4
    GUILD_NEW = 5
    GUILD_STORE = 6
    GUILD_NEWS_THREAD = 10
    GUILD_PUBLIC_THREAD = 11
    GUILD_PRIVATE_THREAD = 12
    GUILD_STAGE_VOICE = 13

@unique
class Permissionoverwritetypes(EnumMixin, IntEnum):
    """
        This is the permission overwrite types enum.
    """
    ROLE = 0
    MEMBER = 1

if typing.TYPE_CHECKING:
    from . import TextChannel, VoiceChannel, NewsChannel, DMChannel, StageChannel

All = typing.Union[
    "TextChannel",
    "VoiceChannel",
    "NewsChannel",
    "DMChannel",
    "StageChannel",
]