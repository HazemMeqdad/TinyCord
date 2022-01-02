import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Integration

async def integration_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a integration is created.
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
    integration = Integration(client, **event.data)
    """ The integration that was created. """
    
    guild = client.get_guild(integration.guild_id)
    """ The guild that the integration was created in. """
    
    guild.integrations[str(integration.id)] = integration
    """ Cache the integration. """
    
    return "on_integration_create", [
        guild, integration 
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return integration_create