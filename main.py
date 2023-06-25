import pygame
import os
import function
from tkinter import simpledialog

pygame.init()
screen = pygame.display.set_mode((0, 0,), pygame.FULLSCREEN)
sky = pygame.image.load("bg.jpg")
screen_width, screen_height = screen.get_size()
sky = pygame.transform.scale(sky, (screen_width, screen_height))
pygame.display.set_caption("SpaceMarker")
spaceIco = pygame.image.load("space.png")
space = pygame.image.load("space.png")
pygame.display.set_icon(spaceIco)

pygame.font.init()
fontesys = pygame.font.SysFont("Arial", 25)
txttela1 = fontesys.render(
    "Precione F10 para salvar as marcaçoes", 1, (255, 255, 255))
txttela2 = fontesys.render(
    "Precione F11 para carregar as marcaçoes", 1, (255, 255, 255))
txttela3 = fontesys.render(
    "Precione F12 para excluir todas as marcaçoes", 1, (255, 255, 255))
txttela4 = fontesys.render("Precione ESC para sair", 1, (255, 255, 255))

def ResetScreen():
    screen.fill((255, 255, 255))
    screen.blit(sky, (0, 0))
    screen.blit(txttela1, (10, 10))
    screen.blit(txttela2, (10, 40))
    screen.blit(txttela3, (10, 70))
    screen.blit(txttela4, (10, 100))

ResetScreen()
pygame.mixer.init()
pygame.mixer.music.load(os.path.join("Space_Machine_Power.mp3"))
pygame.mixer.music.play(loops=-1)

stars = {}
sequence = []

def SavePoints():
    with open("bd.position", "w") as file:
        for key, value in stars.items():
            x, y = value["pos"]
            name = value["name"]
            file.write(f'{key}: {x}: {y}:{name}\n')

def LoadPoints():
    stars.clear()
    sequence.clear()
    try:
        with open("bd.position", "r") as file:
            for line in file:
                key, x, y, name = line.strip().split(":")
                stars[key] = {'pos': (int(x), int(y)), "name": name}
                sequence.append(stars[key]['pos'])
    except FileNotFoundError:
        print("nao encontrado")

def DrawLine ():
    pygame.draw.lines(screen, (255,255,255), False, sequence, 2)
    ultima = sequence[-1]
    penultima = sequence[-2]
    distancia = ((penultima[0] + ultima[0]) // 2, (penultima[1] + ultima[1]) // 2)
    fontesys = pygame.font.SysFont("Arial", 20)
    txt_distancia = fontesys.render("distacia em px: " + str(distancia[0] + distancia[1]), 1, (255, 255, 255))
    screen.blit(txt_distancia, distancia)
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            SavePoints()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F10:
                SavePoints()
            elif event.key == pygame.K_F11:
                LoadPoints()
                ResetScreen()
                for star in stars.values():
                    position = star['pos']
                    pygame.draw.circle(screen, (255, 255, 255), position, 5)
                    font = pygame.font.SysFont("Arial", 20)
                    fontesys = pygame.font.SysFont("Arial", 20)
                    txt_estrela = fontesys.render(
                        star["name"], 1, (255, 255, 255))
                    screen.blit(txt_estrela, position)
                if len(sequence) > 1:
                    DrawLine()
            elif event.key == pygame.K_F12:
                stars = {}
                sequence = []
                open("bd.position", "w")
                ResetScreen()

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            position = pygame.mouse.get_pos()
            item = simpledialog.askstring("space", "Nome da estrela: ")
            if item == "":
                item = "desconhecido " + str(position)
            fontesys = pygame.font.SysFont("Arial", 20)
            txt_estrela = fontesys.render(item, 1, (255, 255, 255))
            key = str(pygame.time.get_ticks())
            stars[key] = {"pos": position, "name": item}
            function.DrawCircle(screen, position)
            screen.blit(txt_estrela, position)
            sequence.append(position)
            if len(sequence) > 1:
                DrawLine()

    pygame.display.update()
pygame.quit()
