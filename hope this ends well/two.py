
import pygame, random

pygame.init()

WW, WH = 300, 600
WINDOW = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('IDK THE NAME YET!')
clock = pygame.time.Clock()
fps = 60
G = 0.25

def draw_player(rect):
    pygame.draw.rect(WINDOW, (255, 255, 255), rect)

def main():

    # some main vars

    # Player
    pw, ph = WW/4, 10
    vx = 0
    speed = 5
    prect = pygame.Rect(175, WH - 50, pw, ph)
    prect.x = WW/2 - prect.width/2

    # Enemy
    enemies = []
    ew, eh = WW/3, 20
    ev = 0
    erect = pygame.Rect(0, -ew, ew, eh)
    for i in range(0, WW, WW//3):
        e = erect.copy()
        e.x = i
        enemies.append(e)

    running = True
    while running:
        clock.tick(fps)

        WINDOW.fill((0, 0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    vx = speed
                if e.key == pygame.K_LEFT:
                    vx = -speed

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT or e.key == pygame.K_LEFT:
                    vx = 0
        # General
        if 0 > prect.left:
            prect.left = 0
        elif WW < prect.right:
            prect.right = WW

        # Enemy
        for i in enemies:
            pygame.draw.rect(WINDOW, (255, 255, 255), i)
            i.y += ev
            if i.top > WH:
                ev = 0
                i.bottom = 0


        ev += G                 # GRAVITY

        prect.x += vx
        draw_player(prect)

        pygame.display.update()

main()