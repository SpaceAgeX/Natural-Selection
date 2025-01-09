import random
import math
import pygame

class Cell:
    cells = []

    def __init__(self, width, height, screen, radius, speed):
        self.width = width
        self.height = height
        self.screen = screen
        self.radius = radius
        self.speed = speed
        self.x, self.y = self.spawn_on_circle()
        self.cells.append(self)

    def spawn_on_circle(self):
        angle = random.uniform(0, 2 * math.pi)
        x = self.width // 2 + (self.height // 2 - 50) * math.cos(angle)
        y = self.height // 2 + (self.height // 2 - 50) * math.sin(angle)
        return x, y

    def find_food_within_radius(self, foods):
        nearby_food = []
        for food in foods:
            distance = math.sqrt((food[0] - self.x)**2 + (food[1] - self.y)**2)
            if distance <= self.radius:
                nearby_food.append(food)
        return nearby_food

    def move_to_closest_food(self, foods):
        closest_food = None
        closest_distance = float('inf')
        for food in foods:
            distance = math.sqrt((food[0] - self.x)**2 + (food[1] - self.y)**2)
            if distance < closest_distance:
                closest_distance = distance
                closest_food = food

        if closest_food:
            dx = closest_food[0] - self.x
            dy = closest_food[1] - self.y
            distance = math.sqrt(dx**2 + dy**2)
            if distance > 1:
                self.x += (dx / distance) * self.speed
                self.y += (dy / distance) * self.speed
            else:
                self.x = closest_food[0]
                self.y = closest_food[1]
                foods.remove(closest_food)

    def draw(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (int(self.x), int(self.y)), 8)
