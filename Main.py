from settings import *
from pygame import display
from os import path
from pytmx.util_pygame import load_pygame

from level import Level

#KAYDETMEYI UNUTMA
class Main:
    def __init__(self):

        pygame.init()

        self.screen = display.set_mode((screenWidth, screenHeight))
        display.set_caption("Mitolojik Zımbırtı")

        self.tmx = {0: load_pygame(path.join("Data", "Levels", "ornek.tmx"))}

        self.clock = pygame.time.Clock()
        self.current_stage = Level(self.tmx[0])

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            deltaTime = self.clock.tick(FPS) / 1000
            self.current_stage.run(deltaTime)
            display.update()

if __name__ == "__main__":
    window = Main()
    window.run()
    #KAYDETMEYI UNUTMA