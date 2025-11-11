# Library management System


class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)
    
    def showInfo(self):
        print(f"The Library has {self.noBooks} books. The books are ")
        for book in self.books:
            print(book)


l1 = Library()
l1.addBook("")
l1.addBook("Batman Comics")
l1.addBook("Super-Man Comics")
l1.addBook("Spider-Man Comics")
l1.addBook("The Sandman")
l1.addBook("Blankets by Craig Thompson")
l1.showInfo()