import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import SlashContext, Option

async def interaction_create(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when the client is ready.
        It does provide the client and the user that was ready.
        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    data = event.data
    # options = [Option(i["type"], name=i["name"], description=i["description"], required=)
    #            for i in data.get("data")["options"]]
    context = SlashContext(
        client, 
        event["type"],
        id=data["id"],
        application_id=data["application_id"],
        command_id=data.get("data")["id"],
        name=data.get("data")["name"],
        # options=,
    )

    return "on_interaction_create", [
        context
    ]
    """ The event that was dispatched. """


def export():
    """ Exports the function. """
    return interaction_create
