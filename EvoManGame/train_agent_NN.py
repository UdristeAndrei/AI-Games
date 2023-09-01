import os
import sys
import pickle
import numpy as np
sys.path.insert(0, 'evoman')
from environment import Environment
from controllers import player_controller_NN

nn_structure = [20, 10, 5]
pop_size = 75
nr_gen = 25
p_crossover = 0.8
p_mutation = 0.2
enemy = 3

if True:
    os.environ["SDL_VIDEODRIVER"] = "dummy"

experiment_name = 'results/train_nn'
if not os.path.exists(experiment_name):
    os.makedirs(experiment_name)

env = Environment(experiment_name=experiment_name,
                  enemies=[enemy],
                  playermode="ai",
                  player_controller=player_controller_NN(),
                  enemymode="static",
                  randomini="yes",
                  level=2,
                  speed="fastest",
                  # savelogs="no",
                  logs="off")


def gen_agents(structure, population_size=20):
    population = list()
    for i in range(population_size):
        controller = list()

        for idx, layer in enumerate(structure[1:]):
            weights = np.random.normal(0, 1/structure[idx], (structure[idx], layer))
            controller.append(weights)

        population.append(controller)
    return population


def run_agents(population):
    fitness_pop = dict()
    for individual in population:
        f, p, e, t = env.play(individual)
        fitness_pop[f] = individual
    return fitness_pop


def tournament(fitness):
    agent1, agent2 = np.random.choice(fitness, 2)
    if agent1 > agent2:
        return agent1
    else:
        return agent2


def crossover(agent1, agent2):
    for i in range(len(agent1)):
        if np.random.random(1) <= p_crossover:
            agent1[i], agent2[i] = agent2[i], agent1[i]
    return agent1, agent2


def mutation(agent, mutation_weight=0.5):
    for i in range(len(agent)):
        if np.random.random(1) <= p_mutation:
            agent[i] += np.random.normal(0, mutation_weight/agent[i].shape[0], agent[i].shape) * \
                        np.random.choice([0, 1], size=agent[i].shape, p=[1-p_mutation, p_mutation])
    return agent


def select_agents(population):
    fitness = sorted(population.keys(), reverse=True)[:int(pop_size*0.5)]

    best_player = fitness[0]
    new_population = list()
    for _ in range(pop_size // 2):

        agt1 = tournament(fitness)
        agt2 = tournament(fitness)

        population[agt1], population[agt2] = crossover(population[agt1], population[agt2])

        new_population.append(mutation(population[agt1]))
        new_population.append(mutation(population[agt2]))

    return new_population, best_player


def save_agent(gen, agent, fitness):
    pickle.dump(agent, open(experiment_name + f"/agent_gen-{gen}_enemy-{enemy}_fitness-{int(fitness)}.pkl", "wb"))


def main():
    pop = gen_agents(nn_structure, pop_size)
    best_player_fitness = -10
    best_player = 0
    for i in range(nr_gen):
        pop_fitness = run_agents(pop)

        print("Generation:", i, "avg:", np.mean(list(pop_fitness.keys())), "max:", max(pop_fitness.keys()))

        pop, best_fitness = select_agents(pop_fitness)

        if best_player_fitness < best_fitness:
            best_player = pop_fitness[best_fitness]
            best_player_fitness = best_fitness

        if i % 5 == 0:
            save_agent(i, best_player, best_player_fitness)
            best_player_fitness = -10
            best_player = 0


if __name__ == "__main__":
    main()
