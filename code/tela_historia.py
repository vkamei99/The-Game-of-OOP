import pygame as pg
import sys
from config_jogo import ConfigJogo, load_image

class Historia:
    def __init__(self, tela):
        self.tela = tela
        self.imagem_de_fundo = load_image(r'./imagens/telas/tela_de_historia.png', scale=1)
        self.rodando = True

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
                ConfigJogo.TELA = 'inicio'
            if (event.type == pg.KEYDOWN and event.key == pg.K_SPACE):
                self.rodando = False
                ConfigJogo.TELA = 'selecao1'

    def desenha(self):
        self.tela.blit(self.imagem_de_fundo,(0, 0, ConfigJogo.LARGURA_TELA, ConfigJogo.ALTURA_TELA))
        pg.display.flip()