from settings import *
from fantas import Sprite
import pygame

class Level:
    def  __init__(self, map):
        self.display_surface = pygame.display.get_surface()

        #gruplar
        self.all_sprites = pygame.sprite.Group()

        self.setup(map)
    
    def setup(self, map):
        for x,y,z in map.get_layer_by_name("example_layer").tiles():
            Sprite((x*tileSize * tileScale, y * tileSize * tileScale), z, self.all_sprites)

    def run(self):
        self.display_surface.fill("black")
        self.all_sprites.draw(self.display_surface)