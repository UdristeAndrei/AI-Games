import pygame
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SNAKE_SIZE = 20
APPLE_SIZE = 20

FPS = 50
VEL = 5
MOVE_90 = SNAKE_SIZE // VEL
