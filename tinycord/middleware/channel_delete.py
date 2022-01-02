import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

async def channel_delete(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event is called when a channel is update.
        It does parse the channel data, delete the channel from the cache and returns the event with the args.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    channel = client.get_channel(event.data["id"])
    """ The channel that was deleted. """

    guild = client.get_guild(channel.guild_id)
    """ The guild that the channel was deleted from. """

    try:
        del client.channels[str(channel.id)]
        del guild.channels[str(channel.id)]
        """ Try to delete the channel from the cache. """
    except KeyError:
        pass

    return "on_channel_delete", [
        guild, channel
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return channel_delete