import pygame

BLANCO = (255, 255, 255)
GRIS   = (200, 200, 200)
NEGRO  = (0, 0, 0)

class Boton:
    def __init__(self, pos, size, color=GRIS, borde=3):
        self.base_pos = pygame.Vector2(pos)
        self.base_size = pygame.Vector2(size)
        self.color = color
        self.borde = borde

        self.current_size = self.base_size.copy()
        self.state = "normal"
        self.anim_time = 150  # ms
        self.start_time = 0

        self.rect = pygame.Rect(self.base_pos, self.base_size)

    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()
        hovering = self.rect.collidepoint(mouse_pos)

        if hovering:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if self.state != "pressed":
                self.state = "hover"
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if self.state != "pressed":
                self.state = "normal"

        if event.type == pygame.MOUSEBUTTONDOWN and hovering:
            self.state = "pressed"
            self.start_time = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        target_size = self.base_size

        if self.state == "hover":
            target_size = self.base_size * 1.1
        elif self.state == "pressed":
            elapsed = now - self.start_time
            if elapsed < self.anim_time:
                # comprime al 90 %
                factor = 1 - 0.1 * (elapsed / self.anim_time)
                target_size = self.base_size * factor
            else:
                # luego regresa a hover
                self.state = "hover"
                self.start_time = now

        # Interpolación suave
        self.current_size += (target_size - self.current_size) * 0.2

        # Actualiza posición centrada
        self.rect.width, self.rect.height = self.current_size
        self.rect.center = self.base_pos + self.base_size / 2

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=8)
        pygame.draw.rect(surface, NEGRO, self.rect, width=self.borde, border_radius=8)
