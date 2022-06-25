import pygame, random
pygame.init()

def escreveTela(texto, cor, tamanho):
    fonte = pygame.font.Font("freesansbold.ttf", tamanho)
    frase = fonte.render(texto, True, cor)
    return frase