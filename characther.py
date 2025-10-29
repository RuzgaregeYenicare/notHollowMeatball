from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.Surface(scaler(tileScale, 96, 96))
        self.image.fill("green")
        self.rect = self.image.get_frect(topleft = pos)

        #hareket
        self.direction = vec()
        self.speed = 350

    def input(self):
        pressed = pygame.key.get_pressed()
        inVector = vec()

        if pressed[pygame.K_d]:
            inVector.x += 1
        if pressed[pygame.K_a]:
            inVector.x -= 1
        
        self.direction = inVector.normalize() if inVector else inVector

    def movement(self, deltaTime):
        self.rect.topleft += self.direction * self.speed * deltaTime

    def update(self, dt):
        self.input()
        self.movement(dt)