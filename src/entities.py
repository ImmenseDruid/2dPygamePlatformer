import pygame
import physics
from pygame.locals import *

class Character(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y

        self.leftOnGroundPoint = (self.rect.x, self.rect.centery + self.rect.h / 2)
        self.rightOnGroundPoint = (self.rect.x + self.rect.w, self.rect.centery + self.rect.h / 2)

        self.raycastLeft = physics.Raycast(self.leftOnGroundPoint, (self.leftOnGroundPoint[0], self.leftOnGroundPoint[1] + 5))
        self.raycastRight = physics.Raycast(self.rightOnGroundPoint, (self.rightOnGroundPoint[0], self.rightOnGroundPoint[1] + 5))

        self.onGround = False

        self.speed = 8
        self.jumpVel = -20

        self.gravity = 1
        self.movementEpsilon = .01

        self.vel = [0, 0]
        self.acc = [0, self.gravity]
  

    def update(self, dt, collisionGroup):

        self.onGround = False  

        self.vel[0] += self.acc[0] * dt
        self.vel[1] += self.acc[1] * dt

        dx = self.vel[0] * dt
        dy = self.vel[1] * dt

        dx, dy = self.collide(dx, dy, collisionGroup)

        self.vel[0] = dx
        self.vel[1] = dy 

        self.x += dx
        self.y += dy

        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)

        self.leftOnGroundPoint = (self.rect.x, self.rect.centery + self.rect.h / 2 + 5)
        self.rightOnGroundPoint = (self.rect.x + self.rect.w, self.rect.centery + self.rect.h / 2 + 5)


    def collide(self, dx, dy, collisionGroup):
        for other in collisionGroup.sprites():
            if self is not other:
                if other.rect.colliderect(pygame.Rect((self.rect.x + dx, self.rect.y), self.rect.size)):
                    if dx > 0: #Going Right
                        dx = other.rect.x - (self.rect.x + self.rect.w)
                    elif dx < 0: # Going Left
                        dx = other.rect.x + other.rect.w - self.rect.x
                if other.rect.colliderect(pygame.Rect((self.rect.x, self.rect.y + dy), self.rect.size)):
                        if dy > 0: #Going Down
                            dy = other.rect.y - (self.rect.y + self.rect.h)
                            self.numJumps = 2
                            self.onGround = True
                        elif dy < 0: #Going Up
                            dy = other.rect.y + other.rect.h - self.rect.y
                            
        return (dx, dy)


    def jump(self):
        self.vel[1] = self.jumpVel
        
    def setVel(self, vel):
        self.vel = vel
        

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class PlayerCharacter(Character):

    def __init__(self, x, y):
        Character.__init__(self, x, y)

        self.numJumps = 2

    def handleInputs(self, keys):
        self.vel[0] = 0

        if keys[K_a]:
            self.vel[0] = -self.speed
        if keys[K_d]:
            self.vel[0] = self.speed

    def jump(self):
        if self.numJumps > 0:
            self.numJumps -= 1
            Character.jump(self)


    def update(self, dt, collisionGroup):
        Character.update(self, dt, collisionGroup)

        if self.onGround:
            self.numJumps = 2


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
        self.image.fill((125, 125, 125))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
