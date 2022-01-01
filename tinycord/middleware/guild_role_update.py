import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Role

async def guild_role_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    after = Role(client, **event.data)
    guild = client.get_guild(after.guild_id)
    before = guild.get_role(after.id)

    try:
        guild.roles.remove(before)
        guild.roles.append(after)
    except:
        pass

    return "on_role_update", [
        guild, before, after 
    ]

def export():
    return guild_role_update