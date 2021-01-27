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

    # NOTA: CUANDO EL JUGADOR JUEGE UNA CARTA DEBERIA CORRER ESTA FUNCIÓN

    def asignHand(self): #le asigna a cada carta su posicion correspondiente en la pantall
        y=0              #toma en cuenta la cantidad de cartas para reordenarlas   
        if len(self.hand) < 8:
            for x in range(len(self.hand)):
                self.hand[x].x = 180+x*110
                self.hand[x].y = 520
        else:
            for x in range(int(len(self.hand)/2)):
                self.hand[x].x = 220+x*110
                self.hand[x].y = 470
            for x in range(int(len(self.hand)/2),len(self.hand)):
                self.hand[x].x = 200+y*110
                self.hand[x].y = 600 
                y=y+1

    def draw(self,numCards,deck):
        #numCards -= 1;
        for x in range(numCards):
            self.hand.append(deck.cards.pop(0))
        for x in range(len(self.hand)):
            self.hand[x].surface = self.identificar(self.hand[x])
        self.asignHand()    
    
    def canPlay(self,discardCard):
        for card in self.hand:
            if card.colour == "Comodin":
                return True
            elif card.colour == discardCard.colour or card.value == discardCard.value:
                return True
        return False

    def showHand(self):   #Enseña por consola la mano del jugador
        print("Tu mano: ")
        print ("")
        for card in self.hand:
            print("1) ", card.color, card.value)
        print ("")
        print ("-----------------")