import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import StageChannel
    
async def stage_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    guild = client.get_guild(event.data['guild_id'])
    stage = client.get_channel(event.data['id'])

    del client.channels[str(stage.id)]
    del guild.channels[str(stage.id)]
    
    return "on_stage_delete", [
        guild, stage
    ]


def export():
    return stage_create