import math
import pygame, sys
from pygame.locals import *
import Score
import Move
import Board_game
import Redu as R
from button import Button
import sound
import Congratulations as cg

pygame.init()

DISPLAYSURF = pygame.display.set_mode((450, 300))
pygame.display.set_caption('2048 Game')

clock = pygame.time.Clock()

Logo = pygame.image.load('image/Logo.png')
pygame.display.set_icon(Logo)

# Color
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
            'black': (0, 0, 0),
            'white': (255, 255, 255),
            'background': (252, 250, 241)}

def get_font(size):
    return pygame.font.Font('font/Montserrat-Bold.ttf', size)

def draw_board(board):
    pygame.draw.rect(DISPLAYSURF, color['board'], [0, 0, 300, 300])
    
    for i in range(4):
        for j in range(4):
            tile = board[i, j]
            pygame.draw.rect(DISPLAYSURF, color[0], (72 * j + 10, 72 * i + 10, 64, 64), 0, 5)
            if tile != 0:
                draw_tile(DISPLAYSURF, i, j, tile)

def draw_tile(screen, row, col, value):
    if value in [2, 4]:
        font_surface = get_font(30).render(str(value), True, color['black'])
    else:
        font_surface = get_font(30 - 2 * math.ceil(math.log10(value))).render(str(value), True, color['white'])
    
    font_rect = font_surface.get_rect(center = (col * 72 + 10 + 64 / 2, row * 72 + 10 + 64 / 2))
    
    if value <= 2048:
        pygame.draw.rect(screen, color[value], (col * 72 + 10, row * 72 + 10, 64, 64), 0, 5)
    else:
        pygame.draw.rect(screen, color['other'], (col * 72 + 10, row * 72 + 10, 64, 64), 0, 5)
    
    screen.blit(font_surface, font_rect)

def score_box(score):
    score_surface = get_font(28).render(str(score), True, color[16])
    score_rect = score_surface.get_rect(center = (375, 118))
    font_surface = get_font(10).render('SCORE', True, color['black'])
    font_rect = font_surface.get_rect(center = (333, 93))
    pygame.draw.rect(DISPLAYSURF, color['box'], (310, 82, 130, 60), 0, 5)
    DISPLAYSURF.blit(font_surface, font_rect)
    DISPLAYSURF.blit(score_surface, score_rect)

def best_score_box(best_score):
    best_surface = get_font(28).render(str(best_score), True, color[16])
    best_rect = best_surface.get_rect(center = (375, 188))
    font_surface = get_font(10).render('YOUR BEST', True, color['black'])
    font_rect = font_surface.get_rect(center = (345, 163))
    pygame.draw.rect(DISPLAYSURF, color['box'], (310, 152, 130, 60), 0, 5)
    DISPLAYSURF.blit(font_surface, font_rect)
    DISPLAYSURF.blit(best_surface, best_rect)

def main_game(Board, score):
    # Reset new game
    Score.new_score = score
    R.add_storage(Board, Score.new_score)
    
    # Create button
    redu_button_01 = pygame.image.load('image/button/return00-01.png').convert_alpha()
    redu_button_02 = pygame.image.load('image/button/return01-01.png').convert_alpha()
    redu_button = Button(redu_button_01, redu_button_02, (385, 30), 0.6) 
    
    setting_button_01 = pygame.image.load('image/button/setting00-01.png').convert_alpha()
    setting_button_02 = pygame.image.load('image/button/setting01-01.png').convert_alpha()
    setting_button = Button(setting_button_01, setting_button_02, (420, 30), 0.6)
    
    while True:
        for event in pygame.event.get():
            direction = ""
            if cg.win_game(Board):
                for i in range(len(cg.congratulations)):
                    index = i
                    DISPLAYSURF.fill(color['background'])
                    DISPLAYSURF.blit(redu_button.get_image(), redu_button.get_pos())
                    DISPLAYSURF.blit(setting_button.get_image(), setting_button.get_pos())
                    draw_board(Board)
                    score_box(Score.new_score)
                    best_score_box(Score.high_score)
                    cg.play(DISPLAYSURF, index)
                    pygame.display.update()
                    pygame.time.wait(20)
            
            if Move.Game_over(Board):
                pygame.mixer.music.stop()
                pygame.time.wait(500)
                game_over(Score.new_score)
            
            if event.type == MOUSEBUTTONDOWN:
                if redu_button.checkForInput(event.pos):
                    redu_button.on_pess()
                    if len(R.Storage_board) > 1:
                        redu = R.redu()
                        Board = redu[0]
                        Score.new_score = redu[1]
                elif setting_button.checkForInput(event.pos):
                    setting_button.on_pess()
                    DISPLAYSURF.blit(setting_button.get_image(), setting_button.get_pos())
                    pygame.display.update()
                    pygame.time.wait(200)
                    sound.stop_music()
                    setting()
            else:
                redu_button.normal()
                setting_button.normal()
            
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
        DISPLAYSURF.blit(redu_button.get_image(), redu_button.get_pos())
        DISPLAYSURF.blit(setting_button.get_image(), setting_button.get_pos())
        draw_board(Board)
        score_box(Score.new_score)
        best_score_box(Score.high_score)
        pygame.display.update()

