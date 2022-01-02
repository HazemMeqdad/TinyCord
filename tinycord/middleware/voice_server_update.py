import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch
    
async def voice_server_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a voice server is updated.
        It does return the event is it is.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """

    guild = client.get_guild(event.data["guild_id"])
    """ The guild that the voice server was updated in. """

    if event.data['endpoint'] is not None:
        guild.voice_server = event.data
    else:
        guild.voice_server = None
        

    return "on_vocie_server_updateR", [
        guild, event.data
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return voice_server_update