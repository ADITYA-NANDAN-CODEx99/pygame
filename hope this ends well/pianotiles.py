import pygame, random

pygame.init()

WW, WH = 400, 600
WINDOW = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('IDK THE NAME YET!')
clock = pygame.time.Clock()


def reset_tiles(t_template, t_list):
    t_template = tile.copy()
    t_template.x = i + 7.5
    t_list.append(t_template)

def main():
    # some main vars
    tiles = []
    tw, th = WW/6, 100
    vy = 5
    tile = pygame.Rect(0, 0, tw, th)
    pos = []
    for i in range(0, WW-WW//5, WW//5):
        pos.append(i)
        

    empty = random.choice([0, 1, 2, 3, 4])

    running = True
    while running:
        clock.tick(60)

        WINDOW.fill((0, 0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False


        for t in tiles:
            pygame.draw.rect(WINDOW, (255, 255, 255), t)
            if tiles.index(t) != empty:
                t.y += vy
            if t.top > WH:
                t.bottom = 0
                empty = random.choice([0, 1, 2, 3, 4])

        pygame.display.update()

main() # -_-