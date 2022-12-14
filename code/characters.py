from config_jogo import ConfigJogo
from players import AcoesPersonagem
from sprites import *
from ataques import *

#posicao de inicio, direcao, cor hitbox
posicao1=[(50, ConfigJogo.ALTURA_TELA//2), 'D']
posicao2=[(ConfigJogo.LARGURA_TELA - ConfigJogo.LARGURA_SPRITE - 20, ConfigJogo.ALTURA_TELA//2), 'E']

#stats = [velocidade, vida, dano]
stats_isolde = [1.2, 110, 8, ('fisico', 'cura')]
stats_pitbull = [0.8, 140, 9, ('fisico', 'boost_speed')]#dano 9
stats_lacertus = [1, 100, 10, ('distancia', 'poison')]
stats_draco = [1.4, 90, 7, ('distancia', 'minion')]

fisico1= AtaqueFisico()
distancia1 = AtaqueDistancia()
cura1 = AtaqueCura()
minion1 = AtaqueMinions()
speed1 = AtaqueSpeed()
poison1 = AtaquePoison()

fisico2 = AtaqueFisico()
distancia2 = AtaqueDistancia()
cura2= AtaqueCura()
minion2 = AtaqueMinions()
speed2 = AtaqueSpeed()
poison2 = AtaquePoison()

#p1 (self, posicao, stats, sprite)
Isolde_1 = AcoesPersonagem(posicao1, stats_isolde, sprites_isolde, fisico1, cura1)
Pitbull_1 = AcoesPersonagem(posicao1, stats_pitbull, sprites_pitbull, fisico1, speed1)
Lacertus_1 = AcoesPersonagem(posicao1, stats_lacertus, sprites_lacertus, distancia1, poison1)
Draco_1 = AcoesPersonagem(posicao1, stats_draco, sprites_draco, distancia1, minion1)
#p2 (self, posicao, stats, sprite)
Isolde_2 = AcoesPersonagem(posicao2, stats_isolde, sprites_isolde, fisico2, cura2)
Pitbull_2 = AcoesPersonagem(posicao2, stats_pitbull, sprites_pitbull, fisico2, speed2)
Lacertus_2 = AcoesPersonagem(posicao2, stats_lacertus, sprites_lacertus, distancia2, poison2)
Draco_2 = AcoesPersonagem(posicao2, stats_draco, sprites_draco, distancia2, minion2)

Lista_p1 = [Isolde_1, Pitbull_1, Lacertus_1, Draco_1]
Lista_p2 = [Isolde_2, Pitbull_2, Lacertus_2, Draco_2]
