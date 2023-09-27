from constants import *


def draw_window(snake, apple):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, RED, apple)
    for body_part in snake.snake_body:
        pygame.draw.rect(WIN, WHITE, body_part)
    pygame.display.update()


def get_state_map(snake, apple, eps=25):
    state = list()
    found_a = False
    found_s = False

    for y in range(0, HEIGHT, TILE_SIZE):
        row = list()
        for x in range(0, WIDTH, TILE_SIZE):
            if abs(apple.x - x) <= eps and abs(apple.y - y) <= eps:
                found_a = True
                row.append(2)

            if abs(snake.snake_body[-1].x - x) <= eps and abs(snake.snake_body[-1].y - y) <= eps:
                found_s = True
                row.append(3)

            for snake_part in snake.snake_body[:-1]:
                if abs(snake_part.x - x) <= eps and abs(snake_part.y - y) <= eps:
                    found_s = True
                    row.append(1)

            if not found_a and not found_s:
                row.append(0)

            found_a = False
            found_s = False
        state.append(row)
    return state


def get_distance(obj1, obj2):
    dist1 = 0
    dist2 = 0
    if obj1 - obj2 > 0:
        dist1 = obj1 - obj2
    else:
        dist2 = abs(obj1 - obj2)
    return dist1, dist2


def get_inputs(snake, apple):
    up = 0
    down = 0
    left = 0
    right = 0

    up_obj = 0
    down_obj = 0
    left_obj = 0
    right_obj = 0

    if snake.snake_body[-1].x == apple.x:
        up, down = get_distance(snake.snake_body[-1].y, apple.y)
        if up > 0:
            up_obj = 1
        if down > 0:
            down_obj = 1

    if snake.snake_body[-1].y == apple.y:
        left, right = get_distance(snake.snake_body[-1].x, apple.x)
        if left > 0:
            left_obj = 1
        if right > 0:
            right_obj = 1

    for snake_part in snake.snake_body[:-1]:
        if snake.snake_body[-1].x == snake_part.x:
            t_up, t_down = get_distance(snake.snake_body[-1].y, snake_part.y)

            if up < t_up:
                up = t_up
                up_obj = 0

            if down < t_down:
                down = t_down
                down_obj = 0

        if snake.snake_body[-1].y == snake_part.y:
            t_left, t_right = get_distance(snake.snake_body[-1].x, snake_part.x)

            if left < t_left:
                left = t_left
                left_obj = 0

            if right < t_right:
                right = t_right
                right_obj = 0

    return up, up_obj, down, down_obj, left, left_obj, right, right_obj
