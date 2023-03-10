import pygame
import os

width, height = 900, 500
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("First Game!")

BLUE = (65, 155, 255)
RED = (255, 0, 0)
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

BORDER = pygame.Rect(width/2 - 5, 0, 10, height)


def draw_window(red, yellow):
    WIN.fill(BLUE)
    pygame.draw.rect(WIN, RED, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def listen():
    # global red, yellow
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and yellow.y - VEL > 0: # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_DOWN] and yellow.y + VEL + yellow.height < height-20: # DOWN
        yellow.y += VEL
    if keys_pressed[pygame.K_w] and red.y - VEL > 0: # w
        red.y -= VEL
    if keys_pressed[pygame.K_s] and red.y + VEL + red.height < height-20: # s
        red.y += VEL

    if keys_pressed[pygame.K_LEFT] and yellow.x - VEL > 0: # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VEL + 30 < BORDER.x: # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_a] and red.x - VEL > BORDER.x + 2: # a
        red.x -= VEL
    if keys_pressed[pygame.K_d] and red.x - VEL < width - red.width: # d
        red.x += VEL


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
