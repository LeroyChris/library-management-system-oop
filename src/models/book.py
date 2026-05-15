from .library_item import LibraryItem
from .author import Author

class Book(LibraryItem):
    """
    A subclass of LibraryItem that represents a book and maintains an association relationship with the Author class.
    """
    def __init__(self, item_id: int, title: str, author_obj: Author):
        super().__init__(item_id, title)
        # This is the core of Association. This attribute stores a reference to an Author class object.
        self.author = author_obj

    def description(self) -> str:
        # Implementing Polymorphism. This method returns detailed book information.
        # The program "borrows" the name attribute from the Author object through the Book object.
        return f"Book: {self.get_title()}\n| Author: {self.author.name}"