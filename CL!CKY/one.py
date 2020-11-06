import pygame, random

pygame.init()

clock = pygame.time.Clock()

WW, WH = 600, 400
screen = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('cl!ckY')
font = pygame.font.Font('english_essay.ttf', 32)

running = True

xy = [100, 100]
size = 50
score = 0

def generate_box (x, y):
    return pygame.Rect(x, y, size, size)

def print_scr (scr):
    s = font.render('Score: '+ str(scr), True, (255, 255, 255))
    screen.blit(s, (WW//2 - s.get_rect().width//2, 0))

def isClicked(xy, mx, my):
    global score
    if xy[0] < mx < xy[0]+size and xy[1] < my < xy[1] + size:
        score += 1
        return True
    return False

clicked = False
start_time = pygame.time.get_ticks()
while running:
    screen.fill((0, 0, 0))
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                clicked = True
        if e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1:
                clicked = False
    
    mx, my = pygame.mouse.get_pos()

    box = generate_box(xy[0], xy[1])
    pygame.draw.ellipse(screen, (255, 255, 255), box)

    current_time = pygame.time.get_ticks()

    if current_time - start_time > 1000:
        start_time = pygame.time.get_ticks()
        xy = [random.randint(0, WW-size), random.randint(0, WH-size)]
    
    if clicked:
        if (current_time - start_time < 1000) and isClicked(xy, mx, my):
            start_time = pygame.time.get_ticks()
            xy = [random.randint(0, WW-size), random.randint(0, WH-size)]

    print_scr(score)

    clock.tick(30)
    pygame.display.update()