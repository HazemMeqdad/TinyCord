import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import StageChannel
    
async def stage_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    after = StageChannel(client, **event.data['channel'])
    before = client.get_channel(after.id)
    guild = client.get_guild(after.guild_id)

    for channel in guild.channels:
        if channel.id == after.id:
            guild.channels.remove(channel)

    guild.channels.append(after)

    for channel in client.channels:
        if channel.id == after.id:
            client.channels.remove(channel)

    client.channels.append(after)

    return "on_stage_update", [
        guild, before, after
    ]


def export():
    return stage_create