import pygame
from pygame.locals import *

music = ['sound/MusicBackground.mp3', 'sound/HighScore.mp3', 'sound/GameOverFx.mp3']

def play_music(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()

def loop_music(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.music.pause()

def replay():
    pygame.mixer.music.unpause()