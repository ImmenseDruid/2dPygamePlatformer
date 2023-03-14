import pygame
import entities
import debug
import physics
from pygame.locals import *


def main():

    pygame.init()

    visibleGroup = pygame.sprite.Group()
    kinematicGroup = pygame.sprite.Group()
    collisionGroup = pygame.sprite.Group()
    updateGroup = pygame.sprite.Group()

    player = entities.PlayerCharacter(50, 136)
    player.add(visibleGroup, collisionGroup, kinematicGroup)
    vel = [0, 0]

    tiles = []
    for i in range(10):
        tiles.append(entities.Tile(i * 64, 200))
    
    for i in range(10):
        tiles.append(entities.Tile(i * 64 + 200, 400))
        
    tiles.append(entities.Tile(6 * 64, 200 - 64))

    tiles.append(entities.Tile(3 * 64, 200 - 64 * 3))

    for tile in tiles:
        tile.add(visibleGroup, collisionGroup)



    screen = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()
    run = True

    FPS = 60
    dt = 1 # 
    physicsSubSteps = 1
    subStepDt = dt / physicsSubSteps

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    player.jump()

        keys = pygame.key.get_pressed()

        player.handleInputs(keys)

        for sprite in kinematicGroup.sprites():            
            for i in range(physicsSubSteps):
                sprite.update(subStepDt, collisionGroup)

        screen.fill((0,0,0))

        visibleGroup.draw(screen)

        pygame.draw.line(screen, (255,255,255), (player.rect.centerx + -5, player.rect.centery), (player.rect.centerx + -5 + player.acc[0], player.rect.centery + player.acc[1]))
        pygame.draw.line(screen, (255,255,255), (player.rect.centerx + 5, player.rect.centery), (player.rect.centerx + 5 + player.vel[0], player.rect.centery + player.vel[1]))
        pygame.draw.circle(screen, (255, 255, 255), (player.leftOnGroundPoint), 2)
        pygame.draw.circle(screen, (255, 255, 255), (player.rightOnGroundPoint), 2)
        debug.printToScreen(screen, "On Ground? : " + str(player.onGround), (10, 100))
        debug.printToScreen(screen, "Player Position : " + str(player.x) + ", " + str(player.y), (10, 25))
        debug.printToScreen(screen, "Player Velocity : " + str(player.vel), (10, 50))
        debug.printToScreen(screen, "Player Acceleration : " + str(player.acc), (10, 75))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()