from constants import *
from utils import draw_window, draw_winner, handle_bullets
from controllers import movement_red_static, movement_yellow


def static_controller(red, yellow, yellow_bullets):
    act1, act2, act3, act4, act5 = 0, 0, 0, 0, 0

    bullets_front = [1 if b.x < red.x else 1 for b in yellow_bullets]
    if len(bullets_front) < 3:
        act1 = 1
    else:
        act2 = 1

    if red.y <= yellow.y - 30:
        act4 = 1
    elif red.y >= yellow.y + 30:
        act3 = 1

    if (red.y > yellow.y - 30) and (red.y < yellow.y + 30):
        act5 = 1

    return act1, act2, act3, act4, act5


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = list()
    yellow_bullets = list()

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True

    while run:

        clock.tick(FPS)
        act1, act2, act3, act4, act5 = static_controller(red, yellow, yellow_bullets)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if (act5 == 1) and len(red_bullets) < MAX_BULLETS:
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
        movement_red_static(red, act1, act2, act3, act4)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text:
            draw_winner(winner_text)
            break

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    main()


if __name__ == "__main__":
    main()
