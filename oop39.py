class SequenceIterable:
    def __init__(self, inList):
        self.iterList = inList
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == len(self.iterList):
            raise StopIteration
        return self.iterList[self.start]


container = SequenceIterable([1, 5, 4, 6, 43, True, "hello"])
for i in container:
    print(i)


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
