import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import User
    
async def user_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    after = User(client, **event.data['user'])
    before = client.get_user(after.id)

    return "on_user_update", [
        before, after
    ]

def export():
    return user_update