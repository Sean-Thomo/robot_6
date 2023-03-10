import pygame
import os
pygame.font.init()

width, height = 900, 500
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("First Game!")

SILVER = (192, 192, 192)
BLUE = (50, 80, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
FPS = 200
VEL = 5
SPACE_WIDTH, SPACE_HEIGHT = 55, 40

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACE_WIDTH, SPACE_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACE_WIDTH, SPACE_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (width, height))

BORDER = pygame.Rect(width//2 - 5, 0, 10, height)

BULLET_VEL = 7
MAX_BULLETS = 5


def draw_window(red, yellow):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    
    red_health_text = HEALTH_FONT.render("HEALTH: "+str(red_health), 1, SILVER)
    yellow_health_text = HEALTH_FONT.render("HEALTH: "+str(yellow_health), 1, SILVER)
    
    WIN.blit(red_health_text, (width - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    
    for yB in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, yB)
    
    for rB in red_bullets:
        pygame.draw.rect(WIN, RED, rB)
    
    pygame.display.update()


def listen():
    # global red, yellow
    keys_pressed = pygame.key.get_pressed()
    # YELLOW MOVEMENT
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < height-20:  # DOWN
        yellow.y += VEL
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + 30 < BORDER.x:  # RIGHT
        yellow.x += VEL

    # RED MOVEMENT
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # w
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < height-20:  # s
        red.y += VEL
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + 2:  # a
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x - VEL < width - red.width:  # d
        red.x += VEL


def handle_bullets(yellow_bullets, red_bullets):
    global red, yellow

    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > width:
            yellow_bullets.remove(bullet)
    
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def main():
    global red, yellow, red_bullets, yellow_bullets, red_health, yellow_health

    red = pygame.Rect(700, 300, SPACE_WIDTH, SPACE_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACE_WIDTH, SPACE_HEIGHT)

    red_bullets = []
    yellow_bullets = []
    
    red_health = 20
    yellow_health = 20

    output = ""

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSLASH and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                if event.key == pygame.K_b and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                
            if event.type == RED_HIT:
                red_health -= 1
            if event.type == YELLOW_HIT:
                yellow_health -= 1
        
        if red_health <= 0:
            output = "Yellow Wins!"
        
        if yellow_health <= 0:
            output = "Red Wins!"
        
        if output != None or output != "":
            pass
        
        handle_bullets(yellow_bullets, red_bullets)
        # print(red_bullets, yellow_bullets)
        listen()
        draw_window(red, yellow)

    pygame.quit()


if __name__ == '__main__':
    main()
