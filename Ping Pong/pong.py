import pygame, random, sys

pygame.init()

WW, WH = 800, 600
screen = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('PING PONG!')

clock = pygame.time.Clock()

# chalu ho gaya
ball = pygame.Rect(WW//2-15, WH//2-15, 30, 30)
ball_speed_x, ball_speed_y = 6 * random.choice((-1, 1)), 6 * random.choice((-1, 1))

player = pygame.Rect(WW-20, WW//2-60, 10, 120)
p_score = 0
player_speed = 0

opponent = pygame.Rect(10, WH//2-60, 10, 120)
o_score = 0
opponent_speed = 5

font = pygame.font.Font('Roboto-Thin.ttf', 32)

score_time = None

def ball_restart():
    global ball_speed_x, ball_speed_y, score_time, WH, WW

    ball.center = (WW//2, WH//2)
    current_time = pygame.time.get_ticks()
    print(current_time)

    if current_time - score_time < 700:
        ball_speed_x = 0
        ball_speed_y = 0
        # num_one = 

    if current_time - score_time < 2100:
        ball_speed_x = 0
        ball_speed_y = 0
    else:
        ball_speed_x, ball_speed_y = 6 * random.choice((-1, 1)), 6 * random.choice((-1, 1))
        score_time = None

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
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= WW:
        ball_speed_x *= -1

    # opponent movement
    if opponent.bottom < ball.y:
        opponent.bottom += opponent_speed
    if opponent.top > ball.y:
        opponent.top -= opponent_speed

    # Scoring
    if ball.left <= 0:
        p_score += 1
        score_time = pygame.time.get_ticks()
    if ball.right >= WW:
        o_score += 1
        score_time = pygame.time.get_ticks()

    # collision
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    if score_time:
        ball_restart()

    pygame.draw.rect(screen, (200, 200, 200), player)
    pygame.draw.rect(screen, (200, 200, 200), opponent)
    pygame.draw.ellipse(screen, (200, 200, 200), ball)
    pygame.draw.aaline(screen, (200, 200, 200), (WW//2, 0), (WW//2, WH))

    player_text = font.render(str(p_score), True, (255, 255, 255))
    screen.blit(player_text, (WW//2 + 20, WH//2 - 56))

    opponent_text = font.render(str(o_score), True, (255, 255, 255))
    screen.blit(opponent_text, (WW//2 - 40, WH//2 - 56))

    pygame.display.update()

    clock.tick(60)
        
pygame.quit()