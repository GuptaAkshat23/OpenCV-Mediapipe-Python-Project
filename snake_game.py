import pygame
import sys
import os
import random
import math

pygame.init()
pygame.display.set_caption("snake game")
pygame.font.init()
random.seed()

SPEED = 0.36
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE #we will keep both food and size of snake same
SEPERATION = 10  #seperation between two pixels
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 60
KEY = {"UP":1 , "DOWN":2 , "LEFT":3, "RIGHT":4}

#initisalising the screen

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.HWSURFACE)
#hwsurface stands for hardware surface which refers to the memory used by the video card for storing memory

score_font = pygame.font.Font(None,38)
score_num_font = pygame.font.Font(None,28)