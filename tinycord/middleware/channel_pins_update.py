import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

async def channel_pins_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event is called when a message is pinned or unpinned in a text channel.
        It does update the cache and return the event with the args.

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
    """ The channel that the message was pinned or unpinned in. """

    before = channel.last_pin_timestamp
    """ The timestamp of the last pinned message. """
    
    after = event.data["last_pin_timestamp"]
    """ The timestamp of the last pinned message. """

    channel.last_pin_timestamp = after


    return "on_channel_pins_update", [
        channel, before, after
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return channel_pins_update