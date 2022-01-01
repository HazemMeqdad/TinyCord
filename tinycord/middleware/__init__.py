import typing

from glob import glob
from importlib import import_module

def get_middlewares() -> typing.Dict[str, typing.Union[typing.Callable, typing.Awaitable]]:
    """
        This function is used to get all the middlewares. from the middleware folder.
    """
    middlewares: typing.Dict[str, typing.Union[typing.Callable, typing.Awaitable]] = {}

    for file in glob("tinycord/middleware/*.py"):

        event = file.split('/')[-1].split('.')[0].split(u'\u005c')[-1]

        try:
            module: module = import_module(f".{event}", package=__name__)
            middlewares[event] = getattr(module, 'export')()

        except ModuleNotFoundError:
            continue

        except AttributeError:
            continue

    return middlewares