import pygame
from .bloque import Bloque

BLANCO = (255, 255, 255)
ROJO   = (200, 30, 30)

class Muro(Bloque):
    """Dibuja un cubo con un rectángulo interior"""
    def __init__(self, pos, size, borde=2):
        super().__init__(pos, size, BLANCO, borde)

    def draw(self, surface):
        # Rectángulo exterior
        super().draw(surface)

        # Rectángulo interior centrado
        inner_w = int(self.w * 0.4)
        inner_h = int(self.h * 0.23)
        inner_x = self.x + (self.w - inner_w)//2
        inner_y = self.y + (self.h - inner_h)//2
        pygame.draw.rect(surface, ROJO,
                         (inner_x, inner_y, inner_w, inner_h))
