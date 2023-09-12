from constants import *
from utils import draw_window, draw_winner, handle_bullets, init_player, det_winner
from controllers import movement_red, movement_yellow


def main():
    red, red_health, red_bullets = init_player(10, HEIGHT-SPACESHIP_HEIGHT, WIDTH//2, WIDTH - SPACESHIP_WIDTH)
    yellow, yellow_health, yellow_bullets = init_player(10, HEIGHT - SPACESHIP_HEIGHT, 0, WIDTH//2 - SPACESHIP_WIDTH)

    clock = pygame.time.Clock()
    run = True

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        key_pressed = pygame.key.get_pressed()
        movement_yellow(yellow, key_pressed)
        movement_red(red, key_pressed)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        winner = det_winner(red_health, yellow_health)
        if winner:
            draw_winner(winner)
            break

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    main()


if __name__ == "__main__":
    main()
