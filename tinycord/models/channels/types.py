from enum import Enum
from ..mixins import EnumMixin

class Channeltypes(Enum, EnumMixin):
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

class Permissionoverwritetypes(Enum, EnumMixin):
    """
        This is the permission overwrite types enum.
    """
    ROLE = 0
    MEMBER = 1