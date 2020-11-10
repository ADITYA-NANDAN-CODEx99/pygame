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
        self.rect = self.image.get_rect()
        self.rect.center = WW//2, WH//2

player = Player()

# Map settings
map1 = load_pygame('map1.tmx')
map_data = pyscroll.TiledMapData(map1)
map_layer = pyscroll.BufferedRenderer(map_data, (WW, WH))
all_group = pyscroll.PyscrollGroup(map_layer=map_layer)
all_group.add(player)

obs_layer = map1.get_layer_by_name('Obstacles')

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
    for x in range(50):
        for y in range(50):
            sprite = map1.get_tile_image(x, y, 1)
            if sprite != None:
                sprite_rect = sprite.get_rect()
                sprite_rect.x = x * 64
                sprite_rect.y = y * 64
                if player.rect.colliderect(sprite_rect):
                    if p_dir == 'up':
                        player.rect.y += player_speed
                    if p_dir == 'down':
                        player.rect.y -= player_speed
                    if p_dir == 'right':
                        player.rect.x -= player_speed
                    if p_dir == 'left':
                        player.rect.x += player_speed

    all_group.center(player.rect.center)
    all_group.draw(window)
    
    pygame.display.update()
