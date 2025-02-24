import random as rand

#define card object
class Card:

    # define method for initialisation
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    # define string representation
    def __repr__(self):
        return self.rank + " of " + self.suit

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "spades", "diamonds", "clubs"]:
            self._suit=suit
        else:
            raise ValueError("Invalid Suit")

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, rank):
        if rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
            self._rank = rank
        else:
            raise ValueError("Invalid Rank")


class Deck:
    def __init__(self, num_packs=1):
        self._cards = []
        self.build(num_packs)
        self.shuffle()

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, cards):
        self._cards = cards

    def build(self, num_packs):
        suits = ["hearts", "spades", "diamonds", "clubs"]
        ranks = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        pack = [Card(r, s) for r in ranks for s in suits]

        self.cards = pack*num_packs

    def shuffle(self):
        rand.shuffle(self._cards)

    def size(self):
        return len(self.cards)

    def dealcards(self, num=1):
        res = []
        i = 0
        while i < num:
            res.append(self._cards.pop())
            i += 1

        return res