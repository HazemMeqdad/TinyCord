import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

async def guild_role_delete(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    guild = client.get_guild(event.data["guild_id"])
    role = guild.get_role(event.data["role_id"])

    try:
        guild.roles.remove(role)
    except:
        pass

    return "on_role_delete", [
        guild, role 
    ]

def export():
    return guild_role_delete