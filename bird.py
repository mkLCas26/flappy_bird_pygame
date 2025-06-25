import pygame
from utils import bird_imgs, bird_start_pos

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