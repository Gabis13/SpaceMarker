import pygame
import winsound



pygame.init()
scale = (800,600)
white = (255,255,255)
screen =  pygame.display.set_mode( scale )
pygame.display.set_caption("SpaceMarker")
running = True
sky = pygame.image.load("bg.jpg")
spaceIco = pygame.image.load("space.ico")
space = pygame.image.load("space.png")

pygame.display.set_icon(spaceIco)


while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()