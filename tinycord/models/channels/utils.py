from .channel import BaseChannel
from .dm import DMChannel
from .news import NewsChannel
from .text import TextChannel
from .voice import VoiceChannel
from ...utils import Snowflake

def deserialize_channel(client, **data):
    """
    This is the deserialize_channel function.
    
    Parameters
    ----------
    client : `Client`
        The main client.
    guild_id : `Snowflake`
        The guild id.
    data : `typing.Dict`
        The data that is used to create the channel.
    
    Returns
    -------
        Channel
    """
    guild_id = Snowflake(data.get('guild_id'))
    if data['type'] == 0:
        return TextChannel(client, guild_id, **data)
    elif data['type'] == 2:
        return VoiceChannel(client, guild_id, **data)
    elif data['type'] == 4:
        return NewsChannel(client, guild_id, **data)
    elif data['type'] == 5:
        return DMChannel(client, guild_id, **data)
    else:
        return BaseChannel(client, guild_id, **data)