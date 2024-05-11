import pygame as pg
from config_jogo import ConfigJogo,Music
from tela_historia import Historia
from tela_inicio import Inicio
from tela_selecao_p1 import Selecao1
from tela_personagem1 import Personagem1
from tela_selecao_p2 import Selecao2
from tela_personagem2 import Personagem2
from tela_jogo import TelaJogo
from tela_vencendor import TelaVencedor

class Jogo:
    def __init__(self):
        pg.init()                
        self.tela = pg.display.set_mode((ConfigJogo.LARGURA_TELA, ConfigJogo.ALTURA_TELA))
        pg.display.set_caption('The Game of OOP')
        Icon = pg.image.load(r'./imagens/icon/ICON.png')
        pg.display.set_icon(Icon)
        self.music = Music()
        
    def rodar(self):
        while True:
            self.music.play()
            if ConfigJogo.TELA == 'inicio':
                cena = Inicio(self.tela)
                cena.rodar()
            if ConfigJogo.TELA == 'historia':
                cena = Historia(self.tela)
                cena.rodar()
            if ConfigJogo.TELA == 'selecao1':
                cena = Selecao1(self.tela)
                cena.rodar()
            if ConfigJogo.TELA == 'personagem1':
                cena = Personagem1(self.tela)
                cena.rodar()    
            if ConfigJogo.TELA == 'selecao2':
                cena = Selecao2(self.tela)
                cena.rodar()
            if ConfigJogo.TELA == 'personagem2':
                cena = Personagem2(self.tela)
                cena.rodar()
            if ConfigJogo.TELA == 'jogo':
                ConfigJogo.ALTURA_TELA = 736
                ConfigJogo.LARGURA_TELA = 1120
                self.tela = pg.display.set_mode((ConfigJogo.LARGURA_TELA, ConfigJogo.ALTURA_TELA))
                cena = TelaJogo(self.tela)
                cena.rodar()
            if ConfigJogo.TELA == 'vencedor':
                cena = TelaVencedor(self.tela)
                cena.rodar()

                
                

