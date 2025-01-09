# main.py
import pygame
from food import Food
from cells import Cell

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Natural Selection Simulation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Font for displaying FPS
font = pygame.font.Font(None, 24)

# Main loop
def main():
    running = True
    food = Food(WIDTH, HEIGHT, screen)
    for x in range(Cell.amount):
        Cell(WIDTH, HEIGHT, 10, screen)

    while running:
        screen.fill(BLACK)

        pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), HEIGHT // 2 - 50, 1)

        food.draw()
        
        for x in Cell.cells:
            x.draw()
            #x.find_food_within_radius(food.foods)

        clock.tick(FPS)

        fps = int(clock.get_fps())
        fps_text = font.render(f"FPS: {fps}", True, WHITE)
        screen.blit(fps_text, (10, 10))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    food.generate()
                    for x in Cell.cells:
                        x.x, x.y = x.spawn_on_circle()
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()