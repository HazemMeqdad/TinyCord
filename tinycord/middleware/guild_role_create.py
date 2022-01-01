import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Role

async def guild_role_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    role = Role(client, **event.data)
    guild = client.get_guild(role.guild_id)

    guild.roles[str(role.id)] = role

    return "on_role_create", [
        guild, role 
    ]

def export():
    return guild_role_create