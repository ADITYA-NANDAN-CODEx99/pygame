import pygame

pygame.init()

WW, WH = 400, 600
WINDOW = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('IDK THE NAME YET!')
clock = pygame.time.Clock()

def draw_player(rect):
    pygame.draw.rect(WINDOW, (255, 255, 255), rect)

def main():

    # some main vars
    pw, ph = 50, 75
    vx, vy = 0, 0
    speed = 5
    prect = pygame.Rect(175, WH - 100, pw, ph)

    running = True
    while running:
        clock.tick(60)

        WINDOW.fill((0, 0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    vy = -speed
                if e.key == pygame.K_DOWN:
                    vy = speed
                if e.key == pygame.K_RIGHT:
                    vx = speed
                if e.key == pygame.K_LEFT:
                    vx = -speed

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                    vy = 0
                if e.key == pygame.K_RIGHT or e.key == pygame.K_LEFT:
                    vx = 0
        # General
        if 0 > prect.left:
            prect.left = 0
        elif WW < prect.right:
            prect.right = WW
        if 0 > prect.top:
            prect.top = 0
        elif WH < prect.bottom:
            prect.bottom = WH

        prect.y += vy
        prect.x += vx
        draw_player(prect)

        pygame.display.update()

main()