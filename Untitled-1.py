
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            print(self.title, "has been borrowed.")
        else:
            print(self.title, "is already borrowed.")

    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "is already available.")


book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("Diary of a Wimpy Kid", "Jeff Kinney")

book1.borrow()
book2.borrow()
book3.borrow()

book1.return_book()
book2.return_book()
book3.return_book()