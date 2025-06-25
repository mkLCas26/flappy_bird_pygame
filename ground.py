import pygame
from utils import ground_img, scroll_speed, win_width


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