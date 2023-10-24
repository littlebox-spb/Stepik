class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} {self.suit}"


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if len(self.cards) <= self.index:
            raise StopIteration
        card = self.cards[self.index]
        self.index += 1
        return card


deck = Deck()
for card in deck:
    print(card)
