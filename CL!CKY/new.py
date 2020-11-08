import pygame, random

pygame.init()

clock = pygame.time.Clock()

WW, WH = 600, 400
screen = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('cl!ckY')
font = pygame.font.Font('Roboto-Thin.ttf', 32)
big_font = pygame.font.Font('Roboto-Thin.ttf', 64)

score = 0

def time_out_mode(st):
    global MainRun
    start_time = st

    xy = [100, 100]
    size = 50
    score = 0

    m = pygame.Rect(0, 0, 25, 25)

    def generate_box (x, y):
        return pygame.Rect(x, y, size, size)

    def print_scr (scr):
        s = font.render('Score: '+ str(scr), True, (255, 255, 255))
        screen.blit(s, (WW//2 - s.get_rect().width//2, 0))

    def isClicked(r1, r2):
        if r1.colliderect(r2):
            return True
        return False

    clicked = False
    # start_time = pygame.time.get_ticks()
    time_out_running = True
    while time_out_running:
        screen.fill((0, 0, 0))
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                time_out_running = False

            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    clicked = True
            if e.type == pygame.MOUSEBUTTONUP:
                if e.button == 1:
                    clicked = False
        
        mx, my = pygame.mouse.get_pos()
        m.center = pygame.mouse.get_pos()

        box = generate_box(xy[0], xy[1])
        pygame.draw.ellipse(screen, (255, 255, 255), box)
        pygame.draw.ellipse(screen, (255, 255, 255), m)

        current_time = pygame.time.get_ticks()

        if current_time - start_time > 1000:
            start_time = pygame.time.get_ticks()
            xy = [random.randint(0, WW-size), random.randint(0, WH-size)]
        
        if clicked:
            if (current_time - start_time < 1000) and isClicked(box, m):
                score += 1
                start_time = pygame.time.get_ticks()
                xy = [random.randint(0, WW-size), random.randint(0, WH-size)]

        game_time = pygame.time.get_ticks()
        if game_time - start_time >= 10000:
            screen.fill((200, 200, 200))

            msg = font.render('Game Over!', True, (255, 255, 255))
            screen.blit(msg, (WW//2 - msg.get_rect().width//2, 100))

            fs = font.render('Final Score: '+ str(score), True, (255, 255, 255))
            screen.blit(fs, (WW//2 - fs.get_rect().width//2, 100))

        print_scr(score)

        clock.tick(30)
        pygame.display.update()


mode = 0 ## Arcade or Timeout
state = 0

clicked = False
MainRun = True
while MainRun:
    screen.fill((0, 0, 0))
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            MainRun = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                clicked = True
        if e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1:
                clicked = False
    
    mx, my = pygame.mouse.get_pos()

    Welcome_Message = big_font.render("CL!CKY", True, (200,200,200))
    screen.blit(Welcome_Message, (WW//2-Welcome_Message.get_rect().width//2, 10))

    set_mode = font.render("Set Mode:", True, (200,200,200))
    screen.blit(set_mode, (WW//2-set_mode.get_rect().width//2, 150))

    timeout = font.render("1) Timeout", True, (200,200,200))
    screen.blit(timeout, (WW//2-timeout.get_rect().width//2, 200))

    arcade = font.render("2) Arcade", True, (200,200,200))
    screen.blit(arcade, (WW//2-arcade.get_rect().width//2, 250))

    start = big_font.render("Start Game!", True, (200,200,200))
    screen.blit(start, (WW//2-start.get_rect().width//2, 325))

    t_rect = timeout.get_rect()
    t_rect.x, t_rect.y = WW//2-timeout.get_rect().width//2, 200

    a_rect = arcade.get_rect()
    a_rect.x, a_rect.y = WW//2-arcade.get_rect().width//2, 250

    s_rect = start.get_rect()
    s_rect.x, s_rect.y = WW//2-start.get_rect().width//2, 325

    if clicked and state == 0:
        if t_rect.x < mx < t_rect.x + t_rect.width and t_rect.y < my < t_rect.y + t_rect.height:
            mode = 1
        elif a_rect.x < mx < a_rect.x + a_rect.width and a_rect.y < my < a_rect.y + a_rect.height:
            mode = 2
        elif s_rect.x < mx < s_rect.x + s_rect.width and s_rect.y < my < s_rect.y + s_rect.height:
            state = 1

    if mode == 1:
        pygame.draw.rect(screen, (200, 200, 200), t_rect, 1)
    elif mode == 2:
        pygame.draw.rect(screen, (200, 200, 200), a_rect, 1)

    if state == 1:
        pygame.draw.rect(screen, (0, 200, 0), s_rect, 1)
        if mode == 1:
            MainRun = False
            time_out_mode(pygame.time.get_ticks())
        if mode == 2:
            MainRun = False


    pygame.display.update()