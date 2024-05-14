# config_jogo.py

 Este arquivo de configuração estabelece parâmetros essenciais e utilitários usados ao longo do jogo. Ele inicializa configurações do jogo como dimensões da tela, tamanhos de fonte e constantes de gameplay. Abaixo estão os componentes chave do arquivo:

##    Inicialização do Pygame:
O arquivo começa importando e inicializando o Pygame, o que é necessário para qualquer desenvolvimento de jogo usando esta biblioteca.

###    Classe de Configuração (ConfigJogo):
Dimensões da Tela: Define constantes para a largura (LARGURA_TELA) e altura (ALTURA_TELA) da tela do jogo.
Tamanho da Fonte: Estabelece um tamanho padrão de fonte (FONT_SIZE) usado dentro do jogo.
Título da Janela do Jogo: Especifica um título para a janela do jogo.
Posições Iniciais dos Jogadores: Indica os pontos de partida para os jogadores na tela do jogo.
Temporizações do Jogo: Inclui configurações como a duração de cada rodada do jogo e atualizações para animações de sprites.
Mapa de Tiles: Define o layout do ambiente do jogo através de um array multidimensional onde cada número representa um tipo diferente de tile ou objeto.

###    Funções Utilitárias:
Carregamento de Imagens: Funções para carregar imagens de caminhos especificados, úteis para renderizar sprites e elementos de fundo.
Escala de Imagens: Permite a escala de imagens para se ajustarem às dimensões da tela ou requisitos de design.
Exibição de Debug: Uma utilidade para renderizar informações de debug na tela, útil durante o desenvolvimento para rastreamento de parâmetros em tempo real.

###    Recursos de Mídia:
Manipulação de Som e Música: Fornece métodos para carregar e controlar a reprodução de áudio, como música de fundo ou efeitos sonoros.

## Funcionalidade Detalhada

A classe ConfigJogo serve como a espinha dorsal para definir e ajustar as mecânicas de gameplay.
Ela inclui métodos para lidar com ativos do jogo (como imagens e sons), que são cruciais para manter uma experiência de jogo suave e dinâmica.
O mapa de tiles dentro da classe delineia a estrutura primária do ambiente do jogo, essencial tanto para renderizar o mundo do jogo quanto para implementar a detecção de colisões.