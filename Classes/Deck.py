from Classes.Card import Card
import random
import pygame,sys


# clase para el mazo

class Deck:
    cards = []
    colours = ["Rojo","Verde","Azul","Amarillo", "Comodin"]
    values = [1,2,3,4,5,6,7,8,9,"Doble manotazo", "Reversa", "Salta", "Tira un color"]
    wilds = ["Cambia color", "Ataque"]
    #Contructor
    def __init__(self):
        

        for colour in self.colours:
            if colour == "Comodin":
                    for wild in self.wilds:
                        card = Card (colour, wild)
                        card.surface = self.identificar(card)
                        self.cards.append(card)
                        self.cards.append(card)
                        self.cards.append(card)
                        self.cards.append(card)
            else:
                for value in self.values:        
                    card = Card(colour, value)
                    card.surface = self.identificar(card)
                    self.cards.append(card)
                    self.cards.append(card)

        card = Card("Comodin","Cuadruple manotazo")
        card.surface = self.identificar(card)
        self.cards.append(card)

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
            "Doble manotazo":"_doble",
            "Reversa":"_reverse", 
            "Salta":"_skip",
            "Cambia color":"_wild", 
            "Ataque":"_ataque",
            "Tira un color":"_tiracolor",
            "Cuadruple manotazo":"_cuadruple"
        }
        Mcolours = {
            "Azul":"blue",
            "Rojo":"red",
            "Amarillo":"yellow",
            "Verde":"Green",
            "Comodin":"comodin"
        }
        valor = Mvalues.get(cartaId.value,"_back")
        color = Mcolours.get(cartaId.colour,"card")
        carta = pygame.image.load('img/{}{}.png'.format(color,valor)).convert()        
        return carta
    
    #Metodo para barajear el mazo
    def shuffleDeck(self):
        for cardPosition in range(len(self.cards)):
            #Por cada carta en el mazo se genera una posicion aleatoria y se intercambia con la que esta en esa posicion
            randPosition = random.randint(0,len(self.cards)-1)
            self.cards[cardPosition], self.cards[randPosition] = self.cards[randPosition], self.cards[cardPosition]

    def spitOutCards(self):
        spittedOutCards = []
        for x in range(random.randint(0,5)):       
            spittedOutCards.append(self.cards.pop(0))
        return spittedOutCards

    


    


                





    

