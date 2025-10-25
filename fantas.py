from settings import *
import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surface, groups):
        super().__init__(groups)
        self.image = pygame.Surface((tileSize * tileScale, tileSize * tileScale))
        self.image.fill("white")
        self.rect = self.image.get_frect(topleft = pos)