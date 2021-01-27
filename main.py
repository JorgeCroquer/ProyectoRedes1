from Classes.Card import Card
from Classes.Deck import Deck
from Classes.Player import Player
import pygame,sys

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

players = [player1, player2, player3,player4]  #Array con todos los players

Direction = 1 #1 para sentido horario. -1 para sentido antihorario

playerTurn = 0 #Turno de jugador

discards.append(Deck.cards.pop(0)) #Agarramos la primera carta del mazo para ser la primera sobre la cual jugar

playing = True #Variable que indica si el juego sigue activo

print(discards[0].value)



if discards[0].colour == "Comodin":
    if discards[0].value == "Ataque":
        #hay que seleccionar a un jugador para que agarre 2 cartas FALTA
        print("Ataque") #este print() es solo para que el programa pueda compilar mientras
    elif discards[0].value== "Cuádruple manotazo":
        players[playerTurn + 1].draw(4,Deck)
        print("Cuádruple manotazo") #este print() es solo para que el programa pueda compilar mientras
    #Cualquier comodin cambia el color FALTA
elif discards[0].value == "Doble manotazo":
    players[playerTurn + 1].draw(2,Deck)
    print("Doble manotazo") #este print() es solo para que el programa pueda compilar mientras
elif discards[0].value == "Reversa":
    Direction *= -1
    print("Reversa") #este print() es solo para que el programa pueda compilar mientras
elif discards[0].value == "Salta":
    playerTurn += Direction
    print("Salta") #este print() es solo para que el programa pueda compilar mientras
elif discards[0].value == "Tira un color":
    #El jugador actual debe tirar todoas las cartas con el mismo color FALTA
    print("Tira un color") #este print() es solo para que el programa pueda compilar mientras
else: 
    #Es una carta normal
    print("Es normal")
















