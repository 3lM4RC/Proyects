import pygame
from .bloque import Bloque

BLANCO = (255, 255, 255)

class Camino(Bloque):
    """El camino es un cuadrado con borde blanco"""
    def __init__(self, pos, size, borde=2):
        super().__init__(pos, size, BLANCO, borde)

    # Usa el draw de Bloque, no necesitas redefinirlo
