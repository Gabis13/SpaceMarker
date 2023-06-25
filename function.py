import pygame
def DrawCircle(scren, position):
    pygame.draw.circle(scren, (255, 255, 255), position, 5)

def SavePoints ():
    stars = {}
    with open("bd.position", "w") as file:
        for key, value in stars.items():
            x,y = value["pos"]
            name = value["name"]
            file.write(f'{key}: {x}: {y}:{name}\n')

def LoadPoints ():
    stars = {}
    try: 
        with open("bd.position","r") as file:
            for line in file:
                key, x, y, name = line.strip().split(":") 
                stars[key] = {'pos': (int(x), int(y)), "name": name}
    except FileNotFoundError:
        print("nao encontrado")


