import pygame, os, function
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
txttela1 = fontesys.render("Precione F10 para salvar as marcaçoes", 1, (255, 255, 255))
txttela2 = fontesys.render("Precione F11 para carregar as marcaçoes", 1, (255, 255, 255))
txttela3 = fontesys.render("Precione F12 para excluir todas as marcaçoes", 1, (255, 255, 255))
txttela4 = fontesys.render("Precione ESC para sair", 1, (255, 255, 255))


screen.fill((255, 255, 255))
screen.blit(sky, (0, 0))
screen.blit(txttela1, (10, 10))
screen.blit(txttela2, (10, 40))
screen.blit(txttela3, (10, 70))
screen.blit(txttela4, (10, 100))


pygame.mixer.init()
pygame.mixer.music.load(os.path.join("Space_Machine_Power.mp3"))
pygame.mixer.music.play(loops=-1)

loadStar= {
    "position": 0,   
    "namestar": ""
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F10:
                function.SavePoints(item, position)
        
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            position = pygame.mouse.get_pos()
            item = simpledialog.askstring("space", "Nome da estrela: ")
            if item == "":
                item = "desconhecido " + str(position)
            fontesys = pygame.font.SysFont("Arial", 20)
            txt_estrela = fontesys.render(item, 1, (255,255,255))
            function.DrawCircle(screen, position)
            screen.blit(txt_estrela, position)
            

    



    pygame.display.update()
pygame.quit()