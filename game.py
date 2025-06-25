import pygame
import random
from sys import exit

from utils import *
from bird import Bird
from pipe import Pipe
from ground import Ground

class Game:
    def __init__(self):
        self.score = 0
        self.game_stopped = True
        self.window = window 
        self.timer = pygame.time.Clock()
        self.font = pygame.font.SysFont("Segoe", 26)
        
    def quit_game(self):
        # exit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
    def run(self):
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
            self.quit_game()
        
            # reset frame
            self.window.fill((0, 0, 0))
        
            # user input
            user_input = pygame.key.get_pressed()
        
            # draw background
            self.window.blit(bg_img, (0, 0))
        
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
                if collision_ground and user_input[pygame.K_r]:
                    self.score = 0
                    self.game_stopped = True
                    return
                    # if user_input[pygame.K_r]:
                    #     score = 0
                    # break
        
            # draw ground, pipes, and bird
            pipes.draw(self.window)
            ground.draw(self.window)
            bird.draw(self.window)

            # show score
            score_text = self.font.render("Score: " + str(self.score), True, pygame.Color(255, 255, 255))
            self.window.blit(score_text, (20, 20))
        
            # game over
            if not bird.sprite.alive and collision_ground:
                self.window.blit(game_over_img, (
                    win_width // 2 - game_over_img.get_width() // 2,
                    win_height // 2 - game_over_img.get_height() // 2
                ))
        
            # update ground, pipes, and bird
            if bird.sprite.alive:
                ground.update()
                pipes.update()
                
                for pipe in pipes:
                    if pipe.pipe_type == "bottom":
                        self.score += pipe.score
                        pipe.score = 0
                
            bird.update(user_input)
        
            self.timer.tick(60)
            pygame.display.update()
        
    def menu(self):
        while self.game_stopped:
            self.quit_game()
        
            # draw menu 
            self.window.fill((0, 0, 0))
            self.window.blit(bg_img, (0, 0))
            self.window.blit(ground_img, Ground(0, 520))
            self.window.blit(bird_imgs[0], (100, 250))
            self.window.blit( start_img, (
                win_width // 2 - game_over_img.get_width() // 2,
                win_height // 2 - game_over_img.get_height() // 2
                ))
        
            # user input
            user_input = pygame.key.get_pressed()
            if user_input[pygame.K_SPACE]:
                self.game_stopped = False
                self.run()
        
            pygame.display.update()
        
        
        
        
        
        
