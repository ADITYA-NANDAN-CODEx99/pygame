import pygame, random

pygame.init()

WW, WH = 400, 600
WINDOW = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('Piano Tiles')
clock = pygame.time.Clock()


def new_tiles_1b(t_template):
    empty = random.choice([0, 1, 2, 3, 4])
    t_list = []
    for i, n in zip(range(0, WW+1, WW//5), range(5)):
        if n != empty:
            t = t_template.copy()
            t.x = i + 7.5
            t_list.append(t)
    return t_list

def new_tiles_4b(t_template):
    empty = random.choice([0, 1, 2, 3])
    t_list = []
    for i, n in zip(range(0, WW+1, WW//4), range(4)):
        if n == empty:
            t = t_template.copy()
            t.x = i + 7.5
            t_list.append(t)
    return t_list

def move_tiles(t_list, t_template, vel):
    
    for t in t_list:
            pygame.draw.rect(WINDOW, (255, 255, 255), t)

            t.y += vel

            if t.top > WH:
                t_list = new_tiles_4b(t_template)
                if vel < 10:
                    vel += 1
                break

def main():
    # some main vars
    tw, th = WW/6, 100
    vy = 5
    tile1 = pygame.Rect(0, -th, tw, th)
    tile2 = pygame.Rect(0, -th*3, tw, th)
    
    tiles1 = new_tiles_4b(tile1)
    tiles2 = new_tiles_4b(tile2)

    running = True
    while running:
        clock.tick(60)

        WINDOW.fill((0, 0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        move_tiles(tiles1, tile1, vy)
        move_tiles(tiles2, tile2, vy)

        pygame.display.update()

main() # -_-
