import pygame
from utils import scroll_speed, win_width, bird_start_pos


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