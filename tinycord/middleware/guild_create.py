import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Guild
    
async def guild_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event is called when a guild is created.
        It does see whether the guild is cached and if not, it caches it.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    guild = Guild(client, **event.data)
    """ The guild that was created. """

    for id, channel in guild.channels.items():
        client.channels[id] = channel
        """ The channels that were should be cached. """
        
    for id, user in guild.users.items():
        client.users[id] = user
        """ The users that were should be cached. """

    client.guilds[str(guild.id)] = guild
    """ Caching the guild. """

    if guild.id in client.unavailable_guilds: # Seeing if the guild id in a speaicl array where cached guilds id saved
        client.unavailable_guilds.remove(guild.id)
        """ Removing the guild id from the unavailable guilds array. """

        return "on_guild_cache", [
            guild
        ]
        """ The event that was dispatched. """

    return "on_guild_join", [
        guild
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return guild_create