def setting():
    # Button
    resume_button_01 = pygame.image.load('image/button/resume00-01.png').convert_alpha()
    resume_button_02 = pygame.image.load('image/button/resume01-01.png').convert_alpha()
    resume_button = Button(resume_button_01, resume_button_02, (225, 70), 0.8)
    
    restart_button_01 = pygame.image.load('image/button/restart00-01.png').convert_alpha()
    restart_button_02 = pygame.image.load('image/button/restart01-01.png').convert_alpha()
    restart_button = Button(restart_button_01, restart_button_02, (225, 135), 0.8)
    
    quit_button_01 = pygame.image.load('image/button/QUIT00-01.png').convert_alpha()
    quit_button_02 = pygame.image.load('image/button/QUIT01-01.png').convert_alpha()
    quit_button = Button(quit_button_01, quit_button_02, (225, 200), 0.8)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN:
                if restart_button.checkForInput(event.pos):
                    restart_button.on_pess()
                    sound.loop_music(sound.music[0])
                    DISPLAYSURF.blit(restart_button.get_image(), restart_button.get_pos())
                    pygame.display.update()
                    pygame.time.wait(200)
                    R.Storage_board = []
                    R.Storage_score = []
                    main_game(Board_game.new_board(), 0)
                elif resume_button.checkForInput(event.pos):
                    resume_button.on_pess()
                    sound.replay()
                    DISPLAYSURF.blit(resume_button.get_image(), resume_button.get_pos())
                    pygame.display.update()
                    pygame.time.wait(200)
                    resume = R.resume_game()
                    main_game(resume[0], resume[1])
                elif quit_button.checkForInput(event.pos):
                    quit_button.on_pess()
                    DISPLAYSURF.blit(quit_button.get_image(), quit_button.get_pos())
                    pygame.display.update()
                    pygame.quit()
                    sys.exit()
            else:
                restart_button.normal()
                resume_button.normal()
                quit_button.normal()
        
        DISPLAYSURF.fill(color['background'])
        DISPLAYSURF.blit(resume_button.get_image(), resume_button.get_pos())
        DISPLAYSURF.blit(restart_button.get_image(), restart_button.get_pos())
        DISPLAYSURF.blit(quit_button.get_image(), quit_button.get_pos())
        pygame.display.update()

def game_over(score):
    gameover = pygame.image.load('image/GameOver-01.png')
    gameover = pygame.transform.rotozoom(gameover, 0, 1.2)
    rect = gameover.get_rect()
    rect.center = (225, 85)
    
    quit_button_01 = pygame.image.load('image/button/QUIT00-01.png').convert_alpha()
    quit_button_02 = pygame.image.load('image/button/QUIT01-01.png').convert_alpha()
    quit_button = Button(quit_button_01, quit_button_02, (150, 200), 0.6)
    
    new_game_01 = pygame.image.load('image/button/new_game00-01.png').convert_alpha()
    new_game_02 = pygame.image.load('image/button/new_game01-01.png').convert_alpha()
    new_game = Button(new_game_01, new_game_02, (300, 200), 0.6)
    
    if score <= Score.high_score:
        score_text = get_font(18).render('YOUR SCORE: ' + str(score), True, color[0])
        rect_score = score_text.get_rect(center = (225, 120))
        pygame.time.wait(200)
        sound.play_music(sound.music[2])
    else:
        score_text = get_font(20).render('NEW HIGH SCORE: ' + str(score), True, color[8])
        rect_score = score_text.get_rect(center = (225, 120))
        pygame.time.wait(200)
        sound.play_music(sound.music[1])
    
    while True:        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if new_game.checkForInput(event.pos):
                    new_game.on_pess()
                    DISPLAYSURF.blit(new_game.get_image(), new_game.get_pos())
                    pygame.display.update()
                    pygame.time.wait(200)
                    R.Storage_board = []
                    R.Storage_score = []
                    sound.loop_music(sound.music[0])
                    main_game(Board_game.new_board(), 0)
                elif quit_button.checkForInput(event.pos):
                    quit_button.on_pess()
                    DISPLAYSURF.blit(quit_button.get_image(), quit_button.get_pos())
                    pygame.display.update()
                    pygame.quit()
                    sys.exit()
        DISPLAYSURF.fill(color['background'])
        DISPLAYSURF.blit(gameover, rect)
        DISPLAYSURF.blit(score_text, rect_score)
        DISPLAYSURF.blit(quit_button.get_image(), quit_button.get_pos())
        DISPLAYSURF.blit(new_game.get_image(), new_game.get_pos())
        pygame.display.update()

if __name__ == '__main__':
    sound.loop_music(sound.music[0])
    main_game(Board_game.new_board(), 0)