import pygame as pg
from config_jogo import img, ConfigJogo

class Bricks:
    def __init__(self, pos):
        self.imagem = ConfigJogo.imagem_bricks
        self.rect = self.imagem.get_rect(topleft = pos)

    def desenha(self, tela):
        tela.blit(self.imagem, self.rect)

    def retorna_rect(self):
        return self.rect

class Agua:
    def __init__(self, pos):
        self.imagem = ConfigJogo.imagem_agua
        self.rect = self.imagem.get_rect(topleft = pos)

    def desenha(self, tela):
        tela.blit(self.imagem, self.rect)

    def retorna_rect(self):
        return self.rect

class Cooblestone:
    def __init__(self, pos):
        self.imagem = ConfigJogo.imagem_cooblestone
        self.rect = self.imagem.get_rect(topleft = pos)

    def desenha(self, tela):
        tela.blit(self.imagem, self.rect)

    def retorna_rect(self):
        return self.rect

class Stone:
    def __init__(self, pos):
        self.imagem = ConfigJogo.imagem_stone
        self.rect = self.imagem.get_rect(topleft = pos)

    def desenha(self, tela):
        tela.blit(self.imagem, self.rect)

    def retorna_rect(self):
        return self.rect
