import pygame

class Bloque:
    """Clase base para elementos de la cuadrícula"""
    def __init__(self, pos, size, color, borde=2):
        self.x, self.y = pos
        self.w, self.h = size
        self.borde = borde
        self.color = color

    def set_pos(self, pos):
        self.x, self.y = pos

    def set_size(self, size):
        self.w, self.h = size

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,
                         (self.x, self.y, self.w, self.h),
                         width=self.borde)
