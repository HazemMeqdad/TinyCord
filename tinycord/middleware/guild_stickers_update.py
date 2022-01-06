import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Sticker
    
async def guild_sticker_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a guild's stickers have been updated.
        It does parse the stickers data, update the data and update the cache and return the event with the args.

        Parameters
        ----------
        client : `Client`
            The main client.
        gateway : `Gateway`
            The gateway that dispatched the event.
        event : `GatewayDispatch`
            The event that was dispatched.
    """
    guild = client.get_guild(event.data["guild_id"])
    """ The guild that the sticker were updated in. """

    after = {sticker['id']: Sticker(client, **sticker) for sticker in event.data['stickers']}
    """ The new sticker. """

    before = {sticker.id: sticker for sticker in guild.stickers if sticker.id in after}
    """ The old sticker from the cache. """

    guild.emojis.update(after)
    """ Update the cache. """

    return "on_guild_stickers_update", [
        guild, before, after
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return guild_sticker_update