from enum import Enum

class Intents(Enum):
    """
        This is the intents enum.
        This used to define the intents that are used to connect to Discord.

        Example:
        ```py
        client = Client(
            "token",
            intents=[Intents.GUILDS, Intents.GUILD_MESSAGES]
        )

        client.connect()
        ```
    """
    GUILDS: int = 1 << 0
    GUILD_MEMBERS: int = 1 << 1
    GUILD_BANS: int = 1 << 2
    GUILD_EMOJIS_AND_STICKERS: int = 1 << 3
    GUILD_INTEGRATIONS: int = 1 << 4
    GUILD_WEBHOOKS: int = 1 << 5
    GUILD_INVITES: int = 1 << 6
    GUILD_VOICE_STATES: int = 1 << 7
    GUILD_PRESENCES: int = 1 << 8
    GUILD_MESSAGES: int = 1 << 9
    GUILD_MESSAGE_REACTIONS: int = 1 << 10
    GUILD_MESSAGE_TYPING: int = 1 << 11
    DIRECT_MESSAGES: int = 1 << 12
    DIRECT_MESSAGE_REACTIONS: int = 1 << 13
    DIRECT_MESSAGE_TYPING: int = 1 << 14

    @staticmethod
    def all() -> int:
        """
            This function is used to get all the int values of the enum.
        """
        return sum(
            [int(i) for i in Intents.__members__.values()]
        )

    def __int__(self) -> int:
        """
            This function is used to get the int value of the enum.
        """
        return int(self.value)