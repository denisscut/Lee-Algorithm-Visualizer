import pygame
import random

COLORS = [(128,0,0), 
          (220,20,60),
          (139,0,0),
          (220,20,60)]

pygame.font.init()
font = pygame.font.SysFont('Arial', 70)
text = font.render(str("You took the sword."), True, (255, 255, 255))

def random_color():
    return random.choice(COLORS)

frame = 25
drum = [(0,12)]
bine = False
stop = True
nr = 0
fps = pygame.time.Clock()
box = 50
mat = [[0 for _ in range(13)] for _ in range(13)]
win = pygame.display.set_mode((650,650))
coada = [(12,0)]
run = True
gata = True
finishx = 0
finishy = 12
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
mat[12][0] = 1
posx = 0
posy = 600
start2 = False

def draw_window(win, posx, posy, frame):
    win.fill((0, 0, 0))
    bg = pygame.image.load("bg.jpg")
    stalp = pygame.image.load("1.png")
    sabie = pygame.image.load("sword.png")
    pygame.draw.rect(win, (200,200,200), (0, 0, 650, 650), 1)
    win.blit(bg, (0,0))
    mouse = pygame.draw.rect(win, (200, 230, 200), (posx, posy, 50, 50))
    win.blit(sabie, (600, 0))

    for i in range(13):
        for j in range(13):
            if mat[i][j] > 1 and gata:
                pygame.draw.rect(win, random_color(), (j * 50, i * 50, 50, 50))
            elif mat[i][j] == -1:
                win.blit(stalp, (j * 50, i * 50))

    for i in range(25):
        pygame.draw.line(win, (255, 255, 255), (i*50, 0), (i*50, 650), 1)
        pygame.draw.line(win, (255, 255, 255), (0, i*50), (650, i*50), 1)

    fps.tick(frame)
    pygame.display.update()


for i in range(12):
    for j in range(7):
        l = random.randint(0, 12)
        if i != finishx and j != finishy:
            mat[i][l] = -1

def reset():
    for i in range(12):
        for j in range(12):
            mat[i][j] = 0
    
    mat[12][0] = 1

    for i in range(12):
        for j in range(4):
            l = random.randint(0, 12)
            if i != finishx and l != finishy:
                mat[i][l] = -1

def main():
    global run, gata, start2, stop, bine
    while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        reset()
                        main()

        while coada != [] and run and gata:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                
            # if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_r:
                        


            x = coada[0][0]
            y = coada[0][1]
            x = x - 1

            if x == finishx and y == finishy:
                gata = False

            if x >= 0 and x <= 12 and y >= 0 and y <= 12 and mat[x][y] == 0:
                mat[x][y] = mat[coada[0][0]][coada[0][1]] + 1
                coada.append((x, y))
                draw_window(win, posx, posy, frame)

            x = coada[0][0]
            y = coada[0][1]
            y = y + 1

            if x == finishx and y == finishy:
                gata = False

            if x >= 0 and x <= 12 and y >= 0 and y <= 12 and mat[x][y] == 0:
                mat[x][y] = mat[coada[0][0]][coada[0][1]] + 1
                coada.append((x, y))
                draw_window(win, posx, posy, frame)

            x = coada[0][0]
            y = coada[0][1]
            y = y - 1

            if x == finishx and y == finishy:
                gata = False

            if x >= 0 and x <= 12 and y >= 0 and y <= 12 and mat[x][y] == 0:
                mat[x][y] = mat[coada[0][0]][coada[0][1]] + 1
                coada.append((x, y))
                draw_window(win, posx, posy, frame)
                
            x = coada[0][0]
            y = coada[0][1]
            x = x + 1

            if x == finishx and y == finishy:
                gata = False

            if x >= 0 and x <= 12 and y >= 0 and y <= 12 and mat[x][y] == 0:
                mat[x][y] = mat[coada[0][0]][coada[0][1]] + 1
                coada.append((x, y))
                draw_window(win, posx, posy, frame)
            coada.remove(coada[0])

        if start2 == False:
            start = mat[0][12]
            start2 = True

        if gata == False:
            bine = True
            val = mat[0][12]
            x = 0
            y = 12
            gasit = True
            doaratat = 1
            while val > 1 and stop:
                gasit = True
                for k in range(4):
                    if gasit == True:
                        newx = x + dx[k]
                        newy = y + dy[k]
                        if newx >= 0 and newx <= 12 and newy >= 0 and newy <= 12 and mat[newx][newy] == mat[x][y] - 1:
                            drum.append((x, y))
                            doaratat = doaratat + 1
                            x = newx
                            y = newy
                            val = val - 1
                            gasit = False
            stop = False
        gata = False

        if bine:
            if start > 1:
                start = start - 1
            #if start == 1:
                #win.fill((0, 0, 0))
                #win.blit(text, (150, 200))
                #pygame.display.update()
            pygame.display.flip()
            draw_window(win, drum[start][1] * 50, drum[start][0] * 50, 5)
        else:
            run = False

main()