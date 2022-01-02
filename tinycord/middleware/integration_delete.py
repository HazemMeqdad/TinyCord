import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

async def integration_delete(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a integration is deleted.
        It does prase the integration data and returns the event with the guild and the integration.
    
        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    guild = client.get_guild(event.data['guild_id'])
    """ The guild that the integration was deleted from. """

    integration = guild.get_integration(event.data['id'])
    """ The integration that was deleted. """

    return "on_integration_delete", [
        guild, integration
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return integration_delete