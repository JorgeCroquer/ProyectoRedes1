from Card import Card
import random


# clase para el mazo

class Deck:
    cards = []

    #Contructor
    def __init__(self):
        colours = ["Rojo","Verde","Azul","Amarillo", "Comodin"]
        values = [1,2,3,4,5,6,7,8,9,"Doble manotazo", "Reversa", "Salta", "Tira un color"]

        wilds = ["Cambia color", "Ataque"]

        for colour in colours:
            if colour == "Comodin":
                    for wild in wilds:
                        card = Card (colour, wild)
                        self.cards.append(card)
                        self.cards.append(card)
                        self.cards.append(card)
                        self.cards.append(card)
            else:
                for value in values:        
                    card = Card(colour, value)
                    self.cards.append(card)
                    self.cards.append(card)

        card = Card("Comodin","Cuádruple manotazo")
        self.cards.append(card)


    #Metodo para barajear el mazo
    def shuffleDeck(self):
        for cardPosition in range(len(self.cards)):
            #Por cada carta en el mazo se genera una posicion aleatoria y se intercambia con la que esta en esa posicion
            randPosition = random.randint(0,len(self.cards)-1)
            self.cards[cardPosition], self.cards[randPosition] = self.cards[randPosition], self.cards[cardPosition]





    


                





    

