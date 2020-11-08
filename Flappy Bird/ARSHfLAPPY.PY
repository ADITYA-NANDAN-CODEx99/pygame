import pygame
import random

pygame.init()

sw = 288
sh = 512
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Flappy Birds")
font = pygame.font.SysFont('Arial', 32)
background = pygame.image.load('imgs/background.png')
base = pygame.image.load('imgs/base.png')
speed = 1


# Main Game Loop
def Start_Game(OS):
    # Bird
    x = 100
    y = 300
    jump = 0
    birdimg = pygame.image.load('imgs/bird.png')

    def draw_bird(x, y):
        screen.blit(birdimg, (x, y))

    # Pipes
    pipeupimg = pygame.image.load('imgs/pipe-up.png')
    pipedownimg = pygame.image.load('imgs/pipe-down.png')
    pipe1 = [300, -170]
    pipe2 = [550, -100]

    Pipes = []
    Pipes.append(pipe1)
    Pipes.append(pipe2)

    def draw_pipe(PIPE):
        screen.blit(pipeupimg, (PIPE[0], PIPE[1]))
        screen.blit(pipedownimg, (PIPE[0], PIPE[1] + 420))

    # Score
    score = 0
    sCoord = (10, 10)

    def print_score(scr):
        screen.blit(font.render("Score: " + str(scr), True, (255, 255, 255)), sCoord)

    # Sounds
    dieSound = pygame.mixer.Sound('sounds/die.wav')
    hitSound = pygame.mixer.Sound('sounds/hit.wav')
    swooshSound = pygame.mixer.Sound('sounds/swoosh.wav')
    pointSound = pygame.mixer.Sound('sounds/point.wav')
    wingSound = pygame.mixer.Sound('sounds/wing.wav')

    running = True
    while running:
        # screen.fill((120, 120, 255))
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    wingSound.play()
                    jump = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jump = 0

        # Bird movement
        draw_bird(x, y)
        if jump == 1:
            y -= 1.5
        else:
            y += speed

        # Pipe Movement
        for i in Pipes:
            draw_pipe(i)
            i[0] -= 1
            if i[0] <= 0:
                i[0] = 500
                i[1] = random.randint(-250, -100)

        # Game Over
        for i in Pipes:
            if i[0] == 100:
                if y <= i[1] + 320 or y >= i[1] + 420:
                    hitSound.play()
                    dieSound.play()
                    print("Game Over!!")
                    running = False
                else:
                    pointSound.play()
                    score += 1
                    print(score)

    print_score(score)
    screen.blit(base, (0, 410))
    pygame.display.update()


WelcomeScreen = True
while WelcomeScreen: 
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.QUIT:
                WelcomeScreen = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    WelcomeScreen = False
                    Start_Game(speed)

    Welcome1 = font.render("WELCOME TO", True, (255, 255, 255))
    screen.blit(Welcome1, (37, 30))
    Welcome2 = font.render("FLAPPY BIRD!", True, (255, 255, 255))
    screen.blit(Welcome2, (37, 80))
    Start1 = font.render("PRESS SPACE", True, (255, 255, 255))
    screen.blit(Start1, (33, sh - 150))
    Start2 = font.render("TO START", True, (255, 255, 255))
    screen.blit(Start2, (63, sh - 100))

    pygame.display.update()