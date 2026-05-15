from models.library_manager import LibraryManager
from models.book import Book
from models.author import Author

def main():
    manager = LibraryManager()

    # Add some initial books to the collection to facilitate testing.
    a1 = Author("Brian Khrisna", "Indonesia")
    a2 = Author("Pramoedya", "Indonesia")
    a3 = Author("J.K Rowling", "England")
    a4 = Author("Paulo Coelho", "Brazil")
    a5 = Author("Tan Malaka", "Indonesia")
    a6 = Author("Albert Camus", "France")

    manager.collection.append(Book(606, "The Darkest Side of Heaven", a1))
    manager.collection.append(Book(202, "Child of All Nations", a2))
    manager.collection.append(Book(505, "Magic World", a3))
    manager.collection.append(Book(101, "The Alchemist", a4))
    manager.collection.append(Book(404, "Madilog", a5))
    manager.collection.append(Book(303, "The Myth of Sisyphus", a6))

    # Display menu repeatedly until the user selects menu option 5.
    while True:
        print("\n=============================================")
        print("   LIBSEARCH - DIGITAL ARCHIVE (ASSOCIATION)")
        print("=============================================")
        print("1. Add New Book")
        print("2. Display All Collection")
        print("3. Sort Collection (Bubble Sort)")
        print("4. Search Book (Binary Search)")
        print("5. Exit\n")

        choice = input("Select Menu (1-5): ")

        if choice == '1':
            print("\nNew Book Addition Form")
            manager.add_new_book()
        elif choice == '2':
            manager.display_collection()
        elif choice == '3':
            manager.sort_collection()
        elif choice == '4':
            try:
                target_id = int(input("Enter the Book ID to search: "))
                manager.search_book(target_id)
            except ValueError:
                print("[ERROR] ID must be a number.")
        elif choice == '5':
            break
        else:
            print("[WARNING] Invalid input!")

if __name__ == "__main__":
    main()