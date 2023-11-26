import pygame

class Button():
    def __init__(self, image_01, image_02, pos):
        self.pos = pos
        self.image_01 = pygame.transform.rotozoom(image_01, 0, 0.6)
        self.image_02 = pygame.transform.rotozoom(image_02, 0, 0.6)
        self.temp = self.image_01
        self.rect_01 = self.image_01.get_rect()
        self.rect_01.center = (pos)
        self.rect_02 = self.image_02.get_rect()
        self.rect_02.center = (pos)
    
    def on_pess(self):
        self.temp = self.image_02
    
    def normal(self):
        self.temp = self.image_01
    
    def get_image(self):
        return self.temp
    
    def get_pos(self):
        rect = self.temp.get_rect()
        rect.center = (self.pos)
        return rect
    
    def checkForInput(self, position):
        if self.rect_01.collidepoint(position):
            return True
        return False