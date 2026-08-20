import pygame
from pygame.locals import K_a, K_s, K_d, K_w

JorgePNG = pygame.image.load("assets/JorgeVJ.png")
JorgePNG_scaled = pygame.transform.scale(JorgePNG, (80, 80))


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):

        # ? super().__init__() inicializa la clase padre (Sprite)
        super().__init__()

        self.image = JorgePNG_scaled
        self.rect = self.image.get_rect()
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

    def update(self, pressed_keys):
        # TODO (2.6): Mover a Jorge
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -4)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 4)
        if pressed_keys[K_a]:
            self.rect.move_ip(-4, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(4, 0)    

        # TODO (2.6): Mantener a Jorge en Pantalla
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, self.screen_width)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, self.screen_height)
