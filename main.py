# main.py
import pygame
import time
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
font = pygame.font.Font(None, 28)


def reset(food, dayTime):
    food.generate()
    for cell in Cell.cells:
        cell.x, cell.y = cell.spawn_on_circle()
    

# Main loop
def main():
    running = True

    food = Food(WIDTH, HEIGHT, screen)

    Cell.cells.clear()
    for _ in range(Cell.CELL_AMOUNT):
        Cell(WIDTH, HEIGHT, screen, 100, 1)

    dayTime = 10
    currentTime = time.time()
    while running:
        screen.fill(BLACK)

        pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), HEIGHT // 2 - 50, 1)

        food.draw()

        for cell in Cell.cells:
            cell.move_to_closest_food(food.foods)
            cell.draw()

        clock.tick(FPS)

        fps = int(clock.get_fps())
        fps_text = font.render(f"FPS: {fps}", True, WHITE)
        screen.blit(fps_text, (10, 10))

        if time.time() - currentTime > dayTime:
            reset(food, dayTime)
            currentTime = time.time()
            

        time_text = font.render(f"Time: {dayTime - int(time.time() - currentTime)}", True, WHITE)
        screen.blit(time_text, (WIDTH - time_text.get_width() - 10, 10))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    reset(food, dayTime)
                    currentTime = time.time()
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()