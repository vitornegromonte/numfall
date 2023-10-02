import pygame as pg
import random

pg.init()
largura_tela = 400
altura_tela = 600
tela = pg.display.set_mode((largura_tela, altura_tela))
valor_inicial = 1

fonte_objetos = pg.font.Font('assets/fonts/pixel-art.ttf', 15)

class Coletavel:
    def __init__(self):
        self.x = random.randint(0, largura_tela - 20)
        self.y = 0
        self.velocidade = 0.07  # Defina uma velocidade constante
        self.operacao = random.choice(["+", "-", "x", "/"])  # Escolha aleatória de operação
        self.operando = random.randint(1, 10)  # Número aleatório pro operando
        self.resposta = self.calcular_resposta()

    def calcular_resposta(self):
        resposta = valor_inicial
        # Determinando a operação
        if self.operacao == "+":
            resposta += self.operando
            
        elif self.operacao == "-":
            resposta -= self.operando
            
        elif self.operacao == "x":
            resposta *= self.operando
            
        elif self.operacao == "/":
            resposta /= self.operando
            
        return resposta

    def mover(self):
        self.y += self.velocidade

    def desenhar_objeto(self):
        objeto_surface = fonte_objetos.render(f"{self.operacao} {self.operando}", True, (255, 255, 255))
        objeto_rect = objeto_surface.get_rect(center=(self.x + 10, self.y + 10))
        tela.blit(objeto_surface, objeto_rect)
