import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Guild
    
async def guild_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    guild = Guild(client, **event.data)

    for channel in guild.channels:
        client.channels.append(channel)

    for user in guild.users:
        client.users.append(user)

    client.guilds.append(guild)

    if guild.id in client.unavailable_guilds:
        client.unavailable_guilds.remove(guild.id)

        return "on_guild_cache", [
            guild
        ]

    return "on_guild_join", [
        guild
    ]

def export():
    return guild_create