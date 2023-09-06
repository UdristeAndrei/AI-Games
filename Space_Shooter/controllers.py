import pygame
import constants


def movement_red(agent, key_presses):
    if key_presses[pygame.K_LEFT]:
        if agent.x > constants.WIDTH / 2 + 5:
            agent.x -= constants.VEL

    if key_presses[pygame.K_RIGHT]:
        if agent.x < constants.WIDTH - constants.SPACESHIP_WIDTH:
            agent.x += constants.VEL

    if key_presses[pygame.K_UP]:
        if agent.y > 0:
            agent.y -= constants.VEL

    if key_presses[pygame.K_DOWN]:
        if agent.y < constants.HEIGHT - constants.SPACESHIP_HEIGHT:
            agent.y += constants.VEL


def movement_yellow(agent, key_presses):
    if key_presses[pygame.K_a]:
        if agent.x > 0:
            agent.x -= constants.VEL

    if key_presses[pygame.K_d]:
        if agent.x < constants.WIDTH/2 - constants.SPACESHIP_WIDTH:
            agent.x += constants.VEL

    if key_presses[pygame.K_w]:
        if agent.y > 0:
            agent.y -= constants.VEL

    if key_presses[pygame.K_s]:
        if agent.y < constants.HEIGHT - constants.SPACESHIP_HEIGHT:
            agent.y += constants.VEL


def movement_red_static(agent, act1, act2, act3, act4):
    if act1 == 1:
        if agent.x > constants.WIDTH / 2 + 5:
            agent.x -= constants.VEL

    if act2 == 1:
        if agent.x < constants.WIDTH - constants.SPACESHIP_WIDTH:
            agent.x += constants.VEL

    if act3 == 1:
        if agent.y > 0:
            agent.y -= constants.VEL

    if act4 == 1:
        if agent.y < constants.HEIGHT - constants.SPACESHIP_HEIGHT:
            agent.y += constants.VEL


def movement_yellow_ai(agent, act1, act2, act3, act4):
    if act1 == 1:
        if agent.x > 0:
            agent.x -= constants.VEL

    if act2 == 1:
        if agent.x < constants.WIDTH/2 - constants.SPACESHIP_WIDTH:
            agent.x += constants.VEL

    if act3 == 1:
        if agent.y > 0:
            agent.y -= constants.VEL

    if act4 == 1:
        if agent.y < constants.HEIGHT - constants.SPACESHIP_HEIGHT:
            agent.y += constants.VEL
