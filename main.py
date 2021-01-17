from Classes.Player import Player
from Classes.Player import Player
from Classes.Card import Card
from Classes.Deck import Deck


#Se crean los jugadores
player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player()

#Se crea el mazo y se barajea
Deck = Deck()
Deck.shuffleDeck()

discards = [] #pila donde se van jugando las cartas

#Se reparten las cartas. Cada quien agarra 7 del Deck
player1.draw(7,Deck)
player2.draw(7,Deck)
player3.draw(7,Deck)
player4.draw(7,Deck)

Direction = 1 #1 para sentido horario. -1 para sentido antihorario

playerTurn = 0

discards.append(Deck.cards.pop(0)) #Agarramos la primera carta del mazo para ser la primera sobre la cual jugar

for x in range(len(Deck.cards)):
    print(x,Deck.cards[x].colour,Deck.cards[x].value)

