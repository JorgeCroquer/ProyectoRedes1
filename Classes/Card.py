#clase para una carta normal
import pygame

class Card:
    
    def __init__(self, colour, value
    # , surface='',x=0,y=0
    ):
        self.colour = colour
        self.value = value
        # self.surface = surface
        # self.x = x
        # self.y = y
        
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        width,height = self.surface.get_size()
        if pos[0] > self.x and pos[0] < self.x + width:
            if pos[1] > self.y and pos[1] < self.y + height:
                return True    
        return False