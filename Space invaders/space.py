import pygame
import random
import math

pygame.init()

WW, WH = 800, 600
screen = pygame.display.set_mode((WW, WH))

# Images
icon = pygame.image.load('imgs/bullet.png')
background = pygame.image.load('imgs/background.png')
player_img =  pygame.image.load('imgs/si.png')
bullet_img = pygame.image.load('imgs/bullet.png')

# Default Values
## Player
pspeed = 4
px, py = 400, 400
pxChange, pyChange = 0, 0

## Enemy
enemy_img =  []
espeed = []
ex, ey = [], []
exChange, eyChange = [], []
enum = 5
exSpeedIncr = 1.1

def define_values():
    for i in range(enum):
        enemy_img.append(pygame.image.load('imgs/alien.png'))
        ex.append(random.randint(100, WW - 100))
        ey.append(random.randint(100, WH - 400))
        exChange.append(3)
        eyChange.append(15)

define_values()

# Back Music
pygame.mixer.music.load('sounds/background.wav')
pygame.mixer.music.play(-1)

# sounds
explosion = pygame.mixer.Sound('sounds/explosion.wav')
fire = pygame.mixer.Sound('sounds/laser.wav')

## Bullet

bx, by = px, py
bspeed = -10
bstate = 0              # ready

# score
score = 0
font = pygame.font.Font('Fonts/Roboto-Thin.ttf', 32)
scrPos = (10, 10)

# Functions
def player (x, y):
    screen.blit(player_img, (x, y))

def enemy (x, y, i):
    screen.blit(enemy_img[i], (x, y))

def draw_bullet (x, y):
    global bstate
    bstate = 1          # firing
    screen.blit(bullet_img, (x, y))

def isCollision (x1, y1, x2, y2):
    dist = math.sqrt( (x1 - x2) ** 2 + (y2 - y1) ** 2 )
    if dist < 64:
        return True
    return False

def game_over_text(score):
    offset = 30
    msg = pygame.font.Font('Fonts/Roboto-Thin.ttf', 64)
    msgImg = msg.render('GAME OVER, DUDE!', True, (255, 255, 255))
    mPos = (WW//2 - msgImg.get_rect().width//2, 
            WH//2 - msgImg.get_rect().height//2 - offset)
    screen.blit(msgImg, mPos)

    fs = pygame.font.Font('Fonts/Roboto-Thin.ttf', 64)
    fsImg = msg.render('FINAL SCORE: '+str(score), True, (255, 255, 255))
    fsPos = (WW//2 - fsImg.get_rect().width//2, 
            WH//2 - fsImg.get_rect().height//2 + offset)
    screen.blit(fsImg, fsPos)

def scr_print(scr):
    screen.blit(font.render("SCORE: " + str(scr), True, (255, 255, 255)), scrPos)

def start_screen():
    offset = 30
    msg = pygame.font.Font('Fonts/Roboto-Thin.ttf', 64)
    msgImg = msg.render('SPACE INVADERS!', True, (255, 255, 255))
    mPos = (WW//2 - msgImg.get_rect().width//2, 
            WH//2 - msgImg.get_rect().height//2 - offset)
    screen.blit(msgImg, mPos)

    fs = pygame.font.Font('Fonts/Roboto-Thin.ttf', 64)
    fsImg = fs.render("PRESS 'P' TO PLAY", True, (255, 255, 255))
    fsPos = (WW//2 - fsImg.get_rect().width//2, 
            WH//2 - fsImg.get_rect().height//2 + offset)
    screen.blit(fsImg, fsPos)

pygame.display.set_icon(icon)

game_start = False
game_over = False

count = 0

running = True
while running:
    count += 1

    screen.fill((50, 50, 50))
    screen.blit(background, (0, 0))

    if not game_start:
        start_screen()

    px += pxChange
    py += pyChange

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            # only on starting screen
            if e.key == pygame.K_p and game_start == False:
                game_start = True

            # Player movement
            if game_start:
                if e.key == pygame.K_LEFT:
                    pxChange = -pspeed
                if e.key == pygame.K_RIGHT:
                    pxChange = pspeed
                
                if e.key == pygame.K_UP:
                    pyChange = -pspeed
                if e.key == pygame.K_DOWN:
                    pyChange = pspeed
                
                if e.key == pygame.K_SPACE:
                    # Bullet sounds
                    # bullet_sound = pygame.mixer.Sound('sounds/laser.wav')
                    fire.play()

                    bx, by = px, py
                    # draw_bullet(bx, by)
                    bstate = 1
        
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                pxChange = 0
            if e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                pyChange = 0

    # Teleportation of player
    if px < -32:
        px = WW - 32
    if px > WW - 32:
        px = 0

    # Enemies
    if game_start:
        for i in range(enum):
            # Game Over
            if ey[i] >= WH - 200:
                game_over = True
                break

            # Enemy Movement
            ex[i] += exChange[i]
            enemy(ex[i], ey[i], i)
            if ex[i] > WW - 32 or ex[i] < -32:
                ey[i] += eyChange[i]
                exChange[i] *= -1 * exSpeedIncr
            
            # Colllision b/w bullet and enemy
            if isCollision(bx, by, ex[i], ey[i]) and bstate == 1:
                explosion.play()
                exChange[i] = 3
                ex[i], ey[i] = random.randint(100, WW - 100), random.randint(100, WH - 500)
                bstate = 0
                score += 1
            
            # Collision b/w enemy and player
            if isCollision(px, py, ex[i], ey[i]):
                explosion.play()
                game_over = True

        
        # Bullet Movement
        if bstate == 1 and not game_over:
            draw_bullet(bx, by)
            by += bspeed
            if by < 0:
                bstate = 0

        if game_over:
            for j in range(enum):
                ey[j] = 800
            py = 800
            game_over_text(score)

        # Score
        scr_print(score)

        if count >= 500:
            enum += 1
            define_values()
            count = 0
        
        player(px, py)

    pygame.display.update()