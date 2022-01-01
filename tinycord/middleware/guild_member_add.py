import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Member

async def guild_member_add(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    member = Member(client, **event.data)
    guild = client.get_guild(member.guild_id)

    guild.members.append(member)

    return "on_member_create", [
        guild, member
    ]

def export():
    return guild_member_add