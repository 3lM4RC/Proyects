import pygame

NEGRO  = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO   = (200, 30, 30)

class Muro:
    """Dibuja un cubo con un rectángulo interior"""
    def __init__(self, pos, size, borde=2):
        self.x, self.y = pos
        self.w, self.h = size
        self.borde = borde

    def set_pos(self, pos):
        """Cambia la posición del muro"""
        self.x, self.y = pos

    def set_size(self, size):
        """Cambia el tamaño del muro"""
        self.w, self.h = size

    def draw(self, surface):
        # “Cubo”: realmente un rectángulo exterior
        pygame.draw.rect(surface, BLANCO,
                         (self.x, self.y, self.w, self.h),
                         width=self.borde)

        # Rectángulo interior (centrado, 70 % del tamaño)
        inner_w = int(self.w * 0.4)
        inner_h = int(self.h * 0.23)
        inner_x = self.x + (self.w - inner_w)//2
        inner_y = self.y + (self.h - inner_h)//2
        pygame.draw.rect(surface, ROJO,
                         (inner_x, inner_y, inner_w, inner_h))
