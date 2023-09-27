import math
import os
import neat
from snake import Snake
from utils import draw_window, get_inputs
from constants import *


def controller_neat(inputs, network):
    outputs_nn = network.activate(inputs)
    outputs = [0 if (x <= 0) else 1 for x in outputs_nn]
    return outputs


def run_game(network, best=False):
    run = True
    snake = Snake()
    apple = snake.gen_apple()
    clock = pygame.time.Clock()
    time = 0
    reward = 1
    while run:
        if best:
            clock.tick(FPS)
        else:
            clock.tick()
            clock.tick_busy_loop()

        inputs = get_inputs(snake, apple)

        up, down, left, right = controller_neat(inputs, network)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        snake.move_snake(up, down, left, right)
        apple, apple_eaten = snake.eat_apple(apple)

        reward += apple_eaten
        death = snake.death()

        if death or time > 2000 * reward:
            return math.log(time) + 10 * reward

        time += 1
        draw_window(snake, apple)

    pygame.quit()


def eval_genomes(genomes, config):
    best_f = 0
    best_net = None
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        f = run_game(net)
        genome.fitness = f
        if f > best_f:
            best_f = f
            best_net = net
    print("Running the best player")
    run_game(best_net, True)


def main(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet,
                                neat.DefaultStagnation, config_path)

    pop = neat.Population(config)

    pop.add_reporter(neat.StdOutReporter(True))
    pop.add_reporter(neat.StatisticsReporter())

    winner = pop.run(eval_genomes, 50)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    main(config_path)
