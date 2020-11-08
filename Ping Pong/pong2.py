import pygame, random

pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
BLUE = (100, 100, 255)
colors = [RED, GREEN, BLUE]

WW, WH = 800, 600
screen = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('PING PONG!')

clock = pygame.time.Clock()

level = 1
opponent_speed = 5

font = pygame.font.Font('Roboto-Thin.ttf', 32)
med_font = pygame.font.Font('Roboto-Thin.ttf', 48)
big_font = pygame.font.Font('Roboto-Thin.ttf', 128)

score_time = None
# chalu ho gaya
ball = pygame.Rect(WW//2-15, WH//2-15, 30, 30)
ball_speed = 6
ball_speed_x, ball_speed_y = 6 * random.choice((-1, 1)), 6 * random.choice((-1, 1))

player = pygame.Rect(WW-20, WW//2-60, 10, 120)
p_score = 0
player_speed = 0

opponent = pygame.Rect(10, WH//2-60, 10, 120)
o_score = 0

pong_sound = pygame.mixer.Sound('pong.ogg')
score_sound = pygame.mixer.Sound('score.ogg')

score_time = None

def ball_restart():
    global ball_speed_x, ball_speed_y, score_time, WH, WW

    ball.center = (WW//2, WH//2)
    current_time = pygame.time.get_ticks()

    if current_time - score_time < 1000:
        ball_speed_x = 0
        ball_speed_y = 0
        three = big_font.render("3", False, (200,200,200))
        screen.blit(three, (WW//2-three.get_rect().width//2, WH//2+50))

    elif 1000 < current_time - score_time < 2000:
        ball_speed_x = 0
        ball_speed_y = 0
        two = big_font.render("2", False, (200,200,200))
        screen.blit(two, (WW//2-two.get_rect().width//2, WH//2+50))
    
    elif 2000 < current_time - score_time < 3000:
        ball_speed_x = 0
        ball_speed_y = 0
        one = big_font.render("1", False, (200,200,200))
        screen.blit(one, (WW//2-one.get_rect().width//2, WH//2+50))

    elif current_time - score_time > 3000:
        ball_speed_x = ball_speed*random.choice((-1,1))
        ball_speed_y = ball_speed*random.choice((-1,1))
        print(ball_speed)
        score_time = None

def start_game(opponent_speed, ball_color, paddle_color):
    global p_score, o_score, player_speed, ball_speed_x, ball_speed_y, score_time
    global welcome_screen, player, opponent, ball, ball_speed
    o_color = random.choice((RED, GREEN, BLUE))
    while o_color == ball_color or o_color == paddle_color:
        o_color = random.choice((RED, GREEN, BLUE))
    running = True
    while running:
        screen.fill((0, 0, 0))
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    player_speed += 7
                if e.key == pygame.K_UP:
                    player_speed -= 7
                
                if e.key == pygame.K_ESCAPE:
                    welcome_screen = True
                    running = False
                    # Defaults
                    ball = pygame.Rect(WW//2-15, WH//2-15, 30, 30)
                    player = pygame.Rect(WW-20, WW//2-60, 10, 120)
                    ball_speed = 6
                    opponent = pygame.Rect(10, WH//2-60, 10, 120)
                    ball_speed_x, ball_speed_y = 6 * random.choice((-1, 1)), 6 * random.choice((-1, 1))
                    o_score, p_score = 0, 0

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_DOWN or e.key == pygame.K_UP:
                    player_speed = 0
        
        # player movement
        player.y += player_speed
        if player.top <= 0:
            player.top = 0
        if player.bottom >= WH:
            player.bottom = WH

        # Ball movement
        ball.x += ball_speed_x
        ball.y += ball_speed_y
        if ball.top <= 0 or ball.bottom >= WH:
            pong_sound.play()
            ball_speed_y *= -1

        # opponent movement
        if opponent.bottom < ball.y:
            opponent.bottom += opponent_speed
        if opponent.top > ball.y:
            opponent.top -= opponent_speed

        # Scoring
        if ball.left <= 0:
            p_score += 1
            if ball_speed < 10:
                ball_speed += 0.5
            score_sound.play()
            score_time = pygame.time.get_ticks()
        if ball.right >= WW:
            o_score += 1
            if ball_speed < 10:
                ball_speed += 0.5
            score_sound.play()
            score_time = pygame.time.get_ticks()

        # collision
        if ball.colliderect(player) or ball.colliderect(opponent):
            pong_sound.play()
            if ball.left <= player.right or ball.right > opponent.left:
                ball_speed_x *= -1

        if score_time:
            ball_restart()

        pygame.draw.rect(screen, paddle_color, player)
        pygame.draw.rect(screen, o_color, opponent)
        pygame.draw.ellipse(screen, ball_color, ball)
        pygame.draw.aaline(screen, ball_color, (WW//2, 0), (WW//2, WH))

        player_text = font.render(str(p_score), True, ball_color)
        screen.blit(player_text, (WW//2 + 20, WH//2 - 56))

        opponent_text = font.render(str(o_score), True, ball_color)
        screen.blit(opponent_text, (WW//2 - 40, WH//2 - 56))

        esc = font.render("PRESS ESC TO GO BACK TO MAIN MENU", True, ball_color)
        screen.blit(esc, (WW//2-esc.get_rect().width//2, WH-50))

        b_speed = font.render("SPEED: "+ str(ball_speed), True, ball_color)
        screen.blit(b_speed, (WW//2-b_speed.get_rect().width//2, 0))

        pygame.display.update()

        clock.tick(60)

def ball_color_change(opponent_speed):          # First
    ball_color_change = True
    ball_color = WHITE
    while ball_color_change:
        screen.fill((0, 0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                ball_color_change = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    ball_color_change = False
                    paddle_color_change(opponent_speed, ball_color)
                if e.key == pygame.K_1:
                    ball_color = WHITE
                if e.key == pygame.K_2:
                    ball_color = RED
                if e.key == pygame.K_3:
                    ball_color = GREEN
                if e.key == pygame.K_4:
                    ball_color = BLUE
        
        w1 = 400
        h1 = 40
        if ball_color == WHITE:
            pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(WW//2-w1//2, WH-300, w1, h1))
        elif ball_color == RED:
            pygame.draw.rect(screen, (50, 0, 0), pygame.Rect(WW//2-w1//2, WH-225, w1, h1))
        elif ball_color == GREEN:
            pygame.draw.rect(screen, (0, 50, 0), pygame.Rect(WW//2-w1//2, WH-150, w1, h1))
        elif ball_color == BLUE:
            pygame.draw.rect(screen, (0, 0, 50), pygame.Rect(WW//2-w1//2, WH-75, w1, h1))

        Welcome_Message = big_font.render("PING - PONG", True, (200,200,200))
        screen.blit(Welcome_Message, (WW//2-Welcome_Message.get_rect().width//2, 10))

        bcolor = med_font.render("1) SELECT BALL COLOR:", True, (200,200,200))
        screen.blit(bcolor, (WW//2-bcolor.get_rect().width//2, WH-400))

        white = font.render("PRESS 1 FOR WHITE", True, WHITE)
        screen.blit(white, (WW//2-white.get_rect().width//2, WH-300))

        red = font.render("PRESS 2 FOR RED", True, RED)
        screen.blit(red, (WW//2-red.get_rect().width//2, WH-225))

        green = font.render("PRESS 3 FOR GREEN", True, GREEN)
        screen.blit(green, (WW//2-green.get_rect().width//2, WH-150))

        blue = font.render("PRESS 4 FOR BLUE", True, BLUE)
        screen.blit(blue, (WW//2-blue.get_rect().width//2, WH-75))

        pygame.display.update()

def paddle_color_change(opponent_speed, b_color):       # Second
    paddle_color_change = True
    paddle_color = WHITE
    while paddle_color_change:
        screen.fill((0, 0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                paddle_color_change = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    paddle_color_change = False
                    start_game(opponent_speed, b_color, paddle_color)
                if e.key == pygame.K_1:
                    paddle_color = WHITE
                if e.key == pygame.K_2:
                    paddle_color = RED
                if e.key == pygame.K_3:
                    paddle_color = GREEN
                if e.key == pygame.K_4:
                    paddle_color = BLUE
        
        w1 = 400
        h1 = 40
        if paddle_color == WHITE:
            pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(WW//2-w1//2, WH-300, w1, h1))
        elif paddle_color == RED:
            pygame.draw.rect(screen, (50, 0, 0), pygame.Rect(WW//2-w1//2, WH-225, w1, h1))
        elif paddle_color == GREEN:
            pygame.draw.rect(screen, (0, 50, 0), pygame.Rect(WW//2-w1//2, WH-150, w1, h1))
        elif paddle_color == BLUE:
            pygame.draw.rect(screen, (0, 0, 50), pygame.Rect(WW//2-w1//2, WH-75, w1, h1))

        Welcome_Message = big_font.render("PING - PONG", True, (200,200,200))
        screen.blit(Welcome_Message, (WW//2-Welcome_Message.get_rect().width//2, 10))

        p_color = med_font.render("2) SELECT PADDLE COLOR:", True, (200,200,200))
        screen.blit(p_color, (WW//2-p_color.get_rect().width//2, WH-400))

        white = font.render("PRESS 1 FOR WHITE", True, WHITE)
        screen.blit(white, (WW//2-white.get_rect().width//2, WH-300))

        red = font.render("PRESS 2 FOR RED", True, RED)
        screen.blit(red, (WW//2-red.get_rect().width//2, WH-225))

        green = font.render("PRESS 3 FOR GREEN", True, GREEN)
        screen.blit(green, (WW//2-green.get_rect().width//2, WH-150))

        blue = font.render("PRESS 4 FOR BLUE", True, BLUE)
        screen.blit(blue, (WW//2-blue.get_rect().width//2, WH-75))

        pygame.display.update()


welcome_screen = True
while welcome_screen:
    screen.fill((0, 0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            welcome_screen = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                welcome_screen = False
                ball_color_change(opponent_speed)
            if e.key == pygame.K_1:
                opponent_speed = 5
                level = 1
            if e.key == pygame.K_2:
                opponent_speed = 10
                level = 2
            if e.key == pygame.K_3:
                opponent_speed = 15
                level = 3
    w = 190
    c = 50
    if level == 1:
        pygame.draw.rect(screen, (c, c, c), pygame.Rect(WW//2-w//2, WH-400, w, 60))
    elif level == 2:
        pygame.draw.rect(screen, (c, c, c), pygame.Rect(WW//2-w//2, WH-300, w, 60))
    elif level == 3:
        pygame.draw.rect(screen, (c, c, c), pygame.Rect(WW//2-w//2, WH-200, w, 60))

    Welcome_Message = big_font.render("PING - PONG", True, (200,200,200))
    screen.blit(Welcome_Message, (WW//2-Welcome_Message.get_rect().width//2, 10))

    # Select_Level = med_font.render("SELECT LEVEL", True, (200,200,200))
    # screen.blit(Select_Level, (WW//2-Select_Level.get_rect().width//2, 130))

    Easy = med_font.render("EASY", True, (200,200,200))
    screen.blit(Easy, (WW//2-Easy.get_rect().width//2, WH-400))

    Medium = med_font.render("MEDIUM", True, (200,200,200))
    screen.blit(Medium, (WW//2-Medium.get_rect().width//2, WH-300))

    Hard = med_font.render("HARD", True, (200,200,200))
    screen.blit(Hard, (WW//2-Hard.get_rect().width//2, WH-200))

    Start = font.render("PRESS ENTER TO START AND, ", True, (200,200,200))
    screen.blit(Start, (WW//2-Start.get_rect().width//2, WH-100))

    Start2 = font.render("1, 2, 3 TO SELECT DIFFICULTY", True, (200,200,200))
    screen.blit(Start2, (WW//2-Start2.get_rect().width//2, WH-50))

    pygame.display.update()

pygame.quit()