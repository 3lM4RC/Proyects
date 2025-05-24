import pygame
from Classes.muro import Muro
from Classes.camino import Camino
from Classes.boton import Boton   # Ajusta el path si lo tienes en otro lugar

# --- CONSTANTES ---
SCREEM_WIDTH  = 800
SCREEM_HEIGHT = 600
GRID_SIZE     = 40
FPS           = 60

# --- INICIALIZACIÓN ---
pygame.init()
screen = pygame.display.set_mode((SCREEM_WIDTH, SCREEM_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Visualización de objetos")
clock  = pygame.time.Clock()

# --- OBJETOS ---
muro = Muro(pos=(100, 250), size=(100, 100))
camino = Camino(pos=(250, 250), size=(100, 100))
boton = Boton(pos=(450, 250), size=(150, 60))

def draw_grid(screen, grid_size):
    for x in range(0, SCREEM_WIDTH, grid_size):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, SCREEM_HEIGHT))
    for y in range(0, SCREEM_HEIGHT, grid_size):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (SCREEM_WIDTH, y))

# --- BUCLE PRINCIPAL ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        boton.handle_event(event)

    # Lógica
    boton.update()

    # Dibujo
    screen.fill((0, 0, 0))
    draw_grid(screen, GRID_SIZE)
    muro.draw(screen)
    camino.draw(screen)
    boton.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
