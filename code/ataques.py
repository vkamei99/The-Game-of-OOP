import pygame as pg
from time import time
from config_jogo import ConfigJogo, debug
import math
from tile import Stone

class AtaqueFisico():
    def __init__(self):
        self.tempo_cooldown = 0.5
        self.tempo_ataque = 0
        self.tempo_atual = 0
        
        self.atk_rect_d = 0
        self.atk_rect_e = 0

        self.largura = 60
        self.altura = 40

        self.levou_dano = False
        self.stone = []
        
    def atacar(self, atacante, inimigo):
        atacante.atacando1 = True
        self.tempo_ataque = time()

        self.levou_dano = False
    
    def cooldown(self, atacante):
        self.tempo_atual = time()
        if atacante.atacando1:
            if self.tempo_atual - self.tempo_ataque >= self.tempo_cooldown:
                atacante.atacando1 = False
    
    def atualiza_ataque(self, atacante, inimigo, mapa):
        self.rect = atacante.rect
        if atacante.atacando1 and not self.levou_dano:
            if atacante.direcao == 'D':
                self.atk_rect_d = pg.rect.Rect(atacante.rect.right, atacante.rect.y+5, self.largura,self.altura)
                if self.atk_rect_d.colliderect(inimigo.rect):
                    inimigo.vida -= atacante.dano
                    self.levou_dano = True

                for tipo_bloco_index, tipo_bloco in enumerate(mapa):
                    for bloco_index, bloco in enumerate(tipo_bloco):
                        if tipo_bloco_index == 3:
                            if self.atk_rect_d.colliderect(mapa[tipo_bloco_index][bloco_index].retorna_rect()):
                                mapa[2].append(Stone((mapa[tipo_bloco_index][bloco_index].retorna_rect().x ,mapa[tipo_bloco_index][bloco_index].retorna_rect().y)))                                
                                mapa[tipo_bloco_index].remove(mapa[tipo_bloco_index][bloco_index])
                                self.levou_dano = True
                        
                    
            if atacante.direcao == 'E':
                self.atk_rect_e = pg.rect.Rect(atacante.rect.left-self.largura, atacante.rect.y+5, self.largura,self.altura)
                if self.atk_rect_e.colliderect(inimigo.rect):
                    inimigo.vida -= atacante.dano
                    self.levou_dano = True
               
                for tipo_bloco_index, tipo_bloco in enumerate(mapa):
                    for bloco_index, bloco in enumerate(tipo_bloco):
                        if tipo_bloco_index == 3:
                            if self.atk_rect_e.colliderect(mapa[tipo_bloco_index][bloco_index].retorna_rect()):
                                mapa[2].append(Stone((mapa[tipo_bloco_index][bloco_index].retorna_rect().x ,mapa[tipo_bloco_index][bloco_index].retorna_rect().y)))                                
                                mapa[tipo_bloco_index].remove(mapa[tipo_bloco_index][bloco_index])
                                self.levou_dano = True

    def desenha(self, tela, atacante, hitbox = False, cor = 'green'):
        if hitbox: #desenha hitbox
            if atacante.atacando1:
                if atacante.direcao == 'D':
                    pg.draw.rect(tela, cor, self.atk_rect_d)
                if atacante.direcao == 'E':
                    pg.draw.rect(tela,cor, self.atk_rect_e)
    
    def retorna_cooldown(self):
        tempo = (self.tempo_atual - self.tempo_ataque)
        if tempo >= self.tempo_cooldown:
            tempo=self.tempo_cooldown
        return tempo

