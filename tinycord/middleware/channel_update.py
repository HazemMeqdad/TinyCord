import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import deserialize_channel
    
async def channel_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:

    after = deserialize_channel(client, **event.data)
    before = client.get_channel(after.id)
    guild = client.get_guild(after.guild_id)
    
    try:

        for channel in guild.channels:
            if channel.id == after.id:
                guild.channels.remove(channel)

        for channel in client.channels:
            if channel.id == after.id:
                client.channels.remove(channel)
            
        guild.channels.append(after)
        client.channels.append(after)
        
    except:
        pass

    return "on_channel_update", [
        guild, before, after
    ]

def export():
    return channel_update