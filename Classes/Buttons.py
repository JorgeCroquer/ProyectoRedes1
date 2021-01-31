#clase para los botones
import pygame

class Button:
    
    botonesC = []
    def __init__(self,surface,x,y
    ):
        self.surface = surface
        self.x = x
        self.y = y
        pygame.init()

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

    def setSurfaceJ1(self,numero,font):
        if numero == 0:
            self.surface =  font.render('J1',True,(255,255,255))
        if numero == 1:
            self.surface =  font.render('J2',True,(255,255,255))
        if numero == 2:
            self.surface =  font.render('J3',True,(255,255,255))
        if numero == 3:
            self.surface =  font.render('J4',True,(255,255,255))

    def setSurfaceJ2(self,numero,font):    
        if numero == 0:
            self.surface =  font.render('J1',True,(235, 64, 52))
        if numero == 1:
            self.surface =  font.render('J2',True,(235, 64, 52))
        if numero == 2:
            self.surface =  font.render('J3',True,(235, 64, 52))
        if numero == 3:
            self.surface =  font.render('J4',True,(235, 64, 52))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        width,height = self.surface.get_size()
        if pos[0] > self.x and pos[0] < self.x + width:
            if pos[1] > self.y and pos[1] < self.y + height:
                return True    
        return False