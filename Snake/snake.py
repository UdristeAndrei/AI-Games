from constants import *
import random


class Snake:
    def __init__(self):
        self.snake_part = pygame.rect.Rect(0, 0, SNAKE_SIZE - 2, SNAKE_SIZE - 2)
        self.snake_part.center = random.randrange(*RANGE), random.randrange(*RANGE)
        self.last_movement = "up"
        self.length = 1
        self.snake_body = [self.snake_part.copy()]

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
            self.snake_part.move_ip(0, -TILE_SIZE)

        elif self.last_movement == "down":
            self.snake_part.move_ip(0, TILE_SIZE)

        elif self.last_movement == "left":
            self.snake_part.move_ip(-TILE_SIZE, 0)

        elif self.last_movement == "right":
            self.snake_part.move_ip(TILE_SIZE, 0)

        self.move_wall()

    def move_snake(self, up, down, left, right):
        self.choose_direction(up, down, left, right)
        self.movement()
        self.snake_body.append(self.snake_part.copy())
        self.snake_body = self.snake_body[-self.length:]

    def move_wall(self):
        if self.snake_part.y < 0:
            self.snake_part.y = HEIGHT - SNAKE_SIZE

        if self.snake_part.y > HEIGHT - SNAKE_SIZE:
            self.snake_part.y = 0

        if self.snake_part.x < 0:
            self.snake_part.x = WIDTH - SNAKE_SIZE

        if self.snake_part.x > WIDTH - SNAKE_SIZE:
            self.snake_part.x = 0

    def eat_apple(self, apple):
        if self.snake_body[-1].colliderect(apple):
            apple = self.gen_apple()
            self.length += 1
        return apple

    def death(self):
        for body_part in self.snake_body[:-1]:
            if self.snake_body[-1].colliderect(body_part):
                return True
        return False

    def gen_apple(self):
        apple = pygame.rect.Rect(0, 0, APPLE_SIZE, APPLE_SIZE)
        apple.center = random.randrange(*RANGE), random.randrange(*RANGE)

        i = 0
        while i < len(self.snake_body):
            if apple.colliderect(self.snake_body[i]):
                apple.center = random.randrange(*RANGE), random.randrange(*RANGE)
                i = 0
            i += 1

        return apple
