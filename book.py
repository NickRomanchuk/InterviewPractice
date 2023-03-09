class Book:

    x = 5

    def __init__(self):
        self.x = 10

    def display(self):
        print(self.x)
        print(Book.x)
    
b = Book()
b.display()