import pygame


font = None
if pygame.font.get_init() == False:
    pygame.font.init()

font = pygame.font.SysFont("TimesNewRoman", 16)


def printToScreen(screen, text, pos):
    image = font.render(text, False, (255, 255, 255), None)
    screen.blit(image, pos)