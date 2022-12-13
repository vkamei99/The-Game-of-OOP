import pygame as pg
import math
from typing import Tuple
from config_jogo import ConfigJogo, debug
from ataques import *

class AcoesPersonagem():
    def __init__(self, posicao, stats, sprite, ataque1, ataque2):
        self.posicao = posicao[0]
        self.direcao = posicao[1]
        
        self.velocidade = stats[0]*4
        self.velocidade_reset = self.velocidade
        self.vida = stats[1]
        self.dano = stats[2]
        self.ataque_tipo = stats[3]
        
        self.direction = pg.math.Vector2()
        
        self.sprite = sprite
        self.sprite_def = 0
        self.largura = ConfigJogo.LARGURA_SPRITE
        self.altura = ConfigJogo.ALTURA_SPRITE
        x = self.posicao[0]
        y = self.posicao[1]
        self.rect = pg.rect.Rect(x,y, self.largura, self.altura)

        self.atacando1 = False
        self.atacando2 = False

        self.ataque1 = ataque1
        self.ataque2 = ataque2

    def mover_pra_cima(self):
        self.direction.y = -1
    def mover_pra_baixo(self):
        self.direction.y = 1
    def pararY(self):
        self.direction.y = 0
    def mover_pra_esquerda(self):
        self.direction.x = -1
    def mover_pra_direita(self):
        self.direction.x = 1
    def pararX(self):
        self.direction.x = 0

    def atualizar_posicao(self, mapa):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.blocos_especiais(mapa)
        self.rect.x += self.direction.x * self.velocidade
        self.colisao_mapa('horizontal', mapa)
        self.rect.y += self.direction.y * self.velocidade
        self.colisao_mapa('vertical', mapa)
        
    def colisao_player(self, pos_inimigo, colisao):
        if colisao == 'D':
            self.posicao = (pos_inimigo[0]-self.largura, self.posicao[1])
        if colisao == 'A':
            self.posicao = (pos_inimigo[0]+self.largura, self.posicao[1])
        if colisao == 'W':
            self.posicao = (self.posicao[0], pos_inimigo[1]-self.altura)
        if colisao == 'S':
            self.posicao = (self.posicao[0], pos_inimigo[1]+self.altura)

    def colisao_mapa(self, direcao, mapa):
        blocos_colidiveis = []
        for tipo_bloco_index, tipo_bloco in enumerate(mapa):
            for bloco_index, bloco in enumerate(tipo_bloco):
                if tipo_bloco_index == 1:
                    blocos_colidiveis.append(mapa[tipo_bloco_index][bloco_index].retorna_rect())
                if tipo_bloco_index == 3:
                    blocos_colidiveis.append(mapa[tipo_bloco_index][bloco_index].retorna_rect())

        if direcao == 'horizontal':
            for index, bloco in enumerate(blocos_colidiveis):
                if self.rect.colliderect(blocos_colidiveis[index]):
                    if self.direction.x > 0:
                        self.rect.right = blocos_colidiveis[index].left
                    if self.direction.x < 0:
                        self.rect.left = blocos_colidiveis[index].right
        if direcao == 'vertical':
            for index, bloco in enumerate(blocos_colidiveis):
                if self.rect.colliderect(blocos_colidiveis[index]):
                    if self.direction.y > 0:
                        self.rect.bottom = blocos_colidiveis[index].top
                    if self.direction.y < 0:
                        self.rect.top = blocos_colidiveis[index].bottom

    def blocos_especiais(self, mapa):
        blocos_especiais = []
        for tipo_bloco_index, tipo_bloco in enumerate(mapa):
            for bloco_index, bloco in enumerate(tipo_bloco):
                if tipo_bloco_index == 0:
                    blocos_especiais.append(mapa[tipo_bloco_index][bloco_index].retorna_rect())
  
        if self.rect.collidelistall(blocos_especiais):
            self.velocidade = self.velocidade_reset/2
        else:
            self.velocidade = self.velocidade_reset

    def desenha(self, tela, hitbox = False, cor = 'red'):
        if hitbox:#desenha hitbox
            pg.draw.rect(tela,cor,self.rect)

        if self.direcao == 'D':#desenha sprites direita
            self.sprite_def = self.sprite[0]
            if self.atacando2:
                self.sprite_def = self.sprite[2]
            if self.atacando1:
                self.sprite_def = self.sprite[1]
        
        elif self.direcao == 'E':#desenha sprites esquerda
            self.sprite_def = pg.transform.flip(self.sprite[0], True, False)
            if self.atacando1:
                self.sprite_def = pg.transform.flip(self.sprite[1], True, False)
            if self.atacando2:
                self.sprite_def = pg.transform.flip(self.sprite[2], True, False)
        
        tela.blit(self.sprite_def, self.rect)

    def retorna_rect(self) -> Tuple[float, float, float, float]:
        return self.posicao + (self.largura, self.altura)
