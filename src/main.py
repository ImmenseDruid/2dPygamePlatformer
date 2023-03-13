import pygame
import entities
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
        
    tiles.append(entities.Tile(6 * 64, 200 - 64))

    tiles.append(entities.Tile(3 * 64, 200 - 64 * 3))

    for tile in tiles:
        tile.add(visibleGroup, collisionGroup)



    screen = pygame.display.set_mode((1000, 800))
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    player.jump()

        keys = pygame.key.get_pressed()

        player.handleInputs(keys)

        for sprite in kinematicGroup.sprites():
            sprite.update(0.05, collisionGroup)

        screen.fill((0,0,0))

        visibleGroup.draw(screen)

        pygame.draw.line(screen, (255,255,255), (player.rect.centerx + -5, player.rect.centery), (player.rect.centerx + -5 + player.acc[0], player.rect.centery + player.acc[1]))
        pygame.draw.line(screen, (255,255,255), (player.rect.centerx + 5, player.rect.centery), (player.rect.centerx + 5 + player.vel[0], player.rect.centery + player.vel[1]))

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()