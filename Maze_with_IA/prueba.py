import pygame
import muros          # gracias al __init__, esto ya carga todas las clases
from muros.muro import Muro   # o importa solo las que necesites

# --- CONSTANTES ---
SCREEM_WIDTH  = 800
SCREEM_HEIGHT = 600
GRID_SIZE     = 40
FPS           = 60

def draw_grid(screen, grid_size):
    screen.fill((0, 0, 0))  # Rellena la pantalla
    muro.draw(screen)

# --- INICIALIZACIÓN ---
pygame.init()
screen = pygame.display.set_mode((SCREEM_WIDTH, SCREEM_HEIGHT), pygame.RESIZABLE)
clock  = pygame.time.Clock()

# crea un muro de prueba
muro = Muro(pos=(100, 250), size=(100, 100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    draw_grid(screen, GRID_SIZE)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
