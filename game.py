import pygame
import random
from sys import exit

from utils import *
from bird import Bird
from pipe import Pipe
from ground import Ground

class Game:
    def __init__(self):
        score = 0
        game_stopped = True
        self.window = window 
        timer = pygame.time.Clock()
        font = pygame.font.SysFont("Segoe", 26)
        
    def quit_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        
