from abc import ABC, abstractmethod

class LibraryItem(ABC):
    """
    An abstract base class that serves as a blueprint for all items in the library.
    """
    def __init__(self, item_id: int, title: str):
        # Used as a unique identifier that can be accessed by subclasses.
        self.item_id = item_id
        # Title cannot be directly modified from outside the class to maintain data integrity (Encapsulation).
        self.__title = title

    @abstractmethod
    def description(self) -> str:
        # A contract that enforces each subclass to define how they display their own information.
        pass

    def get_id(self) -> int:
        # Getter method to provide read access to the attribute.
        return self.item_id

    def get_title(self) -> str:
        # Getter method to provide read access to the hidden attribute.
        return self.__title