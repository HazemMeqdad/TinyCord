import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import deserialize_channel
    
async def channel_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event is called when a channel is created.
        It does parse the channel data, update the data and update the cache.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    after = deserialize_channel(client, **event.data)
    """ The channel that was created. """

    before = client.get_channel(after.id)
    """ The old channel from the cache. """

    guild = client.get_guild(after.guild_id)
    """ The guild that the channel was created in. """
    
    client.channels[str(after.id)] = after
    guild.channels[str(after.id)] = after
    """ Update the cache. """

    return "on_channel_update", [
        guild, before, after
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return channel_update