import pygame
from pygame.locals import *

class Character(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.image = pygame.Surface((64, 64))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y

        self.onGround = False

        self.speed = 10
        self.jumpVel = -20

        self.gravity = 2

        self.vel = [0, 0]
        self.acc = [0, self.gravity]
  

    def update(self, dt, collisionGroup):

        self.vel[0] += self.acc[0] * dt
        self.vel[1] += self.acc[1] * dt

       

        if self.onGround:
            self.acc[1] = 0
        else:
            self.acc[1] = self.gravity

        for other in collisionGroup.sprites():
            if self is not other:
                if other.rect.colliderect(pygame.Rect(self.rect.x + self.vel[0], self.rect.y, self.rect.w, self.rect.h)):
                    pass
                    if self.vel[0] > 0: #Going Right
                        self.vel[0] = other.rect.x - (self.rect.x + self.rect.w)
                    else: # Going Left
                        self.vel[0] = other.rect.x + other.rect.w - self.rect.x
                if other.rect.colliderect(pygame.Rect(self.rect.x, self.rect.y + self.vel[1], self.rect.w, self.rect.h)):
                        if self.vel[1] > 0: #Going Down
                            self.vel[1] = other.rect.y - (self.rect.y + self.rect.h)
                            self.onGround = True
                        else: #Going Up
                            self.vel[1] = other.rect.y + other.rect.h - self.rect.y

        self.x += self.vel[0] * dt
        self.y += self.vel[1] * dt

        self.rect.centerx = self.x
        self.rect.centery = self.y


    def jump(self):
        self.vel[1] = self.jumpVel
        self.onGround = False

    def setVel(self, vel):
        self.vel = vel
        

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class PlayerCharacter(Character):

    def __init__(self, x, y):
        Character.__init__(self, x, y)

    def handleInputs(self, keys):
        self.vel[0] = 0

        if keys[K_a]:
            self.vel[0] = -self.speed
        if keys[K_d]:
            self.vel[0] = self.speed
        


    def update(self, dt, collisionGroup):
        Character.update(self, dt, collisionGroup)


class Enemy(Character):

    def __init__(self, x, y):
        Character.__init__(self, x, y)

    def update(self, dt, collisionGroup):
        Character.update(self, dt, collisionGroup)




class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.image = pygame.Surface((64, 64))
        self.image.fill((100, 100, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
