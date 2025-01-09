import random
import math
import pygame

class Cell:
    cells = []
    amount = 10
    def __init__(self, WIDTH, HEIGHT, radius, screen):

        self.width = WIDTH
        self.height = HEIGHT

        self.screen = screen
        self.radius = radius
        self.vis = 100
        self.x, self.y = self.spawn_on_circle()
        Cell.cells.append(self)

    def spawn_on_circle(self):
        angle = random.uniform(0, 2 * math.pi)
        x = self.width // 2 + (self.height // 2 - 25) * math.cos(angle)
        y = self.height // 2 + (self.height // 2 - 25) * math.sin(angle)  
        return x, y

    def find_food_within_radius(self, foods):
        nearby_food = []
        for food in foods:
            distance = math.sqrt((food[0] - self.x)**2 + (food[1] - self.y)**2)
            if distance <= self.vis:
                nearby_food.append(food)
        return nearby_food

    def draw(self):
        pygame.draw.circle(self.screen, (0, 0, 255), (int(self.x), int(self.y)), 8)
