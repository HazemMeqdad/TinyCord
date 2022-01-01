import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Member

async def guild_member_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    after = Member(client, **event.data)
    guild = client.get_guild(after.guild_id)
    before = guild.get_member(after.id)

    try:
        guild.members.remove(before)
        guild.members.append(after)
    except:
        pass

    return "on_member_update", [
        guild, before, after
    ]

def export():
    return guild_member_update