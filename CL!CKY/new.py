import pygame, random

pygame.init()

clock = pygame.time.Clock()

WW, WH = 600, 400

cursor = pygame.image.load('cursor2.png')
cursor90 = pygame.image.load('cursor90.png')
screen = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('CL!CKY')
pygame.display.set_icon(cursor)
font = pygame.font.Font('Roboto-Thin.ttf', 32)
big_font = pygame.font.Font('Roboto-Thin.ttf', 64)

score = 0
size = 50
ball_color = pygame.color.Color(255, 255, 255)

def generate_box (x, y):
    return pygame.Rect(x, y, size, size)

def print_scr (scr, color):
    s = font.render('Score: '+ str(scr), True, color)
    screen.blit(s, (WW//2 - s.get_rect().width//2, 0))

tCoord = (0,0)
def timer(t, color):
    screen.blit(font.render("Time Left: "+str(t), True, color), tCoord)

def isClicked(r1, r2):
    if r1.colliderect(r2):
        return True
    return False


def time_out_mode(st):
    global MainRun, score
    main_start_time = st
    time_limit = 10000
    time_left_in_secs = time_limit // 1000

    xy = [100, 100]
    score = 0

    m = pygame.Rect(0, 0, 25, 25)

    clicked = False
    start_time = pygame.time.get_ticks()
    time_out_running = True
    r, g, b = 255, 255, 255
    while time_out_running:
        screen.fill((0, 0, 0))
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                time_out_running = False
                MainRun = False

            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    clicked = True
            if e.type == pygame.MOUSEBUTTONUP:
                if e.button == 1:
                    clicked = False
        
        mx, my = pygame.mouse.get_pos()
        m.center = pygame.mouse.get_pos()

        box = generate_box(xy[0], xy[1])
        pygame.draw.ellipse(screen, (r, g, b), box)
        pygame.draw.ellipse(screen, (r, g, b), m)

        current_time = pygame.time.get_ticks()

        if current_time - start_time > 1000:
            start_time = pygame.time.get_ticks()
            xy = [random.randint(0, WW-size), random.randint(0, WH-size)]
        
        if clicked:
            if (current_time - start_time < 1000) and isClicked(box, m):
                r = random.randint(100, 255)
                g = random.randint(100, 255)
                b = random.randint(100, 255)
                score += 1
                start_time = pygame.time.get_ticks()
                xy = [random.randint(0, WW-size), random.randint(0, WH-size)]
                clicked = False

        print_scr(score, (r, g, b))

        game_time = pygame.time.get_ticks()
        if pygame.time.get_ticks() % 1000 < 10:
            time_left_in_secs -= 1
        
        # timer(time_left_in_secs, (r, g, b))

        ## Game Over
        if game_time - main_start_time >= time_limit:
            time_out_running = False

        clock.tick(30)
        pygame.display.update()

def arcade_mode():
    life = 10
    life_rect = pygame.Rect(0, 15, 15, 15)
    clicked = False
    global MainRun, score

    xy = [100, 100]
    score = 0

    m = pygame.Rect(0, 0, 25, 25)

    clicked = False
    start_time = pygame.time.get_ticks()
    arcade_running = True

    r, g, b = 255, 255, 255

    while arcade_running:
        screen.fill((0, 0, 0))
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                arcade_running = False
                MainRun = False

            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    clicked = True
            if e.type == pygame.MOUSEBUTTONUP:
                if e.button == 1:
                    clicked = False
        
        mx, my = pygame.mouse.get_pos()
        m.center = pygame.mouse.get_pos()

        box = generate_box(xy[0], xy[1])
        pygame.draw.ellipse(screen, (r, g, b), box)
        pygame.draw.ellipse(screen, (r, g, b), m)

        current_time = pygame.time.get_ticks()

        if current_time - start_time > 1000:
            start_time = pygame.time.get_ticks()
            xy = [random.randint(0, WW-size), random.randint(0, WH-size)]
            life -= 1
        
        if clicked:
            if (current_time - start_time < 1000) and isClicked(box, m):
                r = random.randint(100, 255)
                g = random.randint(100, 255)
                b = random.randint(100, 255)
                score += 1
                start_time = pygame.time.get_ticks()
                xy = [random.randint(0, WW-size), random.randint(0, WH-size)]
                clicked = False
            if not isClicked(box, m):
                life -= 1
                clicked = False

        print_scr(score, (r, g, b))

        # drawing lives (and not saving lives xD)
        p = 0
        for i in range(life):
            rect = life_rect.copy()
            p += rect.width
            rect.x = p
            pygame.draw.ellipse(screen, (r, g, b), rect)

        ## Game Over
        if life <= 0:
            arcade_running = False

        clock.tick(30)
        pygame.display.update()

def game_over():
    global MainRun, mode, state, clicked
    game_over = True
    while game_over:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                MainRun = False
                game_over = False
            if e.type == pygame.KEYDOWN:
                game_over = False
                MainRun = True
                mode = 0            # No mode set now
                state = 0           # game not started right now
                clicked = False

        screen.fill((0, 0, 0))

        msg = big_font.render('Game Over!', True, (255, 255, 255))
        screen.blit(msg, (WW//2 - msg.get_rect().width//2, 100))

        fs = font.render('Final Score: '+ str(score), True, (255, 255, 255))
        screen.blit(fs, (WW//2 - fs.get_rect().width//2, 200))

        back = font.render('Press any key to go back to menu!', True, (255, 255, 255))
        screen.blit(back, (WW//2 - back.get_rect().width//2, 300))

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

    if mode == 1:
        pygame.draw.rect(screen, (50, 50, 50), t_rect)
    elif mode == 2:
        pygame.draw.rect(screen, (50, 50, 50), a_rect)

    if state == 1 and mode != 0:
        pygame.draw.rect(screen, (0, 50, 0), s_rect)
        if mode == 1:       # Timeout
            time_out_mode(pygame.time.get_ticks())
            game_over()
        if mode == 2:       # Arcade
            arcade_mode()
            game_over()

    Welcome_Message = big_font.render("CL!CKY", True, (200,200,200))
    w_rect = Welcome_Message.get_rect()
    w_rect.x, w_rect.y = WW//2-Welcome_Message.get_rect().width//2, 10
    screen.blit(Welcome_Message, w_rect)
    screen.blit(cursor, (w_rect.x - cursor.get_rect().width, w_rect.y))
    screen.blit(cursor, (w_rect.x + w_rect.width, w_rect.y))

    set_mode = font.render("Set Mode:", True, (200,200,200))
    screen.blit(set_mode, (WW//2-set_mode.get_rect().width//2, 150))

    timeout = font.render("Timeout", True, (200,200,200))
    screen.blit(timeout, (WW//2-timeout.get_rect().width//2, 200))

    arcade = font.render("Arcade", True, (200,200,200))
    screen.blit(arcade, (WW//2-arcade.get_rect().width//2, 250))

    start = big_font.render("Start Game!", True, (200,200,200))
    screen.blit(start, (WW//2-start.get_rect().width//2, 325))

    t_rect = timeout.get_rect()
    t_rect.x, t_rect.y = WW//2-timeout.get_rect().width//2, 200
    screen.blit(cursor90, (t_rect.x - cursor90.get_rect().width, t_rect.y - 5))

    a_rect = arcade.get_rect()
    a_rect.x, a_rect.y = WW//2-arcade.get_rect().width//2, 250
    screen.blit(cursor90, (a_rect.x - cursor90.get_rect().width, a_rect.y - 5))

    s_rect = start.get_rect()
    s_rect.x, s_rect.y = WW//2-start.get_rect().width//2, 325

    if clicked and state == 0:
        if t_rect.x < mx < t_rect.x + t_rect.width and t_rect.y < my < t_rect.y + t_rect.height:
            mode = 1
        elif a_rect.x < mx < a_rect.x + a_rect.width and a_rect.y < my < a_rect.y + a_rect.height:
            mode = 2
        if mode != 0:
            if s_rect.x < mx < s_rect.x + s_rect.width and s_rect.y < my < s_rect.y + s_rect.height:
                state = 1


    pygame.display.update()
