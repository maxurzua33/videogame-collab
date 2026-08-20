import random

import pygame

BUGpng = pygame.image.load("assets/bug.png")
BUGpng_scaled = pygame.transform.scale(BUGpng, (64, 64))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):

        # ? super().__init__() inicializa la clase padre (Sprite)
        super().__init__()

        self.image = BUGpng_scaled
        self.rect = self.image.get_rect(
            center=(
                random.randint(0, screen.get_width()),
                - 10,
                
            )
        )
        self.speed = random.randint(3, 5)

    def update(self):
        # TODO (2.6): Mover a los enemigos
        self.rect.move_ip(0, self.speed)

        # TODO (2.6): Destruir a los enemigos
        if self.rect.bottom < 0:
            self.kill()
        pass
