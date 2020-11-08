import pygame, random, sys

pygame.init()

WW, WH = 800, 600
screen = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('DANCING BALLS!')

clock = pygame.time.Clock()

# font = pygame.font.Font('Roboto-Thin.ttf', 32)

G = 1               # u can edit this ;)

class Ball:
    def __init__(self, x, y, radius, vx, vy, damping, color):
        self.vx = vx
        self.vy = vy
        self.damping = damping
        self.color = color
        self.rect = pygame.Rect(x, y, radius, radius)

    def draw(self):
        self.rect.x += int(self.vx)
        self.rect.y += int(self.vy)

        self.vy += G

        if self.rect.top <= 0 or self.rect.bottom >= WH:
            self.vy *= -(1 - self.damping)
        if self.rect.left <= 0 or self.rect.right >= WW:
            self.vx *= -(1 - self.damping)

        pygame.draw.ellipse(screen, self.color, self.rect)

    def theEdgeCase(self):
        if self.rect.top <= 0:
            self.rect.top = 0 + 1
        if self.rect.bottom >= WH:
            self.rect.bottom = WH - 1
        if self.rect.left <= 0:
            self.rect.left = 0 + 1
        if self.rect.right >= WW:
            self.rect.right = WW - 1

balls = []
for i in range(250):         # u can edit this ;)
    x, y = random.randint(25, WW - 25), random.randint(25, WH - 25)
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    s = random.randint(25, 51)
    vx = random.randint(-15, 16)
    vy = random.randint(-15, 16)
    balls.append(Ball(x, y, s, vx, vy, 0.045, (r, g, b)))       # u can edit this ;)

r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

running = True

while running:
    clock.tick(120)
    ran = range(-3, 4, 1)
    
    r += random.choice(ran)
    g += random.choice(ran)
    b += random.choice(ran)
    if r > 255 or r < 0:
        r = random.randint(0, 255)
    if g > 255 or g < 0:
        g = random.randint(0, 255)
    if b > 255 or b < 0:
        b = random.randint(0, 255)
    screen.fill((r, g, b))
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    for i in balls:
        i.draw()
        i.theEdgeCase()

    pygame.display.update()

    clock.tick(60)
        
pygame.quit()