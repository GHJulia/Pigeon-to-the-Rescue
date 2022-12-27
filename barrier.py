import pygame

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Pigeon to the Rescue")
icon = pygame.image.load('pigeon.png')
pygame.display.set_icon(icon)

playerX, playerY = 150, 490

jumping = False

Y_gravity = 1
jump_height = 25
Y_velocity = jump_height

standing_surface = pygame.transform.scale(pygame.image.load('001-pigeon.png'), (64,64))
jumping_surface = pygame.transform.scale(pygame.image.load('001-pigeon.png'), (64,64))
background = pygame.image.load('sky.png')

pigeon_rect = standing_surface.get_rect(center=(playerX, playerY))

obstacle1X, obstacle1Y = 750 , 475
obstacle1_image = pygame.transform.scale(pygame.image.load('001-barrier.png'), (55,55))
def obstacle1 (x,y):
    screen.blit(obstacle1_image, (x,y))

obstacle2X, obstacle2Y = 1200 , 475
obstacle2_image = pygame.transform.scale(pygame.image.load('001-barrier.png'), (55,55))
def obstacle2 (x,y):
    screen.blit(obstacle2_image, (x,y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_pressed = pygame.key.get_pressed()

    if key_pressed [pygame.K_SPACE]:
        jumping = True

    screen.blit(background, (0,0))
    
    if jumping:
        playerY -= Y_velocity
        Y_velocity -= Y_gravity
        if Y_velocity < -jump_height:
            jumping = False
            Y_velocity = jump_height
        pigeon_rect = jumping_surface.get_rect(center=(playerX, playerY))
        screen.blit(jumping_surface, pigeon_rect)
    else:
        pigeon_rect = standing_surface.get_rect(center=(playerX, playerY))
        screen.blit(standing_surface, pigeon_rect)

    obstacle1X -= 3.5
    obstacle1(obstacle1X, obstacle1Y)

    obstacle2X -= 3.5
    obstacle2(obstacle2X, obstacle2Y)

    pygame.display.update()
    clock.tick(60)