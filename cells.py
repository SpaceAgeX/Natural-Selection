import random
import math
import pygame
import time




class Cell:
    cells = []
    CELL_AMOUNT = 20

    def __init__(self, width, height, screen, radius, speed):

        self.width = width
        self.height = height
        self.screen = screen
        self.color = (0, 0, 255)

        self.radius = radius
        self.speed = speed

        self.foodEaten = 0
         
        self.currentTime = time.time()
        
        self.x, self.y = self.spawn_on_circle()
        self.angle = random.uniform(0, 2 * math.pi)
        self.cells.append(self)
        

    def spawn_on_circle(self):
        angle = random.uniform(0, 2 * math.pi)
        x = self.width // 2 + (self.height // 2 - 50) * math.cos(angle)
        y = self.height // 2 + (self.height // 2 - 50) * math.sin(angle)
        return x, y
    
    def move_randomly(self):      
        
        if time.time() - self.currentTime  >1:
            #reset the time
            self.currentTime = time.time()
            self.angle = random.uniform(0, 2 * math.pi)
        
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def move_to_closest_food(self, foods):
        closest_food = None
        closest_distance = float('inf')
        for food in foods:
            distance = math.sqrt((food[0] - self.x)**2 + (food[1] - self.y)**2)
            if distance < closest_distance:
                closest_distance = distance
                closest_food = food
        if closest_distance > self.radius:
            self.color = (255, 0, 0)
            self.move_randomly()
            return

        self.color = (0, 0, 255)

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
                self.foodEaten += 1
                foods.remove(closest_food)

    def draw(self):
        
 
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), 8)
        