# class InfinityIterator:
#     def __init__(self, start=0):
#         self.current = start - 10

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.current += 10
#         return self.current


# for i in InfinityIterator(7):
#     print(i)


# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages


# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def __iter__(self):
#         return LibraryIterator(
#             self.books
#         )  # тут определите, что будете передавать итератору


# class LibraryIterator:
#     def __init__(self, books):
#         self.pages = []
#         for i in range(len(books)):
#             self.pages.extend(books[i].pages)
#         self.start = -1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.start += 1
#         if self.start == len(self.pages):
#             raise StopIteration
#         return self.pages[self.start]


# # Пример использования
# book1 = Book("Book 1", ["Page 1", "Page 2", "Page 3", "Page 4"])
# book2 = Book("Book 2", ["Page A", "Page B", "Page C"])
# book3 = Book("Book 3", ["Сhapter 1", "Сhapter 2"])

# library = Library()
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# # Используем вложенный итератор для обхода страниц в библиотеке
# for page in library:
#     print(page)


class FibonacciIterator:
    def __init__(self, stop):
        self.stop = stop
        self.previous = 0
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop and self.previous > 0:
            raise StopIteration
        if self.previous > 0:
            self.previous, self.current = self.current, self.previous
            self.current = self.current + self.previous
        else:
            self.previous = 1
        return self.current


fibonacci_iter = FibonacciIterator(0)

for number in fibonacci_iter:
    print(number)


# class StackIterator:
#     def __init__(self, stack):
#         self.stack = stack
#         self.start = len(stack.items)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.start -= 1
#         if self.start == -1:
#             raise StopIteration
#         return self.stack.items[self.start]


# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if len(self.items) == 0:
#             print("Empty Stack")
#         else:
#             return self.items.pop()

#     def peek(self):
#         if len(self.items) == 0:
#             print("Empty Stack")
#         else:
#             return self.items[-1]

#     def is_empty(self):
#         return len(self.items) == 0

#     def size(self):
#         return len(self.items)

#     def __iter__(self):
#         return StackIterator(self)


# stack = Stack()

# stack.push(100)
# stack.push(True)
# stack.push("hello")
# stack.push("world")

# # Используем итератор для обхода стека
# for item in stack:
#     print(item)

# class SequenceIterable:
# def __init__(self, inList):
#     self.iterList = inList
#     self.start = -1

# def __init__(self, inList):
#     nchet = []
#     self.iterList = []
#     for i in range(len(inList)):
#         if i % 2 == 0:
#             self.iterList.append(inList[i])
#         else:
#             nchet.append(inList[i])
#     self.iterList.extend(nchet)
#     self.start = -1

# def __iter__(self):
#     return self

# def __next__(self):
#     self.start += 1
#     if self.start == len(self.iterList):
#         raise StopIteration
#     return self.iterList[self.start]

#     def __next__(self):
#         self.start += 1
#         if self.start == len(self.iterList):
#             raise StopIteration
#         return self.iterList[self.start]


# container = SequenceIterable([1, 5, 4, 6, 43, True, "hello"])
# for i in container:
#     print(i)


# class FileReader:
#     def __init__(self, filename):
#         self.file = open(filename)

#     def __iter__(self):
#         self.file.seek(0)
#         return self

#     def __next__(self):
#         return next(self.file).rstrip('\n')

# for line in FileReader('loremm.txt'):
#     print(line)

# class Card:
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit

#     def __str__(self):
#         return f"{self.rank} {self.suit}"


# class Deck:
#     ranks = [str(n) for n in range(2, 11)] + list("JQKA")
#     suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

#     def __init__(self):
#         self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

#     def __iter__(self):
#         self.index = 0
#         return self

#     def __next__(self):
#         if len(self.cards) <= self.index:
#             raise StopIteration
#         card = self.cards[self.index]
#         self.index += 1
#         return card


# deck = Deck()
# for card in deck:
#     print(card)
