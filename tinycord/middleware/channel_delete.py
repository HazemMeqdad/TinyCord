import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

async def channel_delete(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    channel = client.get_channel(event.data["id"])
    guild = client.get_guild(channel.guild_id)

    try:
        for channel in client.channels:
            if channel.id == channel.id:
                client.channels.remove(channel)

        for channel in guild.channels:
            if channel.id == channel.id:
                guild.channels.remove(channel)
    except:
        pass

    return "on_channel_delete", [
        guild, channel
    ]

def export():
    return channel_delete