import pygame
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 700, 700
TILE_SIZE = 50
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
RANGE = (TILE_SIZE // 2, WIDTH - TILE_SIZE // 2, TILE_SIZE)
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SNAKE_SIZE = APPLE_SIZE = TILE_SIZE

FPS = 60
TIME_STEP = 110
TOLERANCE = 5
