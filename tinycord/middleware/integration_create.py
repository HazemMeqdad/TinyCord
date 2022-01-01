import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Integration

async def integration_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    integration = Integration(client, **event.data)
    guild = client.get_guild(event.data['guild_id'])

    guild.integrations.append(integration)

    return "on_integration_create", [
        guild, integration
    ]

def export():
    return integration_create