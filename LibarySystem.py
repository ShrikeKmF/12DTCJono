class Book:
    def __init__(self, title, author, dewey, isbn):
        self.title = title
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
    author = input("Enter a new books author: ").author()
    dewey = input("Enter a new books dewey code: ").dewey()
    isbn = input("Enter a new books isbn code: ").isbn()
    Book(title, author, dewey, isbn)
    print(f"{title} has been added to the book list")



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

add_book()
print_info()
add_user()
print_user()
