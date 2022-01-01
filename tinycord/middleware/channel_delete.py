import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

async def channel_delete(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    channel = client.get_channel(event.data["id"])
    guild = client.get_guild(channel.guild_id)

    try:
        del client.channels[str(channel.id)]
        del guild.channels[str(channel.id)]
    except KeyError:
        pass

    return "on_channel_delete", [
        guild, channel
    ]

def export():
    return channel_delete