class AtaqueDistancia():
    def __init__(self):
        self.tempo_cooldown = 0.5
        self.tempo_ataque = 0
        self.tempo_atual = 0
        self.levou_dano = False

        self.atk_projetil_d = 0
        self.atk_projetil_e = 0
        
        self.largura = 30
        self.altura = 20

        self.velocidade = 17

        self.pos_projetil = (0,0)

    def atacar(self, atacante, inimigo):
        atacante.atacando1 = True
        self.levou_dano = False
        self.tempo_ataque = time()

        self.pos_projetil = (atacante.rect.right, atacante.rect.y+18)
        self.direcao = atacante.direcao

    def cooldown(self, atacante):
        self.tempo_atual = time()
        if self.tempo_atual - self.tempo_ataque >= self.tempo_cooldown:
            atacante.atacando1 = False
    
    def atualiza_ataque(self, atacante, inimigo, mapa):
        self.rect = pg.rect.Rect(ConfigJogo.LARGURA_TELA,ConfigJogo.ALTURA_SPRITE,0,0)
        self.largura = atacante.sprite[5].get_width()
        self.altura = atacante.sprite[5].get_height()
        #atualiza posicao
        if atacante.atacando1 and not self.levou_dano:
            x = self.pos_projetil[0]
            y = self.pos_projetil[1]

            if self.direcao == 'D':
                novo_x =  x + self.velocidade

            if self.direcao == 'E':
                novo_x =  x - self.velocidade
                
            self.pos_projetil = (novo_x, y)
            self.rect = pg.rect.Rect(x,y,self.largura,self.altura)
            
        if self.rect.colliderect(inimigo.rect):
            inimigo.vida -= atacante.dano
            self.levou_dano = True

        for tipo_bloco_index, tipo_bloco in enumerate(mapa):
                    for bloco_index, bloco in enumerate(tipo_bloco):
                        if tipo_bloco_index == 3:
                            if self.rect.colliderect(mapa[tipo_bloco_index][bloco_index].retorna_rect()):
                                mapa[2].append(Stone((mapa[tipo_bloco_index][bloco_index].retorna_rect().x ,mapa[tipo_bloco_index][bloco_index].retorna_rect().y)))                                
                                mapa[tipo_bloco_index].remove(mapa[tipo_bloco_index][bloco_index])
                                self.levou_dano = True

    def desenha(self, tela, atacante, hitbox = False, cor = 'green'):
        if atacante.atacando1:
            sprite = atacante.sprite[5]
            if hitbox:
                pg.draw.rect(tela,cor,self.rect)
            if atacante.direcao == 'D':
                sprite = atacante.sprite[5]
            if atacante.direcao == 'E':
                sprite = pg.transform.flip(sprite, True, False)
            tela.blit(sprite, self.rect)

    def retorna_cooldown(self):
        tempo = (self.tempo_atual - self.tempo_ataque)
        if tempo >= self.tempo_cooldown:
            tempo=self.tempo_cooldown
        return tempo

class AtaqueCura():
    def __init__(self):
        self.tempo_cooldown = 5
        self.tempo_ataque = 0
        self.tempo_atual = 0
        self.contador_ataques = 0
        self.raio = 45
            
    def atacar(self, atacante, inimigo):
        atacante.atacando2 = True
        self.tempo_ataque = time()

        self.dano_reset = inimigo.dano
        self.contador_ataques += 1
        
    def cooldown(self, atacante):
        self.tempo_atual = time()
        if atacante.atacando2:
            if self.tempo_atual - self.tempo_ataque >= self.tempo_cooldown:
                atacante.atacando2 = False

    def atualiza_ataque(self, atacante, inimigo, mapa, quebra_bloco = False):
        if atacante.atacando2:
            atacante.vida += 0.01
            inimigo.dano = 0
            self.raio -= 0.15
            if self.raio < 0:
                self.raio = 45
        else:
            if self.contador_ataques >= 1:
                inimigo.dano = self.dano_reset
    
    def desenha(self, tela, atacante, hitbox = False, cor = 'green'):
        if atacante.atacando2:
            pg.draw.circle(tela, 'green', (atacante.rect.center), self.raio,3)
            pg.draw.circle(tela, 'green', (atacante.rect.center), 50,3)
            
    def retorna_cooldown(self):
        tempo = (self.tempo_atual - self.tempo_ataque)
        if tempo >= self.tempo_cooldown:
            tempo=self.tempo_cooldown
        return tempo

