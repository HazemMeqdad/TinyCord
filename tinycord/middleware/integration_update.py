import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Integration

async def integration_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    after = Integration(client, **event.data)
    guild = client.get_guild(event.data['guild_id'])
    before = guild.get_integration(after.id)

    try:
        guild.integrations.remove(before)
        guild.integrations.append(after)
    except:
        pass

    return "on_integration_update", [
        guild, before, after
    ]

def export():
    return integration_update