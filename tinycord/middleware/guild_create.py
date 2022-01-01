import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Guild
    
async def guild_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    guild = Guild(client, **event.data)

    for id, channel in guild.channels.items():
        client.channels[id] = channel
        
    for id, user in guild.users.items():
        client.users[id] = user

    client.guilds[str(guild.id)] = guild

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