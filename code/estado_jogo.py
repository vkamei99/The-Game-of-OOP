import pygame as pg
from config_jogo import ConfigJogo, scale, img
from cronometro import Cronometro
from characters import Lista_p1
from characters import Lista_p2

class Estadojogo:
    def __init__(self, p1, p2):
        self.font_vida = pg.font.SysFont(None, 28)
        self.font_tempo = pg.font.SysFont(None, 48)
        self.cronometro = Cronometro()
        self.resetar()

        self.p1 = p1
        self.p2 = p2

        #barra de vida
        self.altura = 10
        self.multiplicador = 1.5
        self.vida_p1_reset = self.p1.vida
        self.vida_p2_reset = self.p2.vida
        #barra de cooldown
        self.largura_cooldown = 100

    def resetar(self):
        self.cronometro.reset()

    def jogo_terminou(self):
        if (self.p1.vida <= 0) or (self.p2.vida <= 0) or (self.cronometro.tempo_passado() > ConfigJogo.DURACAO_PARTIDA):
            return True
        else:
            return False

    def desenha(self, tela):
        self.desenha_ui(tela)
        self.desenha_tempo(tela)
    
    def desenha_ui(self, tela):
    #player 1
        #desenha rosto
        img_rosto_p1 = scale(self.p1.sprite[3], 0.7)
        if self.p1.atacando2:
            img_rosto_p1 = scale(self.p1.sprite[4], 0.65)

        tela.blit(img_rosto_p1, (0, 0))

        #desenha vida e barra de vida
        img_vida_p1 = self.font_vida.render(f'{self.p1.vida:.0f}/{self.vida_p1_reset}', True, (0, 0, 0))
        rect_fundo_vida_p1 = pg.rect.Rect(img_rosto_p1.get_width() + 2, img_vida_p1.get_height()+ 5, self.vida_p1_reset * self.multiplicador, self.altura)
        rect_vida_p1 = pg.rect.Rect(img_rosto_p1.get_width() + 2, img_vida_p1.get_height()+ 5, self.p1.vida * self.multiplicador, self.altura)
        tela.blit(img_vida_p1, (img_rosto_p1.get_width() + 2, 5))
        pg.draw.rect(tela, (100,10,10), rect_fundo_vida_p1)
        pg.draw.rect(tela, 'red', rect_vida_p1)

        #desenha barra cooldown 1
        cooldown1 = self.p1.ataque2.retorna_cooldown()
        razao1 = cooldown1 / self.p1.ataque2.tempo_cooldown
        largura_cooldown1 = self.largura_cooldown * razao1
        rect_fundo_cooldown_p1 = pg.rect.Rect(img_rosto_p1.get_width() + 2, 35, self.largura_cooldown, self.altura)
        rect_cooldown_p1 = pg.rect.Rect(img_rosto_p1.get_width() + 2, 35, largura_cooldown1, self.altura)
        pg.draw.rect(tela, 'black', rect_fundo_cooldown_p1)
        pg.draw.rect(tela, (10,10,200), rect_cooldown_p1)

    #player 2
        #desenha rosto
        img_rosto_p2 = pg.transform.flip(scale(self.p2.sprite[3], 0.7), True, False)
        if self.p2.atacando2:
            img_rosto_p2 = pg.transform.flip(scale(self.p2.sprite[4], 0.65), True, False)
        tela.blit(img_rosto_p2, (ConfigJogo.LARGURA_TELA - img_rosto_p2.get_width(), 0))
        
        #desenha vida e barra de vida
        img_vida_p2 = self.font_vida.render(f'{self.p2.vida:.0f}/{self.vida_p2_reset}', True, (0, 0, 0))
        rect_fundo_vida_p2 = pg.rect.Rect(ConfigJogo.LARGURA_TELA - img_rosto_p2.get_width() - self.vida_p2_reset*self.multiplicador - 2, img_vida_p1.get_height() + 5, self.vida_p2_reset * self.multiplicador, self.altura)
        rect_vida_p2 = pg.rect.Rect(ConfigJogo.LARGURA_TELA - img_rosto_p2.get_width() - self.p2.vida*self.multiplicador - 2, img_vida_p1.get_height() + 5, self.p2.vida * self.multiplicador, self.altura)
        tela.blit(img_vida_p2, (ConfigJogo.LARGURA_TELA - img_rosto_p2.get_width() - img_vida_p2.get_width() - 2, 5))
        pg.draw.rect(tela, (10,10,10), rect_fundo_vida_p2)
        pg.draw.rect(tela, 'red', rect_vida_p2)

        #desenha barra cooldown 1
        cooldown2 = self.p2.ataque2.retorna_cooldown()
        razao2 = cooldown2 / self.p2.ataque2.tempo_cooldown
        largura_cooldown2 = self.largura_cooldown * razao2
        rect_fundo_cooldown_p2 = pg.rect.Rect(ConfigJogo.LARGURA_TELA - img_rosto_p2.get_width() - self.largura_cooldown -2, 35, self.largura_cooldown, self.altura)
        rect_cooldown_p2 = pg.rect.Rect(ConfigJogo.LARGURA_TELA - img_rosto_p2.get_width() -  largura_cooldown2-2, 35, largura_cooldown2, self.altura)
        pg.draw.rect(tela, 'black', rect_fundo_cooldown_p2)
        pg.draw.rect(tela, (10,10,200), rect_cooldown_p2)

    def desenha_tempo(self, tela):
        tempo = ConfigJogo.DURACAO_PARTIDA - self.cronometro.tempo_passado()
        
        img = self.font_tempo.render(f'{tempo:.0f}',True, 'black')
        
        px = ConfigJogo.LARGURA_TELA // 2 - img.get_size()[0] // 2
        py = ConfigJogo.ALTURA_TEMPO
        
        tela.blit(img, (px, py))
