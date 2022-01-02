import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Integration

async def integration_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a integration is updated.
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
    after = Integration(client, **event.data)
    """ The integration that was updated. """

    guild = client.get_guild(event.data['guild_id'])
    """ The guild that the integration was updated in. """

    before = guild.get_integration(after.id)
    """ The integration that was updated. """

    guild.integrations[str(after.id)] = after
    """ Cache the integration. """

    return "on_integration_update", [
        guild, before, after
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return integration_update