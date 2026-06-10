import pygame
import sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('')
clock = pygame.time.Clock()
tile_size = 16

gn = pygame.image.load('background/asteroid1.png')
gg = pygame.image.load('background/asteroid2.png')
gf = pygame.image.load('background/blue-back.png')
pd = pygame.image.load('background/blue-stars.png')

ec = pygame.image.load('background/blue-with-stars.png')
ce = pygame.image.load('background/prop-planet-big.png')
dc = pygame.image.load('background/pro-planet-samll.png')


tiles_img = {
    'gn': gn,
    'gg': gg,
    'gf': gf,
    'pd': pd,
    'ec': ec,
    'ce': ce,
    'dc': dc,   
}

mapa = [
    'gg,gg,gg,gg,gn,gn,gg,gg,gg,gg,gg,gg,gf,gn',
    'gn,gf,gg,gg,gf,gf,gg,gf,gf,gg,gg,gf,gn,gn',
    'gn,gn,gg,gg,gg,gg,gf,gf,gf,gg,gf,gf,gf,gf',
    'gg,gg,gg,gg,gf,gg,gg,gf,gf,gg,gf,gf,gg,gf',
    'gn,gg,gg,gg,gf,gg,gf,gg,gg,gf,gf,gn,gg,gg',
    'gg,gf,gf,gg,pd,pd,pd,gf,gg,gf,gg,gf,gn,gg',
    'gf,gn,gg,pd,pd,gf,gg,gf,gf,gg,gf,gg,gg,gn',
    'gg,gg,pd,pd,gg,gf,gg,gg,gf,gf,gf,gg,gg,gf',
    'gg,gg,gn,gf,gn,gg,gf,gg,gf,gf,gn,gf,gg,gg',
    'gf,gf,gf,gg,gg,gg,gf,gf,gg,gg,gn,gg,gf,gn',
]

colunas = len(mapa[0].split(','))
linhas = len(mapa)
offset_x = (800 - colunas * tile_size) // 2
offset_y = (600 - linhas * tile_size) // 2

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    dt = clock.get_time()
    screen.fill((20, 24, 46))

#primeiro mapa
    for i in range(len(mapa)):
        tiles = mapa[i].split(',')
        for j in range(len(tiles)):
            tile = tiles[j]
            if tile in tiles_img:
                screen.blit(tiles_img[tile], (offset_x +
                            j * tile_size, offset_y + i * tile_size))

        



    pygame.display.update()