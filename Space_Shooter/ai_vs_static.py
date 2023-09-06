import os
import neat
import numpy as np
from constants import *
from utils import draw_window, handle_bullets
from controllers import movement_red_static, movement_yellow_ai


def static_controller(red, yellow, yellow_bullets):
    act1, act2, act3, act4, act5 = 0, 0, 0, 0, 0

    bullets_front = [1 if b.x < red.x else 1 for b in yellow_bullets]
    if len(bullets_front) < 3:
        act1 = 1
    else:
        act2 = 1

    if red.y <= yellow.y - 10:
        act4 = 1
    elif red.y >= yellow.y + 10:
        act3 = 1

    if (red.y > yellow.y - 30) and (red.y < yellow.y + 30):
        act5 = 1

    return act1, act2, act3, act4, act5


def controller_neat(inputs, network):
    outputs_nn = network.activate(inputs)
    outputs = [0 if (x <= 0) else 1 for x in outputs_nn]
    return outputs


def gen_inputs(red, yellow, red_bullets, red_health, yellow_health):
    dist_ship_x = (red.x - yellow.x) / WIDTH
    dist_ship_y = (red.y - yellow.y) / HEIGHT
    dist_wall_up = yellow.y / HEIGHT
    dist_wall_down = (HEIGHT - yellow.y) / HEIGHT
    dist_wall_left = yellow.x / WIDTH
    dist_wall_right = (WIDTH//2 - 50 - yellow.x) / (WIDTH//2)

    bullets_data = np.zeros((5, 2))

    for i in range(len(red_bullets)):
        bullets_data[i][0] = (red_bullets[i].x - yellow.x) / WIDTH
        bullets_data[i][1] = (red_bullets[i].y - yellow.y) / HEIGHT

    return dist_ship_x, dist_ship_y,dist_wall_up, dist_wall_down, dist_wall_left, dist_wall_right, red_health/10, \
        yellow_health/10, *bullets_data.flatten()


def run_game(network):
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = list()
    yellow_bullets = list()

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    game_timer = 0

    while run:

        clock.tick()
        clock.tick_busy_loop()

        r_act1, r_act2, r_act3, r_act4, r_act5 = static_controller(red, yellow, yellow_bullets)
        inputs = gen_inputs(red, yellow, red_bullets, red_health, yellow_health)

        y_act1, y_act2, y_act3, y_act4, y_act5 = controller_neat(inputs, network)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        if (y_act5 == 1) and len(yellow_bullets) < MAX_BULLETS:
            bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
            yellow_bullets.append(bullet)
            BULLET_FIRE_SOUND.play()

        if (r_act5 == 1) and len(red_bullets) < MAX_BULLETS:
            bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
            red_bullets.append(bullet)
            BULLET_FIRE_SOUND.play()

        movement_yellow_ai(yellow, y_act1, y_act2, y_act3, y_act4)
        movement_red_static(red, r_act1, r_act2, r_act3, r_act4)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        if red_health <= 0 or yellow_health <= 0 or game_timer == 480:
            return 0.1 * (10 - red_health) + 0.9 * yellow_health - np.log(game_timer)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
        game_timer += 1

    pygame.quit()


def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        f = run_game(net)
        genome.fitness = f


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
