from snake import Snake, gen_apple
from utils import draw_window
from constants import *


# def get_inputs(snake, apple):
#     if
#     print(snake.snake_body[0].snake_part.x, snake.snake_body[0].snake_part.y)
#     print(snake.snake_body[0].last_movement)


def main():
    run = True
    snake = Snake()
    apple = gen_apple(snake.snake_body[0].snake_part)
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        # get_inputs(snake, apple)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        key_pressed = pygame.key.get_pressed()

        death_flag = snake.movement_snake(key_pressed[pygame.K_UP], key_pressed[pygame.K_DOWN],
                               key_pressed[pygame.K_LEFT], key_pressed[pygame.K_RIGHT])

        if death_flag:
            break
        apple = snake.eat_apple(apple)
        draw_window(snake, apple)


if __name__ == "__main__":
    main()
