from constants import *


def draw_window(snake, apple):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, RED, apple)
    for body_part in snake.snake_body:
        pygame.draw.rect(WIN, WHITE, body_part)
    pygame.display.update()
