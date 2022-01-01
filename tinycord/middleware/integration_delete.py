import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Integration

async def integration_delete(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    guild = client.get_guild(event.data['guild_id'])
    integration = guild.get_integration(event.data['id'])

    try:
        del guild.integrations[str(integration.id)]
    except KeyError:
        pass

    return "on_integration_delete", [
        guild, integration
    ]

def export():
    return integration_delete