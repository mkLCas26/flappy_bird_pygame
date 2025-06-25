import pygame

# window display
win_height = 720
win_width = 551
window = pygame.display.set_mode((win_width, win_height))

# game variables
scroll_speed = 1
bird_start_pos = (100, 250)

# load images
bird_imgs = [pygame.image.load("assets/bird_down.png"),
             pygame.image.load("assets/bird_mid.png"),
             pygame.image.load("assets/bird_up.png"),]
bg_img = pygame.image.load("assets/background.png")
ground_img = pygame.image.load("assets/ground.png")
top_pipe_img = pygame.image.load("assets/pipe_top.png")
bot_pipe_img = pygame.image.load("assets/pipe_bottom.png")
start_img = pygame.image.load("assets/start.png")
game_over_img = pygame.image.load("assets/game_over.png")