class AtaqueMinions():
    def __init__(self):
        self.tempo_cooldown = 5
        self.tempo_ataque = 0
        self.tempo_atual = 0
        
        self.levou_dano = False

        self.velocidade = 4

        self.largura = 30
        self.altura = 10
        
    def atacar(self, atacante, inimigo):
        atacante.atacando2 = True
        self.levou_dano = False
        self.tempo_ataque = time()

        self.pos_minions_x, self.pos_minions_y = atacante.rect.center
        self.inimigo = inimigo            
    
    def cooldown(self, atacante):
        self.tempo_atual = time()
        if atacante.atacando2:
            self.alvo_x, self.alvo_y = self.inimigo.rect.center
            if self.tempo_atual - self.tempo_ataque >= self.tempo_cooldown:
                atacante.atacando2 = False
    
    def atualiza_ataque(self, atacante, inimigo, mapa, quebra_bloco = False):
        self.rect = pg.rect.Rect(ConfigJogo.LARGURA_TELA,ConfigJogo.ALTURA_TELA,0,0)
        #projetil que segue
        if atacante.atacando2 and not self.levou_dano:
            dist = math.sqrt((self.alvo_x - self.pos_minions_x) ** 2 +(self.alvo_y - self.pos_minions_y) ** 2)

            if dist > 1:
                velocidade_x = self.alvo_x - self.pos_minions_x
                velocidade_y = self.alvo_y - self.pos_minions_y

                norma = math.sqrt(velocidade_x ** 2 + velocidade_y ** 2)
                velocidade_x /= norma
                velocidade_y /= norma

                velocidade_x *= self.velocidade
                velocidade_y *= self.velocidade
            else:
                velocidade_x = 0
                velocidade_y = 0

            self.pos_minions_x += velocidade_x
            self.pos_minions_y += velocidade_y

            self.rect = pg.rect.Rect(self.pos_minions_x, self.pos_minions_y, self.largura, self.altura)

        if self.rect.colliderect(inimigo.rect):
            inimigo.vida -= atacante.dano * 2
            self.levou_dano = True

        if quebra_bloco:
            for tipo_bloco_index, tipo_bloco in enumerate(mapa):
                for bloco_index, bloco in enumerate(tipo_bloco):
                    if tipo_bloco_index == 3:
                        if self.rect.colliderect(mapa[tipo_bloco_index][bloco_index].retorna_rect()):
                            print('hit')
                            mapa[tipo_bloco_index][bloco_index] = mapa[2][bloco_index]
                            self.levou_dano = True
                
    def desenha(self, tela, atacante, hitbox = False, cor = 'black'):
        if atacante.atacando2:
            if hitbox: #desenha hitbox
                pg.draw.rect(tela, cor, self.rect)
            tela.blit(atacante.sprite[5], self.rect)

    def retorna_cooldown(self):
        tempo = (self.tempo_atual - self.tempo_ataque)
        if tempo >= self.tempo_cooldown:
            tempo=self.tempo_cooldown
        return tempo

