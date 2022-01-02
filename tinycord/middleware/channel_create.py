import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import deserialize_channel
    
async def channel_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event is called when a channel is created.
        It does parse the channel data and returns the event with the args.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    channel = deserialize_channel(client, **event.data)
    """ The channel that was created. """

    guild = client.get_guild(channel.guild_id)
    """ The guild that the channel was created in. """
    
    client.channels[str(channel.id)] = channel
    guild.channels[str(channel.id)] = channel
    """ Cache the channel. """

    return "on_channel_create", [
        guild, channel
    ]

def export():
    """ Exports the function. """
    return channel_create