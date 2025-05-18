import pygame

SCREEM_WIDTH = 800
SCREEM_HEIGHT = 600

def draw_grid(screen, grid_size):
    for x in range(0, SCREEM_WIDTH, grid_size):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, SCREEM_HEIGHT))
    for y in range(0, SCREEM_HEIGHT, grid_size):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (SCREEM_WIDTH, y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEM_WIDTH, SCREEM_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Grid Example")
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black
        draw_grid(screen, 20)  # Draw the grid with a size of 20 pixels
        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit the frame rate to 60 FPS
    pygame.quit()

if __name__ == "__main__":
    main()