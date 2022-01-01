import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import StageChannel
    
async def stage_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    guild = client.get_guild(event.data['guild_id'])
    stage = client.get_channel(event.data['id'])

    for channel in guild.channels:
        if channel.id == stage.id:
            guild.channels.remove(channel)
        
    for channel in client.channels:
        if channel.id == stage.id:
            client.channels.remove(channel)

    return "on_stage_delete", [
        guild, stage
    ]


def export():
    return stage_create