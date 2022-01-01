import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import deserialize_channel
    
async def channel_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    channel = deserialize_channel(client, **event.data)
    guild = client.get_guild(channel.guild_id)
    
    client.channels.append(channel)
    guild.channels.append(channel)

    return "on_channel_create", [
        guild, channel
    ]

def export():
    return channel_create