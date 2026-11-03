import pygame
import os
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assests")

class Defender:
    def __init__(self):
        pass
        self.lives = 3
        self.speed = 5
        img =  pygame.image.load(ASSETS + "/images/defender.png").convert_alpha()
        self.image = pygame.transform.scale(img, (100, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (100 , 100)
                
    def update(self, screen):
        self.move(screen)
        screen.blit(self.image, self.rect)

    def move(self, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
        
            
        self.rect.clamp_ip(screen.get_rect())
    

    def shoot(self):
        pass

    def hit(self):
        pass
