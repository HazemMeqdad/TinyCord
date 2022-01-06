import typing

if typing.TYPE_CHECKING:
    from ..client import Client
    from ..core import Gateway, GatewayDispatch

from ..models import Emoji
    
async def guild_emojis_update(client: "Client", gateway: "Gateway", event: "GatewayDispatch") -> typing.List[typing.Awaitable]:
    """
        |coro|
        This event called when a guild's emojis have been updated..
        It does parse the channel data, update the data and update the cache and return the event with the args.

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
    """ The guild that the emojis were updated in. """

    after = {emoji['id']: Emoji(client, **emoji) for emoji in event.data['emojis']}
    """ The new emojis. """

    before = {emoji.id: emoji for emoji in guild.emojis if emoji.id in after}
    """ The old emojis from the cache. """

    guild.emojis.update(after)
    """ Update the cache. """


    return "on_guild_emojis_update", [
        guild, before, after
    ]
    """ The event that was dispatched. """

def export():
    """ Exports the function. """
    return guild_emojis_update