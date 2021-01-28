from Classes.Card import Card
from Classes.Deck import Deck
from Classes.Player import Player
import pygame,sys
import msvcrt

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

#Bucle principal
while playing:

    #Verificamos que el mazo tenga mas de 10 cartas, para que no se quede vacio
    if len(Deck.cards) <= 30:
        for i in range(len(discards)-1):
            Deck.cards.append(discards.pop(0))   

    print ("")
    print ("-------------")
    print ("")
    print("jugador {}".format(playerTurn+1))
    print ("")

    #mostramos la carta del tope
    print("Carta en el tope de la pila: {} {}".format(discards[-1].colour, discards[-1].value))
    if (discards[-1].colour == "Comodin"):
        print('El color actual es {}'.format(currentColour))

    

    #Vemos si puede jugar
    if players[playerTurn].canPlay(discards[-1],Deck,currentColour,DobleManotazoTimes):

        #le mostramos su mano
        players[playerTurn].showHand()
        #Se inicializa la carta que se va a jugar
        numCardChosen = -1
        #Este while es para chequear que no seleccione algo invalido
        while numCardChosen == -1:
            print("Elige una carta para jugar")
            try:
                numCardChosen = int(input())
                #El numero que elija debe estar en su mazo
                if not (1 <= numCardChosen <= len(players[playerTurn].hand)):
                    #Se salio del rango de su mazo
                    raise Exception
            
                #Esta linea es complicada.
                #Se elige del arreglo de jugadores el que tenga el turno
                #Luego se elige de la mano (arreglo hand) la carta [numCardChosen-1] y se rescata su color y valor        
                if (players[playerTurn].hand[numCardChosen-1].colour == "Comodin"
                    or players[playerTurn].hand[numCardChosen-1].colour == currentColour 
                    or players[playerTurn].hand[numCardChosen-1].value == discards[-1].value):

                    print("{} {}".format(players[playerTurn].hand[numCardChosen-1].colour, 
                                    players[playerTurn].hand[numCardChosen-1].value))
                    discards.append(players[playerTurn].hand.pop(numCardChosen-1))
                    currentColour = discards[-1].colour
                    
                else:
                    print("No puedes jugar esa carta")
                    numCardChosen = -1 #0 otra vez, para que el ciclo se repita

                        
            except ValueError: 
                #Puso un caracter invalido
                print("Entrada invalida")
                print("")
            except Exception:
                #Se salio de su mazo
                print('Numero invalido')
                numCardChosen = -1
        

        print("")
        #Ahora que se jugó la carta, hay que ver que era para aplicar sus efectos
        #vamos con los comodines
        if discards[-1].colour == "Comodin":
            if discards[-1].value == "Ataque":
                print('')
                #Imprimos los jugadores
                for i in range(len(players)):
                    if (i != playerTurn):
                        print('{}) Jugador {}'.format(i+1, i+1))
                #Variable inicializada para el while
                print("")
                playerChosen = -1
                #Verificamos la eleccion
                while playerChosen == -1:
                    try:
                        playerChosen= int(input('Elije un jugador para atacar: '))-1
                        if not 0 <= playerChosen <= len(players)-1:
                            raise Exception
                        if playerChosen == playerTurn:
                            raise Exception
                    except ValueError:
                        print("Entrada invalida")
                        print("")
                        playerChosen = -1
                    except Exception:
                        if playerChosen == playerTurn:
                            print('¡ESE ERES TU!')
                        else:
                            print("Numero invalido")
                        print("")
                        playerChosen = -1
                #atacamos
                times = 0
                for times in range(2):
                    players[playerChosen].hand.extend(Deck.spitOutCards())
                print("Atacaste al jugador {}".format(playerChosen+1))
                print("")
            elif discards[-1].value== "Cuadruple manotazo":
                times = 0
                #Si esta en el ultimo jugador, le toca agarrar al primero (+direction)
                if playerTurn == len(players)-1 and Direction == 1:
                    for times in range(4):                   
                        players[0].hand.extend(Deck.spitOutCards())
                #Si esta en el primero, le toca agarrar al ultimo (-direction)
                elif playerTurn == 0 and Direction == -1:
                    for times in range(4):                   
                        players[len(players-1)].hand.extend(Deck.spitOutCards())
                else:
                    for times in range (4):
                        players[playerTurn+Direction].hand.extend(Deck.spitOutCards())                


            #variable aux
            i = 0
            #Mostramos los colores
            for colour in colourList:
                i += 1;
                print("{}) {}".format(i,colour))
            #Variable inicializada para el while
            print("")
            #Validamos su eleccion
            colourChosen = -1
            while colourChosen == -1:
                try:
                    colourChosen= int(input('Elije un color: '))-1
                    if not 0 <= colourChosen <= 3:
                        raise Exception
                except ValueError:
                    print("Entrada invalida")
                    print("")
                    colourChosen = -1
                except Exception:
                    print("Numero invalido")
                    print("")
                    colourChosen = -1
            #Cambiamos el color
            currentColour = colourList[colourChosen]
            print('Elegiste el color {}'.format(Deck.colours[colourChosen]))
        
        #Vamos con las demas
        elif discards[-1].value == "Doble manotazo":
            DobleManotazoTimes += 1
        elif discards[-1].value == "Reversa":
            Direction *= -1
            currentColour = discards[-1].colour
        elif discards[-1].value == "Salta":
            if playerTurn == len(players)-1 and Direction == 1:
                playerTurn = 0
            elif playerTurn == 0 and Direction == -1:
                playerTurn = len(players)-1
            else:
                playerTurn += Direction
            currentColour = discards[-1].colour
            print("Salta") #este print() es solo para que el programa pueda compilar mientras
        elif discards[-1].value == "Tira un color":

            #Variable aux
            i= 0
            #Contador de cartas bajadas
            discardsCount= 0
            for card in players[playerTurn].hand:
                if card.colour == currentColour:
                    discards.append(players[playerTurn].hand.pop(i))
                    discardsCount += 1
                else:
                    i+=1  
            print('')
            print('Bajaste {} cartas de color {}'.format(discardsCount, currentColour)) 
            print('') 
            currentColour = discards[-1].colour
        else: 
            #Es una carta normal
            print("Es normal")




    else:
        #Si no pudo jugar porque agarró 2, entonces hay que borrar la cadena de doble manotazo
        if (discards[-1].value == 'Doble manotazo'):
            DobleManotazoTimes = 0
        print("No puedes jugar. Tienes que pisar el boton de la maquina")
        print("Presione una tecla para continuar...")
        msvcrt.getch()
        print("*lo pisa*")
       
        players[playerTurn].hand.extend(Deck.spitOutCards())
        


    if len(players[playerTurn].hand) == 0:
        playing = False
    else:
        playerTurn += Direction
        if (playerTurn == len(players)):
            playerTurn = 0
        elif playerTurn < 0:
            playerTurn = len(players)-1    
    
print('EL GANADOR ES EL JUGADOR {}'.format(playerTurn))