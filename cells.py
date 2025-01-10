import random
import math
import pygame
import time


class Cell:
    cells = []
    CELL_AMOUNT = 20

    def __init__(self, width, height, screen, radius, speed, strength):
        self.width = width
        self.height = height
        self.screen = screen
        self.color = (0, 0, 255)

        self.radius = radius
        self.speed = speed
        self.strength = strength

        self.foodEaten = 0
        
        self.currentTime = time.time()
        self.lastMoveTime = time.time()
        self.lastPosition = (0, 0)
        
        self.x, self.y = self.spawn_on_circle()
        self.angle = random.uniform(0, 2 * math.pi)
        self.cells.append(self)

    def is_overlapping(self, x, y):
        for cell in Cell.cells:
            if cell != self and math.sqrt((cell.x - x)**2 + (cell.y - y)**2) < 16:  # 16 = 2 * cell radius
                return True
        return False

    def resolve_overlap(self):
        for cell in Cell.cells:
            if cell != self:
                distance = math.sqrt((self.x - cell.x)**2 + (self.y - cell.y)**2)
                if distance < 16:  # 16 = 2 * cell radius
                    angle = math.atan2(self.y - cell.y, self.x - cell.x)
                    push_factor_self = self.strength / (self.strength + cell.strength)
                    push_factor_other = cell.strength / (self.strength + cell.strength)
                    
                    self.x += math.cos(angle) * (16 - distance) * push_factor_other
                    self.y += math.sin(angle) * (16 - distance) * push_factor_other
                    
                    cell.x -= math.cos(angle) * (16 - distance) * push_factor_self
                    cell.y -= math.sin(angle) * (16 - distance) * push_factor_self

    def spawn_on_circle(self):
        while True:
            angle = random.uniform(0, 2 * math.pi)
            x = self.width // 2 + (self.height // 2 - 50) * math.cos(angle)
            y = self.height // 2 + (self.height // 2 - 50) * math.sin(angle)
            if not self.is_overlapping(x, y):
                return x, y

    def move_randomly(self):      
        if time.time() - self.currentTime > 1:
            self.currentTime = time.time()
            self.angle = random.uniform(0, 2 * math.pi)

        new_x = self.x + self.speed * math.cos(self.angle)
        new_y = self.y + self.speed * math.sin(self.angle)

        if not self.is_overlapping(new_x, new_y):
            self.x, self.y = new_x, new_y
        else:
            self.angle = random.uniform(0, 2 * math.pi)  # Adjust angle if stuck

    def move_to_closest_food(self, foods):
        closest_food = None
        closest_distance = float('inf')
        for food in foods:
            distance = math.sqrt((food[0] - self.x)**2 + (food[1] - self.y)**2)
            if distance < closest_distance:
                closest_distance = distance
                closest_food = food

        # Check if cell is stuck
        if (self.x, self.y) == self.lastPosition and time.time() - self.lastMoveTime > 0.1:
            self.lastMoveTime = time.time()
            closest_food = random.choice(foods) if foods else None

        self.lastPosition = (self.x, self.y)

        if closest_distance > self.radius:
            self.color = (255, 0, 0)
            self.move_randomly()
            return

        self.color = (0, 0, 255)

        if closest_food:
            dx = closest_food[0] - self.x
            dy = closest_food[1] - self.y
            distance = math.sqrt(dx**2 + dy**2)
            if distance > 8:
                new_x = self.x + (dx / distance) * self.speed
                new_y = self.y + (dy / distance) * self.speed
                if not self.is_overlapping(new_x, new_y):
                    self.x, self.y = new_x, new_y
                else:
                    self.angle = random.uniform(0, 2 * math.pi)  # Adjust angle if stuck
            else:
                self.foodEaten += 1
                foods.remove(closest_food)  # Only remove if the cell reaches the food

        self.resolve_overlap()  # Ensure cells adjust if too close to others

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), 8)
