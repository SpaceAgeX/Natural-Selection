# food.py
import random
import pygame

class Cell:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen
        self.target = None
        #spawn somewhere along the circle
        
