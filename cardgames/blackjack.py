
from cardgames.utils import cards

class Player:

    def __init__(self, name, buy_in):
        self._name=name
        self._balance=buy_in
        self._hand = []

    def __repr__(self):
        return "Player Name: " + self._name + "\nCurrent Balance: "+str(self._balance)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, hand):
        self._hand = hand

    def hit(self, cards):
        self.hand =  self.hand + cards

    def reset_hand(self):
        self.hand = []

    def getscore(self):
        score = 0

        # move all aces to end of list
        aces=[]
        for c in self.hand:
            if c.rank == "A":
                aces.append(c)
                self.hand.remove(c)
        self.hand += aces

        for c in self.hand:
            try:
                score += int(c.rank)
            except:
                if c.rank in ["J", "Q", "K"]:
                    score += 10
                elif score + 11 > 21:
                    score += 1
                else:
                    score += 11

        return score

    def payout(self, bet, outcome):
        self.balance += bet*outcome


def PlayHand(player, bet, dealer_stand = 17, num_packs=1):
    result = {
        "Blackjack": 1.5,
        "Win": 1,
        "Push": 0,
        "Loss": -1,
        "Bust": -1,
        "Dealer Blackjack": -1
    }

    #initialise dealer and deck objects
    dealer = Player('Dealer', 1)
    deck = cards.Deck(num_packs)

    #deal starting hands
    player.hand = deck.dealcards(2)
    dealer.hand = deck.dealcards(2)

    #present starting hands
    print("Dealers first card: ")
    print(dealer.hand[0])

    print(player.hand)
    print("You're on: {}".format(player.getscore()))

    # check for blackjack
    if player.getscore()==21 and dealer.getscore() == 21:
        outcome = "Push"
    elif player.getscore() == 21 and dealer.getscore() != 21:
        outcome = "Blackjack"
    elif player.getscore() != 21 and dealer.getscore() == 21:
        outcome = "Dealer Blackjack"
    else:
        #player's turn
        player_action = input("Hit or Stand [H/S]: ")
        while player_action.upper() == "H" and player.getscore() < 21:
            player.hit(deck.dealcards())

            print(player.hand)
            print("You're on: {}".format(player.getscore()))

            if player.getscore() >= 21:
                break

            player_action = input("Hit or Stand [H/S]: ")

        if player.getscore() > 21:
            outcome = "Bust"
        else:
            # dealer's turn
            while dealer.getscore() < dealer_stand:
                dealer.hit(deck.dealcards())
            print(dealer.hand)
            print(dealer.getscore())
            if dealer.getscore() > 21:
                outcome = "Win"
            else:
                if player.getscore() > dealer.getscore():
                    outcome = "Win"
                elif player.getscore() == dealer.getscore():
                    outcome = "Push"
                else:
                    outcome = "Loss"

    print(outcome)
    player.payout(bet, result[outcome])
    player.reset_hand()
    return player


def Play(player):

    response = input("Play a hand [Y/N]: ")
    mybet = int(input("How much would you like to bet: "))

    while response.upper() == 'Y' and player.balance > 0:
        MyPlayer = PlayHand(player, mybet)
        print(player)
        response = input("Play another hand [Y/N]: ")

    print(player)
    print("Thanks for playing!")
    exit()
