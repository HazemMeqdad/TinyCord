import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import StageChannel
    
async def stage_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    stage = StageChannel(client, **event.data['channel'])
    guild = client.get_guild(stage.guild_id)

    guild.channels.append(stage)
    client.channels.append(stage)

    return "on_stage_create", [
        guild, stage
    ]

def export():
    return stage_create