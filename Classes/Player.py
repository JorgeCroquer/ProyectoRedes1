class Player:
    def __init__(self):
        self.hand = []

    def draw(self,numCards,deck):
        #numCards -= 1;
        for x in range(numCards):
            self.hand.append(deck.cards.pop(0))
