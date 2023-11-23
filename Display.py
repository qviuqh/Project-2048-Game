import pygame, sys
from pygame.locals import *
import Score
import Move
import Board_game
import Redu as R

pygame.init()

DISPLAYSURF = pygame.display.set_mode((450, 300))
pygame.display.set_caption('2048 Game')

# Font
font = pygame.font.Font('font/Montserrat-Bold.ttf', 30)
font_01 = pygame.font.Font('font/Montserrat-Bold.ttf', 10)
font_score = pygame.font.Font('font/Montserrat-Bold.ttf', 28)

color =    {0: (204, 192, 179),
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
            'box': (237, 233, 217),
            'black': (0, 0 ,0),
            'background': (252, 250, 241)}

def draw_board(board):
    pygame.draw.rect(DISPLAYSURF, color['board'], [0, 0, 300, 300])
    
    for i in range(4):
        for j in range(4):
            tile = board[i, j]
            pygame.draw.rect(DISPLAYSURF, color[0], (72 * j + 10, 72 * i + 10, 64, 64), 0, 5)
            if tile != 0:
                draw_tile(DISPLAYSURF, i, j, tile)

def draw_tile(screen, row, col, value):
    font_surface = font.render(str(value), True, color['black'])
    font_rect = font_surface.get_rect(center = (col * 72 + 10 + 64 / 2, row * 72 + 10 + 64 / 2))
    pygame.draw.rect(screen, color[value], (col * 72 + 10, row * 72 + 10, 64, 64), 0, 5)
    screen.blit(font_surface, font_rect)

def score_box(score):
    score_surface = font_score.render(str(score), True, color[16])
    score_rect = score_surface.get_rect(center = (375, 118))
    font_surface = font_01.render('SCORE', True, color['black'])
    font_rect = font_surface.get_rect(center = (333, 93))
    pygame.draw.rect(DISPLAYSURF, color['box'], (310, 82, 130, 60), 0, 5)
    DISPLAYSURF.blit(font_surface, font_rect)
    DISPLAYSURF.blit(score_surface, score_rect)

def best_score_box(best_score):
    best_surface = font_score.render(str(best_score), True, color[16])
    best_rect = best_surface.get_rect(center = (375, 188))
    font_surface = font_01.render('YOUR BEST', True, color['black'])
    font_rect = font_surface.get_rect(center = (345, 163))
    pygame.draw.rect(DISPLAYSURF, color['box'], (310, 152, 130, 60), 0, 5)
    DISPLAYSURF.blit(font_surface, font_rect)
    DISPLAYSURF.blit(best_surface, best_rect)

def main_game():
    Board = Board_game.new_board()
    R.add_storage(Board, Score.new_score)
    
    while True:
        for event in pygame.event.get():
            direction = ""
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                elif event.key == pygame.K_LEFT:
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
            
            if Move.valid_move(Board, direction) == True:
                Board = Move.move(Board, direction)
                Board_game.random_tile(Board)
                R.add_storage(Board, Score.new_score)
        
        DISPLAYSURF.fill(color['background'])
        draw_board(Board)
        score_box(Score.new_score)
        best_score_box(Score.high_score)
        pygame.display.update()

if __name__ == '__main__':
    main_game()