import pygame,sys
from Classes.Card import Card

class Player:
    def __init__(self):
        self.hand = []

    def identificar(self,cartaId):
        Mvalues = {
            1:"_1",
            2:"_2",
            3:"_3",
            4:"_4",
            5:"_5",
            6:"_6",
            7:"_7",
            8:"_8",
            9:"_9",
            "Doble manotazo":"_picker",
            "Reversa":"_reverse", 
            "Salta":"_skip" 
        }
        Mcolours = {
            "Azul":"blue",
            "Rojo":"red",
            "Amarillo":"yellow",
            "Verde":"Green"
        } 
        if cartaId.colour == "Comodin":
            carta = pygame.image.load('img/small/wild_color_changer.png').convert()
            return carta
        if cartaId.value == "Tira un color":
            carta = pygame.image.load('img/small/card_back_alt.png').convert()
            return carta    
        valor = Mvalues.get(cartaId.value,"card")
        color = Mcolours.get(cartaId.colour,"_back")
        carta = pygame.image.load('img/small/{}{}.png'.format(color,valor)).convert()
        return carta

    def draw(self,numCards,deck):
        #numCards -= 1;
        for x in range(numCards):
            self.hand.append(deck.cards.pop(0))
        for x in range(len(self.hand)):
            self.hand[x].surface = self.identificar(self.hand[x])
    
    def canPlay(self,discardCard):
        for card in self.hand:
            if card.colour == "Comodin":
                return True
            elif card.colour == discardCard.colour or card.value == discardCard.value:
                return True
        return False