import pygame
import os

width, height = 900, 500
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("First Game!")

COLOR = (65, 155, 255)
FPS = 60
VEL = 5
SPACE_WIDTH, SPACE_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACE_WIDTH, SPACE_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACE_WIDTH, SPACE_HEIGHT)), 270)


def draw_window(red, yellow):
    WIN.fill(COLOR)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def listen():
    # global red, yellow
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP]: # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_DOWN]: # DOWN
        yellow.y += VEL
    if keys_pressed[pygame.K_w]: # w
        red.y -= VEL
    if keys_pressed[pygame.K_s]: # s
        red.y += VEL


def main():
    global red, yellow
    red = pygame.Rect(700, 300, SPACE_WIDTH, SPACE_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACE_WIDTH, SPACE_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        listen()
        draw_window(red, yellow)

    pygame.quit()


if __name__ == '__main__':
    main()
