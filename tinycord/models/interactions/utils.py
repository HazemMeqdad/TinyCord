import typing
from .types import CommandApplictionTypes

def deserialize_command(client, **data):
    """
        |coro|
        This function is used to deserialize a command.
        Parameters
        ----------
        client : `Client`
            The main client.
        data : `dict`
            The data of the command.
    """
    if data["type"] == 1:
        return 

