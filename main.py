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
game_stopped = True

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
    global score
    
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
            last_ground = ground.sprites()[-1]
            new_groundx = last_ground.rect.x + ground_img.get_width()
            ground.add(Ground(new_groundx, groundy_pos))
        
        # spawn pipe
        if pipe_timer <= 0 and bird.sprite.alive:
            x_top, x_bottom = 550, 550
            y_top = random.randint(-600, -480)
            y_bottom = y_top + random.randint(98,130) + bot_pipe_img.get_height()
            pipes.add(Pipe(x_top, y_top, top_pipe_img, "top"))
            pipes.add(Pipe(x_bottom, y_bottom, bot_pipe_img, "bottom"))
            pipe_timer = random.randint(180, 250)
        pipe_timer -= 1  
        
        # collision detection
        collision_pipes = pygame.sprite.spritecollide(bird.sprites()[0], pipes, False)
        collision_ground = pygame.sprite.spritecollide(bird.sprites()[0], ground, False)
        if collision_pipes or collision_ground:
            bird.sprite.alive = False
            if collision_ground:
                window.blit(game_over_img, (
                    win_width // 2 - game_over_img.get_width() // 2,
                    win_height // 2 - game_over_img.get_height() // 2
                    ))
                if user_input[pygame.K_r]:
                    score = 0
                    break
        
        # draw ground, pipes, and bird
        pipes.draw(window)
        ground.draw(window)
        bird.draw(window)

        # show score
        score_text = font.render("Score: " + str(score), True, pygame.Color(255, 255, 255))
        window.blit(score_text, (20, 20))
        
        # update ground, pipes, and bird
        if bird.sprite.alive:
            ground.update()
            pipes.update()
        bird.update(user_input)
        
        timer.tick(60)
        pygame.display.update()
        
# main menu
def menu():
    global game_stopped
    
    while game_stopped:
        quit_game()
        
        # draw menu 
        window.fill((0, 0, 0))
        window.blit(bg_img, (0, 0))
        window.blit(ground_img, Ground(0, 520))
        window.blit(bird_imgs[0], (100, 250))
        window.blit( start_img, (
                win_width // 2 - game_over_img.get_width() // 2,
                win_height // 2 - game_over_img.get_height() // 2
                ))
        
        # user input
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_SPACE]:
            main()
        
        pygame.display.update()
        
menu()
