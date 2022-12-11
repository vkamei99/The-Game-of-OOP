import pygame as pg
from pygame import font, mixer

pg.init()
pg.font.init()

class ConfigJogo:
    LARGURA_TELA = 1080
    ALTURA_TELA = 720
    FONT_SIZE = 48
    TELA = 'inicio'

    PERSONAGEM_P1 = 0
    PERSONAGEM_P2 = 0

    ALTURA_TEMPO = 20
    DURACAO_PARTIDA = 180

    LARGURA_SPRITE = 30
    ALTURA_SPRITE = 50

    TAMANHO_TILE = 32

    TILEMAP = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,0,0,0,0,0,2,2,2,2,2,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,0,0,0,0,0,0,0,2,2,2,2,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,2,2,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,2,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,3,3,3,2,2,2,3,3,3,2,2,2,2,2,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,3,3,3,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,2,2,2,2,2,3,3,3,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,2,2,2,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]


    imagem_bricks = pg.image.load(r'./mapa/sprites/bricks.png')
    imagem_agua = pg.image.load(r'./mapa/sprites/agua.png')
    imagem_cooblestone = pg.image.load(r'./mapa/sprites/cooblestone.png')
    imagem_stone = pg.image.load(r'./mapa/sprites/Stone.png')
    
def img (diretorio):
    return pg.image.load(diretorio)

def scale(imagem, scale = 1.0):
    size = imagem.get_size()
    size = (int(size[0] * scale), int(size[1] * scale))
    return pg.transform.scale(imagem, size)

def debug(tela, info, x = 10, y = 10, size=30):
    font = pg.font.Font(None,size)
    texto= font.render(str(info),True,'White')
    debug_rect = texto.get_rect(topleft = (x,y))
    pg.draw.rect(tela,'Black',debug_rect)
    tela.blit(texto,debug_rect)
    
def load_image(name, colorkey=None, scale=1.0):
        image = pg.image.load(name)

        size = image.get_size()
        size = (int(size[0] * scale), int(size[1] * scale))
        image = pg.transform.scale(image, size)

        image = image.convert_alpha()
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pg.RLEACCEL)
        return image

def poze():
    pass