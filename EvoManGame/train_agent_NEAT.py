import os
import sys
import pickle

import neat.config
import numpy as np
sys.path.insert(0, 'evoman')
from environment import Environment
from controllers import player_controller_NEAT

nr_gen = 50
enemy = 1
headless = False

if headless:
    os.environ["SDL_VIDEODRIVER"] = "dummy"

experiment_name = 'results/train_neat'
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

env = Environment(experiment_name=experiment_name,
                  enemies=[enemy],
                  playermode="ai",
                  player_controller=player_controller_NEAT(),
                  enemymode="static",
                  randomini="yes",
                  level=2,
                  speed="fastest",
                  # savelogs="no",
                  logs="off")


def save_agent(agent, fitness):
    pickle.dump(agent, open(experiment_name + f"/agent_enemy-{enemy}_fitness-{int(fitness)}.pkl", "wb"))


def eval_genomes(genomes, config):
    best_fitness = -5
    best_net = None

    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        f, p, e, t = env.play(net)
        genome.fitness = f

        if best_fitness < f:
            best_net = net
            best_fitness = f

    save_agent(best_net, best_fitness)


def main(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet,
                                neat.DefaultStagnation, config_path)

    pop = neat.Population(config)

    pop.add_reporter(neat.StdOutReporter(True))
    pop.add_reporter(neat.StatisticsReporter())

    winner = pop.run(eval_genomes, nr_gen)

    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    pickle.dump(winner_net, open(experiment_name + f"/agent_enemy-{enemy}_winner.pkl", "wb"))


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    main(config_path)
