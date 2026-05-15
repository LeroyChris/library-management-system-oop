from .book import Book
from .author import Author

class LibraryManager:
    """
    A manager class that serves as the brain of the system, handling storage, sorting, and searching operations.
    """
    def __init__(self):
        # Stores a collection of Book objects.
        self.collection = []
        # A flag indicating whether the current book list is sorted or unsorted.
        self.is_sorted = False

    def validate_unique_id(self, new_id: int) -> bool:
        # Iterates through self.collection. If an ID matching new_id is found, the function returns False.
        for book in self.collection:
            if book.get_id() == new_id:
                return False
        return True

    def add_new_book(self) -> None:
        # Requests and validates the ID input.
        try:
            new_id = int(input("Enter Book ID (Number): "))
        except ValueError:
            print("[ERROR] ID must be a number.")
            return

        if not self.validate_unique_id(new_id):
            print("[ERROR] ID already registered. Use a different ID.")
            return

        # If ID is valid, request author data.
        title = input("Enter Book Title: ")
        author_name = input("Enter Author Name: ")
        nationality = input("Enter Author's Country of Origin: ")

        # Create an Author object first.
        new_author = Author(author_name, nationality)
        
        # Create a Book object by passing the Author object to it.
        new_book = Book(new_id, title, new_author)
        
        # Add it to the list and change sorted status to False.
        self.collection.append(new_book)
        self.is_sorted = False
        
        print(f"[SUCCESS] '{title}' by {author_name} has been added successfully.")

    def display_collection(self) -> None:
        print("ID\t| Book Information")
        if not self.collection:
            return
        for book in self.collection:
            print(f"[{book.get_id()}]\t| {book.description()}")

    def sort_collection(self) -> None:
        # Uses neighbor comparison (Bubble Sort).
        n = len(self.collection)
        for i in range(n):
            for j in range(0, n - i - 1):
                # If current ID > right ID, swap the positions of objects.
                if self.collection[j].get_id() > self.collection[j + 1].get_id():
                    self.collection[j], self.collection[j + 1] = self.collection[j + 1], self.collection[j]
        
        self.is_sorted = True
        print("[SYSTEM] Collection has been sorted successfully.")

    def search_book(self, target_id: int) -> None:
        # Ensures data is sorted (if not, call sort_collection).
        # If data is not sorted, the result will appear as shown below.
        if not self.is_sorted:
            print("[WARNING] Please sort the data first!")
            print(f"[RESULT] ID {target_id} not found.")
            return

        left = 0
        right = len(self.collection) - 1
        found = False

        while left <= right:
            # Determine the midpoint.
            mid = (left + right) // 2
            book_mid = self.collection[mid]
            
            # If target_id equals mid, data is found.
            if book_mid.get_id() == target_id:
                print(f"[FOUND] Book: {book_mid.get_title()} | Author: {book_mid.author.name}")
                print(f"Author Details: {book_mid.author.__str__()}")
                found = True
                break
            elif book_mid.get_id() < target_id:
                # If not, narrow the search space to the right or left half.
                left = mid + 1
            else:
                right = mid - 1

        if not found:
            print(f"[RESULT] ID {target_id} not found.")