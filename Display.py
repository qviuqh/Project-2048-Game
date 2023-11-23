import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((450, 300))
pygame.display.set_caption('2048 Game')

color = {0: (204, 192, 179),
         2: (238, 228, 218),
         4: (238, 224, 198),
         8: (243, 177, 118),
         16: (245, 149, 99),
         32: (249, 123, 89),
         64: (246, 94, 59),
         128: (237, 207, 114),
         256: (237, 204, 97),
         512: (236, 200, 80),
         1024: (239, 197, 63),
         2048: (238, 194, 46),
         'other': (183, 132, 171),
         'board': (187, 173, 160),
         'background': (252, 250, 241)}

def draw_board():
    pygame.draw.rect(DISPLAYSURF, color['board'], [0, 0, 300, 300])

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    DISPLAYSURF.fill(color['background'])
    draw_board()
    pygame.display.update()