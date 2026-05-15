class Author:
    """
    This class serves as an independent entity representing author data.
    """
    def __init__(self, name: str, nationality: str):
        # Stores the author's full name and country of origin.
        self.name = name
        self.nationality = nationality

    def __str__(self) -> str:
        # Returns the string representation of the object. In UML, this method is often called toString().
        # Returns text in the format Name (Country) each time the object is called by the print() command.
        return f"{self.name} ({self.nationality})"