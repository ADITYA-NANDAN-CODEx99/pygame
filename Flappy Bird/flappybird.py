# Assets: bit.ly/3omBvO1
import pygame
import random
pygame.init()

screen  = pygame.display.set_mode((288,512))

pygame.display.set_caption("FLAPPY BIRDS")

background = pygame.image.load('imgs/background.png')
base = pygame.image.load('imgs/base.png')

#bird
x = 100
y = 300
jump = 0
speed = 0.5
birdimg = pygame.image.load('imgs/bird.png')

def draw_bird(x,y):
    screen.blit(birdimg, (x,y))

#pipes
scroll_speed = 0.5
pipeupimg = pygame.image.load('imgs/pipe-up.png')
pipedownimg = pygame.image.load('imgs/pipe-down.png')
pipe1 = [300, -170]
pipe2 = [550, -100]
Pipes = []
Pipes.append(pipe1)
Pipes.append(pipe2)

def draw_pipe(PIPE):
    screen.blit(pipeupimg, (PIPE[0], PIPE[1]))
    screen.blit(pipedownimg, (PIPE[0], PIPE[1]+420))

#score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
sCoord = (10,10)

def print_score(scr):
    screen.blit(font.render("Score: "+str(scr), True, (255,255,255)), sCoord)

#sounds
dieSound = pygame.mixer.Sound('sounds/die.wav')
hitSound = pygame.mixer.Sound('sounds/hit.wav')
swooshSound = pygame.mixer.Sound('sounds/swoosh.wav')
pointSound = pygame.mixer.Sound('sounds/point.wav')
wingSound = pygame.mixer.Sound('sounds/wing.wav')

def main_menu():
    global running
    main_menu = True
    while main_menu:
        screen.blit(background, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = True
                    main_menu = False
                    game()
                    game_over(score)
        
        menu_txt1 = font.render("PRESS SPACE", True, (255,255,255))
        menu_txt2 = font.render("TO BEGIN!", True, (255,255,255))

        if main_menu:
            screen.blit(menu_txt1, (30, 200))
            screen.blit(menu_txt2, (57, 230))

        pygame.display.update()

def game_over(s):
    global running, y, Pipes, score
    game_over = True
    while game_over:
        screen.blit(background, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = True
                    game_over = False
                    y = 300                 # default value
                    Pipes[0] = [300, -170]  # default value
                    Pipes[1] = [550, -100]  # default value
                    score = 0               # default value
                    main_menu()
        
        go_txt1 = font.render("PRESS SPACE", True, (255,255,255))
        go_txt2 = font.render("TO GO TO MENU!", True, (255,255,255))
        hs_txt = font.render("FINAL SCORE: " + str(s), True, (255,255,255))

        if game_over:
            screen.blit(go_txt1, (30, 230))
            screen.blit(go_txt2, (10, 260))
            screen.blit(hs_txt, (15, 170))

        pygame.display.update()

running = False

def game():
    global running, x, y, jump, score

    while running:
        screen.blit(background, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    wingSound.play()
                    jump = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jump = 0
            
        #bird movement
        draw_bird(x,y)
        if jump == 1:
            y -= 1.5
        else:
            y += speed

        #pipe movement
        for i in Pipes:
            draw_pipe(i)
            i[0] -= scroll_speed
            if i[0] <= -100:
                i[0] = 500
                i[1] = random.randint(-250,-100)

        #game over
        for i in Pipes:
            if y >= 400 or y <= 0:
                hitSound.play()
                dieSound.play()
                running = False
            if i[0] == 100:
                if y<=i[1]+320 or y>=i[1]+420:
                    hitSound.play()
                    dieSound.play()
                    running = False
                else:
                    pointSound.play()
                    score+=1

        print_score(score)
        screen.blit(base, (0,410))
        pygame.display.update()

main_menu()
