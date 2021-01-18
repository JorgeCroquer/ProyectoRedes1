class Player:
    def __init__(self):
        self.hand = []

    def draw(self,numCards,deck):
        #numCards -= 1;
        for x in range(numCards):
            self.hand.append(deck.cards.pop(0))
    
    def canPlay(self,discardCard):
        for card in self.hand:
            if card.colour == "Comodin":
                return True
            elif card.colour == discardCard.colour or card.value == discardCard.value:
                return True
        return False