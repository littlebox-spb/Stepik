class Author:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Author: {self.name}"


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title}, {self.author}"


a1 = Author("Я")
b1 = Book("Моя книга!", a1)
print(b1)
