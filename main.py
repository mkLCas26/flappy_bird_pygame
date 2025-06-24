# import libraries and other necessities
import pygame
from sys import exit

pygame.init()
timer = pygame.time.Clock()

# window display
win_height = 720
win_width = 551
window = pygame.display.set_mode((win_width, win_height))

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

# for game
scroll_speed = 1

class Ground(pygame.sprite.Sprite):
    def __init__(self, groundx, groundy):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = groundx, groundy
        
    def move(self):
        #moving ground
        self.rect.rectx -= scroll_speed
        if self.rect.x <= win_width:
            self.kill()
            
        

# exit the game
def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# run game
def main():
    run = True
    while run:
        quit_game()
        
        window.fill((0, 0, 0))
        
        # draw background
        window.blit(bg_img, (0, 0))
        
        timer.tick(60)
        pygame.display.update()
        
main()
        
        
