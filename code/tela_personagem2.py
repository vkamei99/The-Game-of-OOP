import pygame as pg
import sys
from config_jogo import ConfigJogo, load_image, poze


class Personagem2:
    def __init__(self, tela):
        self.tela = tela
        self.rodando = True

        self.isolde = load_image(r'./imagens/telas/tela_isoldes.png', scale=1)
        self.pitbull = load_image(r'./imagens/telas/tela_pitbull.png', scale=1)
        self.lacertus = load_image(r'./imagens/telas/tela_acertus.png', scale=1)
        self.draco = load_image(r'./imagens/telas/tela_draco.png', scale=1)

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
                ConfigJogo.TELA = 'selecao2'
            if (event.type == pg.KEYDOWN and event.key == pg.K_SPACE):
                self.rodando = False
                ConfigJogo.TELA = 'jogo'
                        
    def desenha(self):
        if ConfigJogo.PERSONAGEM_P2 == 0:
            self.tela.blit(self.isolde,(0, 0, ConfigJogo.LARGURA_TELA, ConfigJogo.ALTURA_TELA))
        if ConfigJogo.PERSONAGEM_P2 == 1:
            self.tela.blit(self.pitbull,(0, 0, ConfigJogo.LARGURA_TELA, ConfigJogo.ALTURA_TELA))
        if ConfigJogo.PERSONAGEM_P2 == 2:
            self.tela.blit(self.lacertus,(0, 0, ConfigJogo.LARGURA_TELA, ConfigJogo.ALTURA_TELA))
        if ConfigJogo.PERSONAGEM_P2 == 3:
            self.tela.blit(self.draco,(0, 0, ConfigJogo.LARGURA_TELA, ConfigJogo.ALTURA_TELA))
        pg.display.flip()