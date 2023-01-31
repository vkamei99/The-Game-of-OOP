# The Game of OOP

 Criadores: Arthur Christ Marcolan,
            Viktor Kamei Mota,
            Arthur Fiorio da Cunha,

Professor: Filipe Wall Mutz

Matéria: Programação Orientada a Objetos

## Requesitos para rodar o jogo

1) É necessário que você possua o interpretador python baixado em seu computador
2) Você precisa baixar a em seu computador a biblioteca "pygames":
    Abrindo o CMD de seu computador e digitando:
        python -m pip install pygame
3) Além claro de baixar todos os arquivos presentes neste repositório
4) Para rodar o jogo no windows você pode abrir o propmt de comando no diretorio principal baixado (onde contem as pastas "code","imagens"...) e digitar o comando  python code/main.py

## Em que consiste este trabalho

Foi pedido para que nós fizessemos um trabalho no qual, o trabalho consiste em desenvolver um jogo de 2 jogadores no formato de combate em arena 
(e.g., bomberman, dota, etc.) utilizando a linguagem Python, a biblioteca pygame e programação orientada a objetos.

## Contexto histórico do jogo

Durante o período mediavel, a grande nação de Oop ultilizava dos campos férteis de seus feudos para  o plantio, gerando prosperidade como nenhum outro feudo, porém após a morte do Rei de Oop, seus 4 filhos herdeiros, entram em desacordo, dividindo-se em 4 sub-famílias, cada uma delas que tem a desejo de obter a posse dessas terras e criar o seu próprio reino. Assim travando terríveis e fatais batalhas para responder uma sequinte pergunta:
QUEM SERÁ O PRÓXIMO REI DE OOP???

## Comandos para jogar

**Player 1**: terá movimentações com as telcas *W*(cima), *S*(baixo), *A*(esquerda) e *D*(direita). Já as teclas de combate serão E(para ataques simples) e Q(para seus especiais).

**Player 2**: terá movimentações com as telcas *I*(cima), *K*(baixo), *J*(esquerda) e *L*(direita). Já as teclas de combate serão *O*(para ataques simples) e *U*(para seus especiais).

## Observações:

    Versao recomendada do python:
    Python 3.10.2
    
## Vídeo com uma gameplay monstrando cada personagem detalhado

    Video demonstrativo do jogo funcionando:
        https://youtu.be/-krtIwnCi_g

## Link tutorial de instalação de pygame para windows

    https://www.geeksforgeeks.org/how-to-install-pygame-in-windows/

## Requisitos para avaliação
**ATAQUES**:

*Tyron Pitbull:
    O personagem Tyron Pitbull e um dos quatro personagens pedidos para ser feito ele tem ataque fisico e quando usado o seu especial ele recebe um acrescimo de velocidade e seu ataque passa a dar "stun" nos outros personagens

*Draco Oriens:
    O personagem Draco Oriens e o nosso atacante a distância ele lança flechas e em seu especial ele lança uma "flecha minion" que segue o inimigo durante um periodo de tempo

*Lacertus Acertus:
    O ataque com mouse foi adicionado para o lacertus que quando usa seu ataque especial e criada uma poça de veneno que dano ao inimigo que entra nela, ele tambem ataca a distancia

*Isolde:
    Isolde e o personagem que ataca fisicamente seu especial e de ação propria curando ele durante o especial ele e imune a dano

**MAPA**:
    O mapa foi feito com tilemaps adicionando 4 tipos de tiles diferentes;
        o de fundo onde os personagens podem andar livremente,
        a parede onde os personagens não podem andar, 
        a água onde os personagens ficam mais lento,
        a paredes quebraveis que o personagem nao pode andar ate quebrar elas.

**TESTES**:
    No arquivo tela_jogo.py na parte de desenha pode ser ligado e desligado a hitbox dos ataques e dos personagens, tambem tem uma função debug que pode ser usada para imprimir variaveis na tela.

     