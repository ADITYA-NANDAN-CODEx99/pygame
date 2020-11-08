import pygame, random

pygame.init()

WW, WH = 400, 600
WINDOW = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('Piano Tiles')
clock = pygame.time.Clock()

def main():
    # some main vars
    v = 5
    t1 = pygame.Rect(0, 0, WW//4, 150)

    tiles = []
    pos = []

    for i in range(0, WW, WW//4):
        pos.append(i)
        t = t1.copy()
        t.x = i
        tiles.append(t)

    running = True
    while running:
        clock.tick(60)

        WINDOW.fill((0, 0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        
        ### DRAWING ###
        pygame.draw.rect(WINDOW, (255, 255, 255), tiles[0])

        ### GRID ###
        for j in pos:
            if j != 0:
                pygame.draw.line(WINDOW, (255, 255, 255), (j, 0), (j, WH))

        pygame.display.update()

main() # -_-

# kk bb time to eat something :P