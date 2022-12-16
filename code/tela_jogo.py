import pygame as pg
import sys
from config_jogo import ConfigJogo, debug
from characters import Lista_p1, Lista_p2
from estado_jogo import Estadojogo
from tile import Bricks, Stone, Agua, Cooblestone

class TelaJogo:
    def __init__(self, tela):
        self.tela = tela
        
        self.rodando = True
        self.encerrado = False
        
        self.p1 = Lista_p1[ConfigJogo.PERSONAGEM_P1]
        self.rect_1 = pg.rect.Rect(self.p1.retorna_rect())

        self.p2 = Lista_p2[ConfigJogo.PERSONAGEM_P2]
        self.rect_2 = pg.rect.Rect(self.p2.retorna_rect())
        
        self.estado = Estadojogo(self.p1, self.p2)
        self.clock = pg.time.Clock()

        self.bricks = []
        self.stone = []
        self.cooblestone = []
        self.agua = []
        self.cria_mapa()

    def rodar(self):
        while not self.encerrado:
            self.clock.tick(120)
            self.tratamento_de_eventos()
            self.atualiza_estado()
            self.desenha()

    def tratamento_de_eventos(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                print("Encerrando o programa.")
                sys.exit()
            if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                print("Encerrando o programa.")
                sys.exit()

        #Player 1
            #movimentação
            if pg.key.get_pressed()[pg.K_w]:
                self.p1.mover_pra_cima()
            elif pg.key.get_pressed()[pg.K_s]:
                self.p1.mover_pra_baixo()
            else:
                self.p1.pararY()
            if pg.key.get_pressed()[pg.K_a]:
                self.p1.direcao = 'E'
                self.p1.mover_pra_esquerda()
            elif pg.key.get_pressed()[pg.K_d]:
                self.p1.direcao = 'D'
                self.p1.mover_pra_direita()
            else:
                self.p1.pararX()                 
            #ataque1
            if pg.key.get_pressed()[pg.K_e] and not self.p1.atacando1:
                self.p1.ataque1.atacar(self.p1, self.p2) 
            #ataque2
            if pg.key.get_pressed()[pg.K_q] and not self.p1.atacando2:
                self.p1.ataque2.atacar(self.p1, self.p2)
      
        #Player 2
            #movimentação
            if pg.key.get_pressed()[pg.K_i]:
                self.p2.mover_pra_cima()
            elif pg.key.get_pressed()[pg.K_k]:
                self.p2.mover_pra_baixo()
            else:
                self.p2.pararY()
            if pg.key.get_pressed()[pg.K_j]:
                self.p2.direcao = 'E'
                self.p2.mover_pra_esquerda()
            elif pg.key.get_pressed()[pg.K_l]:
                self.p2.direcao = 'D'
                self.p2.mover_pra_direita()
            else:
                self.p2.pararX()
            #ataque1
            if pg.key.get_pressed()[pg.K_o] and not self.p2.atacando1:
                self.p2.ataque1.atacar(self.p2, self.p1)
            #ataque2
            if pg.key.get_pressed()[pg.K_u] and not self.p2.atacando2:
                self.p2.ataque2.atacar(self.p2, self.p1)

    def player_colisao(self, colisao = True):
        if colisao:
            if self.rect_1.colliderect(self.rect_2):
                if self.p1.velocidadeX > 0:
                    self.p1.colisao_player(self.p2.posicao, 'D')
                if self.p1.velocidadeX < 0:
                    self.p1.colisao_player(self.p2.posicao, 'A')
                if self.p1.velocidadeY > 0:
                    self.p1.colisao_player(self.p2.posicao, 'W')
                if self.p1.velocidadeY < 0:
                    self.p1.colisao_player(self.p2.posicao, 'S')
                        
            if self.rect_2.colliderect(self.rect_1):
                if self.p2.velocidadeX > 0:
                    self.p2.colisao_player(self.p1.posicao, 'D')
                if self.p2.velocidadeX < 0:
                    self.p2.colisao_player(self.p1.posicao, 'A')
                if self.p2.velocidadeY > 0:
                    self.p2.colisao_player(self.p1.posicao, 'W')
                if self.p2.velocidadeY < 0:
                    self.p2.colisao_player(self.p1.posicao, 'S')

    def cria_mapa(self):
        for fileira_index, fileira in enumerate(ConfigJogo.TILEMAP):
            for coluna_index, coluna in enumerate(fileira):
                x = coluna_index * ConfigJogo.TAMANHO_TILE
                y = fileira_index * ConfigJogo.TAMANHO_TILE
                if coluna == 0:
                    self.agua.append(Agua((x,y)))
                if coluna == 1:
                    self.bricks.append(Bricks((x,y)))
                if coluna == 2:
                    self.stone.append(Stone((x,y)))
                if coluna == 3:
                    self.cooblestone.append(Cooblestone((x,y)))
        self.mapa = [self.agua, self.bricks, self.stone, self.cooblestone]

    def desenha_mapa(self):
        for tipo_bloco_index, tipo_bloco in enumerate(self.mapa):
            for bloco_index, bloco in enumerate(tipo_bloco):
                self.mapa[tipo_bloco_index][bloco_index].desenha(self.tela)

    def atualiza_estado(self):
        self.p1.atualizar_posicao(self.mapa)
        self.p1.ataque1.cooldown(self.p1)
        self.p1.ataque1.atualiza_ataque(self.p1, self.p2, self.mapa)
        self.p1.ataque2.cooldown(self.p1)
        self.p1.ataque2.atualiza_ataque(self.p1, self.p2, self.mapa)
        self.rect_1 = pg.rect.Rect(self.p1.retorna_rect())

        self.p2.atualizar_posicao(self.mapa)
        self.p2.ataque1.cooldown(self.p2)
        self.p2.ataque1.atualiza_ataque(self.p2, self.p1, self.mapa)
        self.p2.ataque2.cooldown(self.p2)
        self.p2.ataque2.atualiza_ataque(self.p2, self.p1, self.mapa)
        self.rect_2 = pg.rect.Rect(self.p2.retorna_rect())
        
        self.player_colisao(False)

        if self.estado.jogo_terminou():
            self.encerrado = True
            ConfigJogo.TELA = 'vencedor'

    def desenha(self):
        self.desenha_mapa()

        self.p1.ataque1.desenha(self.tela, self.p1, False) #(tela, player, hitbox, cor da hitbox = red)
        self.p1.ataque2.desenha(self.tela, self.p1, False)
        self.p1.desenha(self.tela, False) #(tela, hitbox, cor da hitbox = red)

        self.p2.ataque1.desenha(self.tela, self.p2, False)
        self.p2.ataque2.desenha(self.tela, self.p2, False)
        self.p2.desenha(self.tela, False, 'blue')
    
        self.estado.desenha(self.tela)

        #debug(self.tela, f'{self.p1.velocidade},{self.p1.direction}')

        pg.display.flip()
