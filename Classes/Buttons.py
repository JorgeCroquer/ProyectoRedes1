#clase para los botones
import pygame

class Button:
    
    botonesC = []
    
    def __init__(self,surface,x,y
    ):
        self.surface = surface
        self.x = x
        self.y = y


    def setSurface1(self,numero):
        if numero == 0:
            self.surface = pygame.image.load('img/boton_rojo_sombra1.png')
        if numero == 1:
            self.surface = pygame.image.load('img/boton_verde_sombra1.png') 
        if numero == 2:
            self.surface = pygame.image.load('img/boton_azul_sombra1.png') 
        if numero == 3:
            self.surface = pygame.image.load('img/boton_amarillo_sombra1.png')

    def setSurface2(self,numero):
        if numero == 0:
            self.surface = pygame.image.load('img/boton_rojo_sombra2.png')
        if numero == 1:
            self.surface = pygame.image.load('img/boton_verde_sombra2.png') 
        if numero == 2:
            self.surface = pygame.image.load('img/boton_azul_sombra2.png') 
        if numero == 3:
            self.surface = pygame.image.load('img/boton_amarillo_sombra2.png')    

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        width,height = self.surface.get_size()
        if pos[0] > self.x and pos[0] < self.x + width:
            if pos[1] > self.y and pos[1] < self.y + height:
                return True    
        return False