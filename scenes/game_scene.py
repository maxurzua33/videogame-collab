if __name__ == "__main__":  # ! Solo para que no ejecutes este archivo
    import sys

    print(
        "\033c"
        + "\033[38;2;255;0;0mESTE ARCHIVO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

from elements.enemy import Enemy
from elements.player import Player


def gameloop(screen):
    # * Preparamos la escena de juego, cargando los elementos que se van a usar en el loop principal

    # TODO (2.5): Añadir fondo del display
    background_image = pygame.image.load("assets/pixelBackground.jpg").convert()

    # TODO (2.7): Crear la instancia de jugador
    player = Player(screen)

    # TODO (2.7): Crear los grupos de sprites
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # TODO (2.8): Crear el generador de enemigos
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    # TODO (2.9): Crear el reloj del juego
    clock = pygame.time.Clock()

    running = True  # variable booleana para manejar el loop

    # * Loop principal del juego, todo lo que ocurre en el juego se hace dentro de este loop
    while running:
        # TODO (2.5): Dibujar la imagen de fondo en la ventana
        screen.blit(background_image,(0,0))

        # Iteramos sobre cada evento en la cola
        for event in pygame.event.get():
            if event.type == KEYDOWN:  # se presiono una tecla?
                if event.key == K_ESCAPE:  # era la tecla de escape?
                    running = False  # terminamos el loop

            elif event.type == QUIT:  # fue un click al cierre de la ventana?
                running = False  # terminamos el loop

            # TODO (2.8): Generar enemigos
            elif event.type == ADDENEMY:
                new_enemy = Enemy(screen)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            
        # TODO (2.7): Actualizar el estado interno de los sprites (posiciones, etc)
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()

        # TODO (2.7): Dibujar los sprites actualizados en la ventana
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)

        # TODO (2.10): Calcular colisiones entre jugador y enemigos
        if pygame.sprite.spritecollideany(player,enemies):
            player.kill()
            running = False
        # TODO (2.5): Actualizar la ventana para reflejar todos los cambios
        pygame.display.flip()


        # TODO (2.9): Controlar la velocidad de fotogramas
        clock.tick(60)