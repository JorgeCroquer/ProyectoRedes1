from Classes.Player import Player
from Classes.Player import Player
from Classes.Card import Card
from Classes.Deck import Deck
import pygame,sys

# Rutinas graficas:
#  Estas rutinas se correrán en el while principal
#  para que vayan actualizando las cartas de los jugadores

def showOthers():
    sep = 60
    for x in range(1,len(players)):
        if len(players[x].hand) <= 5:
            sep = 70    
        if len(players[x].hand) > 5 and len(players[x].hand) < 15 :
            sep = 40
        if len(players[x].hand) >= 15 :
            sep = 20     
        if x == 1:
            carta = pygame.image.load('img/card_back.png').convert() 
            carta = pygame.transform.rotate(carta,90)
        if x == 2: 
            carta = pygame.image.load('img/card_back.png').convert()
            carta = pygame.transform.rotate(carta,180)
        if x == 3: 
            carta = pygame.image.load('img/card_back.png').convert()
            carta = pygame.transform.rotate(carta,270)     
        for y in range(len(players[x].hand)):
            if x == 1: 
                Cx = 1050
                Cy = 100+y*sep
            if x == 2: 
                Cx = 300+y*sep
                Cy = -10
            if x == 3: 
                Cx = -45
                Cy = 100+y*sep
            screen.blit(carta,(Cx,Cy)) 

def showHand():
    for x in range(len(player1.hand)):
        screen.blit(player1.hand[x].surface,(player1.hand[x].x,player1.hand[x].y))          

def showDiscard():
    carta = identificar(discards[0])
    screen.blit(carta,(600,250)) 

def showDeck():
    carta = pygame.image.load('img/card_back.png').convert()
    screen.blit(carta,(400,250)) 

#Rutinas logicas de dibujo
#Estas rutinas nos ayudan a asignarle a cada carta su imagen y posicion segun debe ser
#posteriormente fueron integradas a la clase player pero se mantienen aquí por si acaso se necesitaran
def identificar(cartaId):
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
    # if cartaId.colour == "Comodin":
    #     carta = pygame.image.load('img/small/wild_color_changer.png').convert()
    #     return carta
    # if cartaId.value == "Tira un color":
    #     carta = pygame.image.load('img/small/card_back_alt.png').convert()
    #     return carta    
    valor = Mvalues.get(cartaId.value,"_back")
    color = Mcolours.get(cartaId.colour,"card")
    carta = pygame.image.load('img/{}{}.png'.format(color,valor)).convert()
    return carta

def asignHand():
    y=0
    if len(player1.hand) < 8:
        for x in range(len(player1.hand)):
            player1.hand[x].x = 180+x*110
            player1.hand[x].y = 520
    else:
        for x in range(int(len(player1.hand)/2)):
            player1.hand[x].x = 220+x*110
            player1.hand[x].y = 470
        for x in range(int(len(player1.hand)/2),len(player1.hand)):
            player1.hand[x].x = 200+y*110
            player1.hand[x].y = 600 
            y=y+1

#Especificamos los detalles de la pantalla
pygame.init()
screen = pygame.display.set_mode((1200,720))
pygame.display.set_caption("UNO Attack")
clock = pygame.time.Clock()

#Creamos el fondo
bg_surface = pygame.Surface([1200,720])
bg_surface.fill((46,57,102)) #Este es el color de fondo

#EMPIEZA EL JUEGO -------------------------------------------------------------------------------------

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
player1.draw(15,Deck)
player2.draw(7,Deck)
player3.draw(7,Deck)
player4.draw(7,Deck)

players = [player1, player2, player3,player4]

Direction = 1 #1 para sentido horario. -1 para sentido antihorario

playerTurn = 0

discards.append(Deck.cards.pop(0)) #Agarramos la primera carta del mazo para ser la primera sobre la cual jugar

asignHand()#asignamos a cada carta su posicion en pantalla

#Imprimimos valores por consola para constrastar con los graficos
for x in range(len(player1.hand)):
    print('{}) {} {}'.format(x,player1.hand[x].colour,player1.hand[x].value))
print("--------------------------------")    
print(discards[0].colour,discards[0].value)

while True:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for x in range(len(player1.hand)):
                if player1.hand[x].isOver(pos):
                    print('cliqueaste la carta: {} {}'.format(player1.hand[x].colour,player1.hand[x].value))
        if event.type == pygame.MOUSEMOTION:
             for x in range(len(player1.hand)):
                if player1.hand[x].isOver(pos):
                    player1.asignHand() 
                    player1.hand[x].y -= 20                              
    screen.blit(bg_surface,(0,0))
    showHand()
    showOthers()  
    showDiscard()
    showDeck()
    pygame.display.update()
    clock.tick(120)
