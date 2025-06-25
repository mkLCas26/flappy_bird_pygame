# import libraries and other necessities
import pygame
from sys import exit
import random

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

# for game variables
scroll_speed = 1
bird_start_pos = (100, 250)
score = 0
font = pygame.font.SysFont("Segoe", 26)

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bird_imgs[0]
        self.rect = self.image.get_rect()
        self.rect.center = bird_start_pos
        self.image_index = 0
        self.vel = 0
        self.flap = False
        self.alive = True
        
    def update(self, user_input):
        # animate bird
        if self.alive:
            self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = bird_imgs[self.image_index // 10]
        
        # gravity and flap
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 500:
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.flap = False
            
        # rotate bird in movement
        self.image = pygame.transform.rotate(self.image, self.vel * -7)
        
        # user input = spacebar
        if user_input[pygame.K_SPACE] and not self.flap and self.rect.y > 0 and self.alive:
            self.flap = True
            self.vel = -7

class Pipe(pygame.sprite.Sprite):
    def __init__(self, pipex, pipey, image, pipe_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pipex, pipey
        self.enter, self.exit, self.passed = False, False, False
        self.pipe_type = pipe_type
        
    def update(self):
        # move pipe
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()
            
        # scoring
        global score
        if self.pipe_type == "bottom":
            if bird_start_pos[0] > self.rect.topleft[0] and not self.passed:
               self.enter = True
            if bird_start_pos[0] > self.rect.topright[0] and not self.passed:
                self.exit = True
            if self.enter and self.exit and not self.passed:
                self.passed = True
                score += 1
                
                     

class Ground(pygame.sprite.Sprite):
    def __init__(self, groundx, groundy):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = groundx, groundy
        
    def update(self):
        #moving ground
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()
            
        

# exit the game
def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# run game
def main():
    # initialize bird
    bird = pygame.sprite.GroupSingle()
    bird.add(Bird())
    
    # setup pipes
    pipe_timer = 0
    pipes = pygame.sprite.Group()

    # initialize first ground img
    groundx_pos, groundy_pos = 0, 520
    ground = pygame.sprite.Group()
    ground.add(Ground(groundx_pos, groundy_pos))
    
    run = True
    while run:
        quit_game()
        
        # reset frame
        window.fill((0, 0, 0))
        
        # user input
        user_input = pygame.key.get_pressed()
        
        
        # draw background
        window.blit(bg_img, (0, 0))
        
        # spawn ground
        if len(ground) <= 2:
            ground.add(Ground(groundx_pos, groundy_pos))
        
        # spawn pipe
        if pipe_timer <= 0:
            x_top, x_bottom = 550, 550
            y_top = random.randint(-600, -480)
            y_bottom = y_top + random.randint(98,130) + bot_pipe_img.get_height()
            pipes.add(Pipe(x_top, y_top, top_pipe_img))
            pipes.add(Pipe(x_bottom, y_bottom, bot_pipe_img))
            pipe_timer = random.randint(180, 250)
        pipe_timer -= 1  
        
        # draw ground, pipes, and bird
        ground.draw(window)
        pipes.draw(window)
        bird.draw(window)
        
        # move ground, pipes, and bird
        ground.update()
        pipes.update()
        bird.update(user_input)
        
        timer.tick(60)
        pygame.display.update()
        
main()
        
        
