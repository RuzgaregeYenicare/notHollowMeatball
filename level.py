from settings import *
from fantas import Sprite
from characther import Player

class Level:
    def  __init__(self, map):
        self.display_surface = pygame.display.get_surface()

        #gruplar
        self.all_sprites = pygame.sprite.Group()

        self.setup(map)
    
    def setup(self, map):
        for x,y,z in map.get_layer_by_name("example_layer").tiles():
            Sprite(scaler(tileScale, x * tileSize, y * tileSize), z, self.all_sprites)

        for obj in map.get_layer_by_name("objects"):
            if obj.name == "Player":
                Player(scaler(tileScale, obj.x, obj.y), self.all_sprites)

    def run(self, dt):
        self.all_sprites.update(dt)
        self.display_surface.fill("black")
        self.all_sprites.draw(self.display_surface)