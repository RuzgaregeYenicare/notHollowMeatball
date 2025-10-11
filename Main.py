import pygame, sys
from pygame import display, time

from settings import *

class Main:
    def __init__(self):

        pygame.init()

        self.screen = display.set_mode((screenWidth, screenHeight))
        self.clock = time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill("black")
            display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    window = Main()
    window.run()

'''Bizim kalbimiz ilim ateşiyle doludur,

Biz bağlıyız gönülden sevgili Lisemize

Bugün tuttuğumuz yol inkılabın yoludur

Yarının ümitleri genç nesil derler bize.

 

Bize iman veriyor hür vatanın hür sesi,

Ebediyen var olsun İZMİR ATATÜRK LİSESİ.

 

Nurlu mefkuremize Lise hayat veriyor,

İlim bizim aşkımız, Türklük bizim şanımız,

Gideceğimiz yolu Gazi’miz gösteriyor,

Yaşasın Türk Milleti, yaşasın vatanımız.

 

Bize iman veriyor hür vatanın hür sesi,

Ebediyen var olsun İZMİR ATATÜRK LİSESİ'''