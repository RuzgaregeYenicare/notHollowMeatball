import pygame, sys
from pygame.math import Vector2 as vec

screenWidth, screenHeight = 1280, 720
FPS = 60
tileSize = 32
tileScale = 2

def scaler(scale, *args):
    return tuple(i * scale for i in args)

layerList = {}
#KAYDETMEYI UNUTMA