class Hashable:
    def __hash__(self):
        """
            This function is used to hash the object.
        """
        return self.id >> 22
    
    def __repr__(self) -> str:
        """
            This function is used to represent the object.
        """
        return f'<{self.__class__.__name__} {self.id}>'

class EnumMixin:
    def __str__(self):
        """
            This function is used to get the string value of the enum.
        """
        return str(self.name)
    
    def __int__(self):
        """
            This function is used to get the int value of the enum. 
        """
        return int(self.value)