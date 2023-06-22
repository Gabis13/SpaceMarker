import pygame
import winsound
from tkinter import simpledialog


pygame.init()
scale = (800,600)
white = (255,255,255)
screen =  pygame.display.set_mode( scale )
pygame.display.set_caption("SpaceMarker")
running = True
sky = pygame.image.load("bg.jpg")
spaceIco = pygame.image.load("space.png")
space = pygame.image.load("space.png")
star = []


pygame.display.set_icon(spaceIco)


while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:" )
            print(item)
            if item == None:
                item = "desconhecido"+str(pos)
            star[item] = pos

    screen.fill(white)
    screen.blit( sky, (0,0) )

    pygame.display.update()
pygame.quit()