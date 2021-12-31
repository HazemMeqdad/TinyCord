import typing

class Snowflake(int):
    """
        This class is used to represent a snowflake.
        This is used to represent a snowflake.

        Attributes
        ----------
        MIN: int
            The minimum value of a snowflake.
        MAX: int
            The maximum value of a snowflake.
        EPOCH: int
            The sec of the eproch of Discord.
    """
    MIN = 0
    MAX = 2**63 - 1
    EPOCH = 1420070400000

    def __new__(cls, id: int) -> 'Snowflake':
        """
            This function is used to create a snowflake.
        """
        if type(id) is type(None):
            return None

        if not cls.MIN <= int(id) <= cls.MAX:
            raise ValueError(f'{id} is not a valid snowflake.')
        try:
            return super().__new__(cls, id)
        except TypeError:
            return None

    @property
    def timestamp(self) -> int:
        """
            This function is used to get the timestamp of the snowflake.
        """
        return (self >> 22) + self.EPOCH

    @property
    def worker_id(self) -> int:
        """
            This function is used to get the worker id of the snowflake.
        """
        return (self & 0x3E0000) >> 17

    @property
    def process_id(self) -> int:
        """
            This function is used to get the process id of the snowflake.
        """
        return (self & 0x1F000) >> 12

    @property
    def increment(self) -> int:
        """
            This function is used to get the increment of the snowflake.
        """
        return self & 0xFFF