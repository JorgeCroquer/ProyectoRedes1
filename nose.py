from Classes.Card import Card
from Classes.Deck import Deck
from Classes.Player import Player
import pygame,sys
import msvcrt
import sys
import serial
import io
import random 
import time
import threading
import keyboard


#SE INICIA LAS CONEXIONES
#
#
########################

#if maestro:

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

players = [player1, player2, player3,player4]

#AQUI SE DEBEN MANDAR LAS CARTAS A CADA UNO
#
#
###########################################

#CADA ESCLAVO COPIA SUS CARTAS Y LA MAESTRA LAS SUYAS#

Direction = 1 #1 para sentido horario. -1 para sentido antihorario

playerTurn = 0 #Turno de jugador

numPlayers = len(players)

discards.append(Deck.cards.pop(0)) #Agarramos la primera carta del mazo para ser la primera sobre la cual jugar

#Chequeamos que no se arranque con un comodin o con un Doble Manotazo
while discards[-1].colour == 'Comodin' or discards[-1].value == 'Doble manotazo':
    discards.append(Deck.cards.pop(0))

#Rescatamos la lista de colores
colourList = Deck.colours
#Y le quitamos el 4, que es Comodin
colourList.pop(4);

#Inicializamos el color
currentColour = discards[-1].colour #Variable para gestionar los cambios de color

#Variable para llevar la cantidad de Doble Manotazos que se han jugado en cadena
DobleManotazoTimes= 0

playing = True #Variable que indica si el juego sigue activo

while playing:

    #Si el jugador puede jugar:
    if players[playerTurn].canPlay(discards[-1],Deck,currentColour,DobleManotazoTimes):
        #MENSAJE DE SI PUEDES JUGAR CON TOPE
        #EN ESCLAVO SE ELIGE CARTA VALIDA
        #ESPERA A RECIBIR CARTA JUGADA
        #RECIBO LA CARTA Y EMPIEZO A HACER EFECTOS
        print()
    else:
        #SE PRESIONA BOTON PARA PEDIR CARTAS
        #MENSAJE DE NO PUEDES JUGAR + LAS DOS CARTAS QUE CARGA
        





##ESCLAVOOOO
jugador 1 
hand = [0,1,2,3,4] #ESTE ES SU MAZO
tope = carta recibida #RECIBE CARTA

#AQUI VERIFICO
while numCardChosen == -1: 
            print("Elige una carta para jugar")
            try:
                numCardChosen = int(input())
                #El numero que elija debe estar en su mazo
                if not (1 <= numCardChosen <= len(hand):
                    #Se salio del rango de su mazo
                    raise Exception
            
                #Esta linea es complicada.
                #Se elige del arreglo de jugadores el que tenga el turno
                #Luego se elige de la mano (arreglo hand) la carta [numCardChosen-1] y se rescata su color y valor        
                if (hand[numCardChosen-1].colour == "Comodin"
                    or hand[numCardChosen-1].colour == tope.color 
                    or hand[numCardChosen-1].value == tope.value):

                        cartaParaMandar = hand[numCardChosen-1]

                    
                    
                    
                else:
                    print("No puedes jugar esa carta")
                    numCardChosen = -1 #0 otra vez, para que el ciclo se repita

##MANDAR CARTA
