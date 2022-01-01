import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import User

async def guild_ban_add(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    user = User(client, **event.data['user'])
    guild = client.get_guild(event.data['guild_id'])

    return "on_ban_add", [
        guild, user
    ]

def export():
    return guild_ban_add