class AtaqueSpeed():
    def __init__(self):
        self.tempo_cooldown = 10
        self.tempo_ataque = 0
        self.tempo_atual = 0

        self.contador_ataques = 0
        self.levou_dano = False
        
        self.atk_rect_d = 0
        self.atk_rect_e = 0

        self.largura = 60
        self.altura = 40

    def atacar(self, atacante, inimigo):
        atacante.atacando2 = True
        self.tempo_ataque = time()

        self.velocidade_reset = atacante.velocidade_reset
        self.velocidade_boost = atacante.velocidade_reset + 0.6*4
        self.levou_dano = False
        self.contador_ataques += 1
        if atacante.atacando2:
            atacante.velocidade_reset = self.velocidade_boost

    def cooldown(self, atacante):
        self.tempo_atual = time()
        if atacante.atacando2:
            if self.tempo_atual - self.tempo_ataque >= self.tempo_cooldown:
                atacante.atacando2 = False
            
    def atualiza_ataque(self, atacante, inimigo, mapa, quebra_bloco = False):
        if not atacante.atacando2 and (self.contador_ataques >=1):
            atacante.velocidade_reset = self.velocidade_reset
        
        if atacante.atacando2:
            if atacante.atacando1:
                if atacante.direcao == 'D':
                    self.atk_rect_d = pg.rect.Rect(atacante.rect.right, atacante.rect.y+5, self.largura,self.altura)
                    if self.atk_rect_d.colliderect(inimigo.rect):
                        inimigo.pararX()
                        inimigo.pararY()
                        
                if atacante.direcao == 'E':
                    self.atk_rect_e = pg.rect.Rect(atacante.rect.left-self.largura, atacante.rect.y+5, self.largura,self.altura)
                    if self.atk_rect_e.colliderect(inimigo.rect):
                        inimigo.pararX()
                        inimigo.pararY()
                
    def desenha(self, tela, atacante, hitbox = False, cor = 'green'):
        if atacante.atacando2:
            pass
                       
    def retorna_cooldown(self):
        tempo = (self.tempo_atual - self.tempo_ataque)
        if tempo >= self.tempo_cooldown:
            tempo=self.tempo_cooldown
        return tempo

class AtaquePoison():
    def __init__(self):
        self.tempo_cooldown = 10
        self.tempo_ataque = 0
        self.tempo_atual = 0
        self.raio = 100
        self.contador_ataques = 0
                
    def atacar(self, atacante, inimigo):
        atacante.atacando2 = True
        self.tempo_ataque = time()
        self.contador_ataques += 1
        self.mouse_position = pg.mouse.get_pos()
        self.velocidade_reset = inimigo.velocidade_reset
        self.velocidade_slow = inimigo.velocidade_reset / 2
    
    def cooldown(self, atacante):
        self.tempo_atual = time()
        if atacante.atacando2:
            if self.tempo_atual - self.tempo_ataque >= self.tempo_cooldown:
                atacante.atacando2 = False
    
    def atualiza_ataque(self, atacante, inimigo, mapa, quebra_bloco = False):
        if atacante.atacando2:
            dist = math.sqrt((self.mouse_position[0] - inimigo.rect.x)**2 + (self.mouse_position[1] - inimigo.rect.y)**2)
            if dist <= self.raio:
                inimigo.vida -= 0.05
                inimigo.velocidade_reset = self.velocidade_slow
            if dist > self.raio:
                inimigo.velocidade_reset = self.velocidade_reset
            
    def desenha(self, tela, atacante, hitbox = False, cor = 'green'):
        if atacante.atacando2:
            if hitbox:
                pg.draw.circle(tela, cor, self.mouse_position, self.raio)
            tela.blit(atacante.sprite[6], (self.mouse_position[0]-100, self.mouse_position[1]-100))
    
    def retorna_cooldown(self):
        tempo = (self.tempo_atual - self.tempo_ataque)
        if tempo >= self.tempo_cooldown:
            tempo=self.tempo_cooldown
        return tempo

class AtaqueStum():
    def __init__(self):
        self.tempo_cooldown = 0.5
        self.tempo_ataque = 0
        self.tempo_atual = 0
        self.levou_dano = False
        
    def atacar(self, atacante, inimigo):
        atacante.atacando2 = True
        self.tempo_ataque = time()
        self.levou_dano = False
    
    def cooldown(self, atacante):
        self.tempo_atual = time()
        if atacante.atacando2:
            if self.tempo_atual - self.tempo_ataque >= self.tempo_cooldown:
                atacante.atacando2 = False
    
    def atualiza_ataque(self, atacante, inimigo, mapa):
        if atacante.atacando2:
            inimigo.pararX()
            inimigo.pararY()

    def desenha(self, tela, atacante, hitbox = False, cor = 'green'):
        pass
    
    def retorna_cooldown(self):
        tempo = (self.tempo_atual - self.tempo_ataque)
        if tempo >= self.tempo_cooldown:
            tempo=self.tempo_cooldown
        return tempo