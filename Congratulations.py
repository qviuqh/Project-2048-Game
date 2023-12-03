import pygame
import numpy as np

pygame.init()

checking = 0
congratulations = []

win_game_text = pygame.font.Font('font/Montserrat-Bold.ttf', 40)
font_surface = win_game_text.render("YOU WIN", True, (249, 123, 89))
font_rect = font_surface.get_rect(center = (225, 150))

for i in range(75):
    congratulations.append(pygame.image.load('image/Congratulations/{}.png'.format(str(i))))

def play(sceen, index):
    img = congratulations[index]
    rect = img.get_rect()
    rect.center = (225, 150)
    sceen.blit(img, rect)
    sceen.blit(font_surface, font_rect)

def win_game(board):
    global checking
    if 2048 in board and np.count_nonzero(board == 2048) != checking:
        checking += np.count_nonzero(board == 2048) - checking
        return True
    else:
        return False