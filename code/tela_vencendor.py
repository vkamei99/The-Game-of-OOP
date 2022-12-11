import pygame as pg
import sys
from config_jogo import ConfigJogo, load_image, debug
from characters import Lista_p1, Lista_p2

class TelaVencedor:
    def __init__(self, tela):
        self.tela = tela
        self.imagem_de_fundo1 = load_image(r'./imagens/telas/tela_vencedor_p1.png', scale=1)
        self.imagem_de_fundo2 = load_image(r'./imagens/telas/tela_vencedor_p2.png', scale=1)
        self.rodando = True
        self.p1 = Lista_p1[ConfigJogo.PERSONAGEM_P1]
        self.p2 = Lista_p2[ConfigJogo.PERSONAGEM_P2]
        self.font = pg.font.SysFont(None, 40)

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
                sys.exit()
            
    def desenha(self):
        if self.p1.vida > self.p2.vida:
            self.tela.blit(self.imagem_de_fundo1,(0, 0, ConfigJogo.LARGURA_TELA, ConfigJogo.ALTURA_TELA))
        if self.p2.vida > self.p1.vida:
            self.tela.blit(self.imagem_de_fundo2,(0, 0, ConfigJogo.LARGURA_TELA, ConfigJogo.ALTURA_TELA))
        pg.display.flip()