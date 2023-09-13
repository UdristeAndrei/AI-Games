from constants import *
import numpy as np


def gen_apple(snake):
    apple = pygame.Rect(np.random.randint(0, WIDTH - APPLE_SIZE), np.random.randint(0, HEIGHT - APPLE_SIZE),
                        APPLE_SIZE, APPLE_SIZE)

    while apple.colliderect(snake):
        apple = pygame.Rect(np.random.randint(0, WIDTH - APPLE_SIZE), np.random.randint(0, HEIGHT - APPLE_SIZE),
                            APPLE_SIZE, APPLE_SIZE)

    return apple


def gen_new_part(last_part):
    new_part = 0
    if last_part.last_movement == "up":
        new_part = SnakePart(last_part.snake_part.x, last_part.snake_part.y + SNAKE_SIZE)
    elif last_part.last_movement == "down":
        new_part = SnakePart(last_part.snake_part.x, last_part.snake_part.y + SNAKE_SIZE)
    elif last_part.last_movement == "left":
        new_part = SnakePart(last_part.snake_part.x, last_part.snake_part.y + SNAKE_SIZE)
    elif last_part.last_movement == "right":
        new_part = SnakePart(last_part.snake_part.x, last_part.snake_part.y + SNAKE_SIZE)
    return new_part


class SnakePart:
    def __init__(self, pos_x, pos_y):
        self.snake_part = pygame.Rect(pos_x, pos_y, SNAKE_SIZE, SNAKE_SIZE)
        self.last_movement = "up"
        self.turns = 0

    def choose_direction(self, up, down, left, right):
        if up and self.last_movement != "down":
            self.last_movement = "up"
        elif down and self.last_movement != "up":
            self.last_movement = "down"
        elif left and self.last_movement != "right":
            self.last_movement = "left"
        elif right and self.last_movement != "left":
            self.last_movement = "right"

    def movement(self):
        if self.last_movement == "up":
            self.snake_part.y -= VEL

        elif self.last_movement == "down":
            self.snake_part.y += VEL

        elif self.last_movement == "left":
            self.snake_part.x -= VEL

        elif self.last_movement == "right":
            self.snake_part.x += VEL

        self.move_wall()

    def move_wall(self):
        if self.snake_part.y < 0:
            self.snake_part.y = HEIGHT - SNAKE_SIZE

        if self.snake_part.y > HEIGHT - SNAKE_SIZE:
            self.snake_part.y = 0

        if self.snake_part.x < 0:
            self.snake_part.x = WIDTH - SNAKE_SIZE

        if self.snake_part.x > WIDTH - SNAKE_SIZE:
            self.snake_part.x = 0


class Snake:
    def __init__(self):
        snake_part = SnakePart(100, 100)
        self.snake_body = [snake_part]

    def movement_head(self, up, down, left, right):
        self.snake_body[0].choose_direction(up, down, left, right)
        self.snake_body[0].movement()

    def movement_body(self):
        for i in range(1, len(self.snake_body)):
            if self.snake_body[i].last_movement != self.snake_body[i - 1].last_movement and \
                    self.snake_body[i].turns <= 3:
                self.snake_body[i].turns += 1

            elif self.snake_body[i].last_movement != self.snake_body[i - 1].last_movement and \
                    self.snake_body[i].turns > 3:

                self.snake_body[i].last_movement = self.snake_body[i - 1].last_movement
                self.snake_body[i].turns = 0

            self.snake_body[i].movement()

    def death(self):
        for i in range(3, len(self.snake_body)):
            if self.snake_body[0].snake_part.colliderect(self.snake_body[i].snake_part):
                return True

        return False

    def movement_snake(self, up, down, left, right):
        self.movement_head(up, down, left, right)
        self.movement_body()
        return self.death()

    def eat_apple(self, apple):
        if self.snake_body[0].snake_part.colliderect(apple):
            new_snake_part = gen_new_part(self.snake_body[-1])

            self.snake_body.append(new_snake_part)
            apple = gen_apple(self.snake_body[0].snake_part)
        return apple
