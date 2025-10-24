from settings import *
import pygame

class Level:
    def  __init__(self, map):
        self.display_surface = pygame.display.get_surface()
        self.setup(map)
    
    def setup(self, map):
        pass

    def run(self):
        self.display_surface.fill("black")