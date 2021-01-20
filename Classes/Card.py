#clase para una carta normal

class Card:
    
    def __init__(self, colour, value, surface=''):
        self.colour = colour
        self.value = value
        self.surface = surface
        
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.surface.width:
            if pos[1] > self.y and pos[1] < self.y + self.surface.height:
                return True    
        return False