import pygame

from scenes import basic_scene, game_scene

# ? Inicializamos pygame
pygame.init()

# ? Definimos las medidas de nuestra pantalla
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# ? Creamos nuestro objeto pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# ? Aqui se ejecutaran las escenas del juego en orden
basic_scene.gameloop(screen)

# TODO (2.2): Añadir nueva escena de juego
game_scene.gameloop(screen)