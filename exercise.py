# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library
# class and show how you can print all books, add a book and get the number of books using different methods. Show that your
# program doesnt persist the books after the program is stopped!

# Library Management Software

class Library():
    def __init__(self):
        self.no_of_books = 0
        self.books = []
    
    def addBook(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)
        
    def Show(self):
        print(f"There are {self.no_of_books} and they are \n")
        for book in self.books:
            print(book)
        
b1 = Library()
b1.addBook("physics")
b1.addBook("maths")
b1.Show()

  




