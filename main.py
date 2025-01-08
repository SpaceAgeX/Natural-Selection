import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Natural Selection Simulation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Font for displaying FPS
font = pygame.font.Font(None, 24)

class Food:
    FoodAmount = 50
    Foods = []

    def __init__(self):
        Food.generate(self)
        
    def generate(self):
        Food.clear(self)
        for _ in range(Food.FoodAmount):
            while True:
                x = random.randint(WIDTH // 2 - HEIGHT // 2 + 50, WIDTH // 2 + HEIGHT // 2 - 70)
                y = random.randint(HEIGHT // 2 - HEIGHT // 2 + 50, HEIGHT // 2 + HEIGHT // 2 - 70)
                if (x - WIDTH // 2)**2 + (y - HEIGHT // 2)**2 <= (HEIGHT // 2 - 70)**2:
                    self.Foods.append((x, y))
                    break
    def clear(self):
        self.Foods = []

    def draw(self):
        for food in self.Foods:
            pygame.draw.circle(screen, GREEN, food, 5)

# Main loop
def main():
    running = True
    food = Food()

    while running:
        screen.fill(BLACK)

        pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), HEIGHT // 2 - 50, 1)

        food.draw()

        clock.tick(FPS)

        fps = int(clock.get_fps())
        fps_text = font.render(f"FPS: {fps}", True, WHITE)
        screen.blit(fps_text, (10, 10))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    food.generate()
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
