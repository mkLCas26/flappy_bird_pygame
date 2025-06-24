# import libraries and other necessities
import pygame
from sys import exit

pygame.init()
timer = pygame.time.Clock()

win_height = 720
win_width = 551
window = pygame.display.set_mode((win_width, win_height))

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    run = True
    while run:
        quit_game()
        
        window.fill (0, 0, 0)
        
        timer.tick(60)
        pygame.display.update()
        
main()
        
        
