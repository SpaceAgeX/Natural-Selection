# food.py
import random
import pygame

class Food:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen
        self.food_amount = 250
        self.speed = 5
        self.foods = []
        self.generation = 0 
        self.generate()
        

    def generate(self):
        
        

        

        self.foods.clear()
        for _ in range(self.food_amount):
            while True:
                x = random.randint(self.width // 2 - self.height // 2 + 50, self.width // 2 + self.height // 2 - 70)
                y = random.randint(self.height // 2 - self.height // 2 + 50, self.height // 2 + self.height // 2 - 70)
                if (x - self.width // 2)**2 + (y - self.height // 2)**2 <= (self.height // 2 - 70)**2:
                    self.foods.append((x, y))
                    break
        self.generation += 1
    

    def draw(self):
        for food in self.foods:
            pygame.draw.circle(self.screen, (0, 255, 0), food, 2)
