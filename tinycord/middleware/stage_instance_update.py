import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import StageChannel
    
async def stage_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    after = StageChannel(client, **event.data['channel'])
    before = client.get_channel(after.id)
    guild = client.get_guild(after.guild_id)

    guild.channels[str(after.id)] = after
    client.channels[str(after.id)] = after

    return "on_stage_update", [
        guild, before, after
    ]


def export():
    return stage_update