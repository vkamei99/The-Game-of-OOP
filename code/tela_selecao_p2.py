import pygame as pg
import sys
from config_jogo import ConfigJogo, load_image, debug

class Selecao2:
    def __init__(self, tela):
        self.tela = tela
        self.imagem_de_fundo = load_image(r'./imagens/telas/tela_de_selecao2.png', scale=1)
        self.rodando = True
        self.pos_x = ConfigJogo.LARGURA_TELA - 30 - 400
        self.pos_y = 20

        ConfigJogo.PERSONAGEM_P2 = 0

    def rodar(self):
        while self.rodando:
            self.tratamento_de_eventos()
            self.desenha()

    def tratamento_de_eventos(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                print("Encerrando o programa.")
                sys.exit()
            if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.rodando = False
                ConfigJogo.TELA = 'selecao1'
            if (event.type == pg.KEYDOWN and event.key == pg.K_SPACE):
                self.rodando = False
                ConfigJogo.TELA = 'jogo'

            if (event.type == pg.KEYDOWN and event.key == pg.K_e):
                self.rodando = False
                ConfigJogo.TELA = 'personagem2'

            if (event.type == pg.KEYDOWN and event.key == pg.K_k) and (self.pos_y  + 195 <= ConfigJogo.ALTURA_TELA):
                self.pos_y += 175
                ConfigJogo.PERSONAGEM_P2 += 1
            if (event.type == pg.KEYDOWN and event.key == pg.K_i) and (self.pos_y > 20):
                self.pos_y -= 175
                ConfigJogo.PERSONAGEM_P2 -= 1
            
    def desenha(self):
        self.tela.blit(self.imagem_de_fundo,(0, 0, ConfigJogo.LARGURA_TELA, ConfigJogo.ALTURA_TELA))
        pg.draw.rect(self.tela, 'red', (self.pos_x, self.pos_y, 400, 150), 5)
        #debug(self.tela,ConfigJogo.PERSONAGEM_P2)
        pg.display.flip()