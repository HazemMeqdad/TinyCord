import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch


async def on_member_delete(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    guild = client.get_guild(event.data["guild_id"])
    member = guild.get_member(event.data["user"]["id"])

    try:
        del guild.members[str(member.id)]
    except KeyError:
        pass

    return "on_member_delete", [
        guild, member
    ]

def export():
    return on_member_delete