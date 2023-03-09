import pygame
import os

width, height = 900, 500
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("First Game!")

COLOR = (65, 155, 255)
FPS = 60
SPACE_WIDTH, SPACE_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACE_WIDTH, SPACE_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACE_WIDTH, SPACE_HEIGHT)), 270)


def draw_window():
    WIN.fill(COLOR)
    WIN.blit(YELLOW_SPACESHIP, (300, 100))
    WIN.blit(RED_SPACESHIP, (700, 100))
    pygame.display.update()


def main():
    red = pygame.Rect(100, 300, )

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()
