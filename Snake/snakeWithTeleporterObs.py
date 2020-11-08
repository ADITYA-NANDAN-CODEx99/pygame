import pygame
import random

pygame.init()

# Window
WH, WW = 615, 615
WINDOW = pygame.display.set_mode((WH, WW))
pygame.display.set_caption("SNAKE GAME")

fps = 7
food_count_for_increasing_speed = 0
step = 30
up = (0, -step)
down = (0, step)
left = (-step, 0)
right = (step, 0)

direction = left      # DEFAULT

score = 0

f_size = 50
f_increment = 10
f_max = 100
f_min = f_size
f_go_size = 50
font = pygame.font.Font('Roboto-Thin.ttf', f_size)

snake_pos = [
    [210, 210], 
    [240, 210], 
    [270, 210], 
    [300, 210]
]

food_pos = [210 - step*2, 210]

game_over = False

running = True
while running:

    pygame.time.Clock().tick(fps)
    WINDOW.fill((150, 0, 200))

    # if not game_over:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                direction = up
            if e.key == pygame.K_DOWN:
                direction = down
            if e.key == pygame.K_RIGHT:
                direction = right
            if e.key == pygame.K_LEFT:
                direction = left
    
    if snake_pos[0] == food_pos:        # eating food
        x_range = list(range(step, WW, step))
        y_range = list(range(step, WH, step))
        food_pos = [random.choice(x_range), random.choice(y_range)]
        snake_pos.append(snake_pos[-1])
        score += 1
        f_size += f_increment
        if f_size > f_max:
            f_increment *= -1
        if f_size <= f_min:
            f_increment *= -1
        food_count_for_increasing_speed += 1
        if food_count_for_increasing_speed == 5:
            food_count_for_increasing_speed = 0
            if fps < 50:
                fps += 1

    for i in range(1, len(snake_pos)):
        if snake_pos[0] == snake_pos[i]:
            game_over = True

    # Drawing
    for x, y in snake_pos:
        pygame.draw.circle(WINDOW, (255, 255, 255), (x, y), int(step/2))
    pygame.draw.circle(WINDOW, (255, 0, 255), food_pos, int(step/2))
    

    if not game_over:
        snake_pos = [
            [snake_pos[0][0] + direction[0], 
            snake_pos[0][1] + direction[1]]
        ] + snake_pos[:-1]
    
    if game_over:
        font = pygame.font.Font('Roboto-Thin.ttf', int(f_go_size))
        go_text = font.render("TOTAL SCORE = "+ str(score), True, (255, 255, 255))
        go_text_w, go_text_h = go_text.get_rect().width, go_text.get_rect().height
        WINDOW.blit(go_text, (WW/2 - go_text_w/2, WH/2 - go_text_h/2))

    if not game_over:
        font = pygame.font.Font('Roboto-Thin.ttf', int(f_size))
        text = font.render(str(score), True, (255, 255, 255))
        text_w, text_h = text.get_rect().width, text.get_rect().height
        WINDOW.blit(text, (WW/2 - text_w/2, WH/2 - text_h/2))

    last_x = WW - int(step/2)
    last_y = WH - int(step/2)

    if snake_pos[0][0] < 0:             # left side
        snake_pos[0][0] = last_x
    if snake_pos[0][0] > last_x:        # right side
        snake_pos[0][0] = 0

    if snake_pos[0][1] < 0:             # upar wali side
        snake_pos[0][1] = last_y
    if snake_pos[0][1] > last_y:        # niche wali side
        snake_pos[0][1] = 0

    pygame.display.update()

pygame.quit()