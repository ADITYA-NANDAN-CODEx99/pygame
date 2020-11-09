import pygame
from pytmx import load_pygame, TiledTileLayer
import pyscroll

pygame.init()

# Game settings
WW, WH = 800, 600
window = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('MapGame!')
imgs = []
clock = pygame.time.Clock()

# Player Properties
p_dir = None
player_speed = 5
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("imgs/player.png").convert_alpha()
        # self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()

player = Player()
player_rect = player.rect

# Map settings
map1 = load_pygame('map.tmx')
map_data = pyscroll.TiledMapData(map1)
map_layer = pyscroll.BufferedRenderer(map_data, (WW, WH))
group = pyscroll.PyscrollGroup(map_layer=map_layer)
group.add(player)

running = True
while running:
    # BGColor, Which is not visible ;)
    window.fill((0, 0, 0))

    # FPS
    clock.tick(60)

    # Events
    for e in pygame.event.get():

        # Quiting the game
        if e.type == pygame.QUIT:
            running = False

        # Player ka movement
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                p_dir = 'up'
            if e.key == pygame.K_DOWN:
                p_dir = 'down'
            if e.key == pygame.K_RIGHT:
                p_dir = 'right'
            if e.key == pygame.K_LEFT:
                p_dir = 'left'
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                p_dir = 'None'
            if e.key == pygame.K_RIGHT or e.key == pygame.K_LEFT:
                p_dir = 'None'

    if p_dir == 'up':
        player.rect.y -= player_speed
    if p_dir == 'down':
        player.rect.y += player_speed
    if p_dir == 'right':
        player.rect.x += player_speed
    if p_dir == 'left':
        player.rect.x -= player_speed

    # collision
    for sprite in group:
        if player.rect.colliderect(sprite):
            if p_dir == 'right':
                player.rect.x -= player_speed

    group.center(player.rect.center)
    group.draw(window)
    
    pygame.display.update()