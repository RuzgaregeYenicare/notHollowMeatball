from settings import *
from pygame import display
from os import path
from level import Level
from pytmx.util_pygame import load_pygame

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
            
            self.current_stage.run()
            display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    window = Main()
    window.run()
    #KAYDETMEYI UNUTMA