import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch
    
async def invite_remove(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when the a new invite is created.
        It does does provide the invite.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """

    invite = event.data
    """ The invite that was created. """
    
    channel = client.get_channel(invite['channel_id'])
    """ The channel that the invite was created in. """

    return "on_invite_remove", [
        channel, invite
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return invite_remove