from time import time

class Cronometro:
    def __init__(self):
        self.reset()

    def reset(self):
        self.tempo_referencia = time()

    def tempo_passado(self):
        tempo_atual = time()
        return tempo_atual - self.tempo_referencia

    def tempo_atual(self):
        tempo_atual=time()
        return tempo_atual