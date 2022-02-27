class Book:
    def __init__(self, title, author, dewey, isbn):
        self.title = title.title()
        self.author = author
        self.dewey = dewey
        self.isbn = isbn
        self.available = True
        self.borrower = None
        book_list.append(self)

    def book_details(self):
        print(self.title)
        print(self.author)
        print(self.dewey)
        print(self.isbn)
        print(self.available)
        print(self.borrower)
        print("########################")


def print_info():
    for book in book_list:
        book.book_details()


class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.fees = 0.0
        self.Borrowed_books = []
        user_list.append(self)

    def user_details(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("Fees:", self.fees)
        print("########################")


def print_user():
    for i in user_list:
        i.user_details()


def add_user():
    name = input("Enter a new users name: ").title()
    address = input("Enter users address: ")
    User(name, address)
    print(name, address, "Has been added to user list")


def add_book():
    title = input("Enter a new books title: ").title()
    author = input("Enter a new books author: ").title()
    dewey = input("Enter a new books dewey code: ").upper()
    isbn = input("Enter a new books isbn code: ")
    Book(title, author, dewey, isbn)
    print(f"{title} has been added to the book list")


def find_user():
    user_to_find = input("Enter the name of the user: ").title()
    for user in user_list:
        if user.name == user_to_find:
            print(f"Hi {user_to_find}")
            return user
    print("Sorry no user with that name has been found")
    return None


def find_book():
    book_to_find = input("Enter the name of the book: ").title()
    for book in book_list:
        if book.title == book_to_find:
            print(f"The book '{book_to_find}' is in the catalogue")
            return book
    print("Sorry no book with that title is in the catalogue")
    return None


def lend_book():
    user = find_user()
    print()
    if user:
        book = find_book()
        if book.available:
            confirm = input("Type Y if you want to borrow this book: ").upper()
            if confirm == "Y":
                print(f"Book Title: {book.title} is now out on loan to"
                      f" {user.name}")
                book.available = False
                book.borrower = user.name
                user.Borrowed_books.append(book.title)
        else:
            print(f"Sorry, {book.title} is out on loan already")


def return_book():
    user = find_user()
    print()
    if user:
        book = find_book()
        if not book.available:
            confirm = input("Type Y if you want to return this book: ").upper()
            if confirm == "Y":
                print(f"Book Title: {book.title} is now returned to the "
                      f"library")
                book.available = True
                book.borrower = user.name
                user.Borrowed_books.remove(book.title)
        else:
            print(f"Sorry, '{book.title}' is on loan to someone else")


book_list = []
user_list = []

Book("Lord of the Rings", "J.R.R Tolkien", "TOL", "9780261103252")
Book("The Hunger Games", "Suzanne Collins", "COL", "9781407132082")
Book("A Tale of Two Cities", "Charles Dickens", "DIC", "9781853262647")
Book("Harry Potter", "J.K Rowling", "ROW", "9780439321624")

User("John", "12 Example St")
User("Susan", "1011 Binary Rd")
User("Paul", "25 Apple Tree Ave")
User("Mary", "8 Moon Cres")

new_action = True
while new_action:
    print("1. Lend Book")
    print("2. Return Book")
    print("3. Add User")
    print("4. Add Book")
    print("5. Exit")
    choice = input("\n What would you like to do: ")
    if choice == "1":
        lend_book()
    elif choice == "2":
        return_book()
    elif choice == "3":
        add_user()
    elif choice == "4":
        add_book()
    elif choice == "5":
        new_action = False
    else:
        print("That is not a menu item please try again ")
print("Thank you for using the Library System")
