from snake import Snake
from utils import draw_window
from constants import *


def run_game():
    run = True
    time = 0
    snake = Snake()
    apple = snake.gen_apple()
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        key_pressed = pygame.key.get_pressed()

        time_now = pygame.time.get_ticks()
        if time_now - time > TIME_STEP:
            time = time_now
            snake.move_snake(key_pressed[pygame.K_UP], key_pressed[pygame.K_DOWN],
                             key_pressed[pygame.K_LEFT], key_pressed[pygame.K_RIGHT])
        apple = snake.eat_apple(apple)

        death = snake.death()
        if death:
            break

        draw_window(snake, apple)


if __name__ == "__main__":
    run_game()
