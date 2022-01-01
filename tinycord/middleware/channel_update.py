import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import deserialize_channel
    
async def channel_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:

    after = deserialize_channel(client, **event.data)
    before = client.get_channel(after.id)
    guild = client.get_guild(after.guild_id)
    
    client.channels[str(after.id)] = after
    guild.channels[str(after.id)] = after

    return "on_channel_update", [
        guild, before, after
    ]

def export():
    return channel_update