import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Loading Images
sky_bg = pygame.image.load("blue.jpg")
sky_bg = pygame.transform.scale(sky_bg, (1280, 720))
land_bg = pygame.image.load("Land_BG.png")
water_bg = pygame.image.load("Water_BG.png")
cloud1_bg = pygame.image.load("Cloud1.png")
cloud2_bg = pygame.image.load("Cloud2.png")
text_1 = pygame.image.load("text_1.png")
text_1 = pygame.transform.scale(text_1, (32*3, 56*3))
text_2 = pygame.image.load("text_2.png")
text_2 = pygame.transform.scale(text_2, (32*3, 56*3))
text_3 = pygame.image.load("text_3.png")
text_3 = pygame.transform.scale(text_3, (32*3, 56*3))

# Game Introduction
screen.blit(sky_bg, (0,0))
screen.blit(text_3, (550,320))
pygame.display.update()
pygame.time.delay(1000)
screen.blit(sky_bg, (0,0))
screen.blit(text_2, (550,320))
pygame.display.update()
pygame.time.delay(1000)
screen.blit(sky_bg, (0,0))
screen.blit(text_1, (550,320))
pygame.display.update()
pygame.time.delay(1000)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sky_bg, (0,0))
    screen.blit(land_bg, (0, 560))
    screen.blit(water_bg, (0, 640))
    screen.blit(cloud1_bg, (300, 100))
    screen.blit(cloud2_bg, (100, 150))
    screen.blit(cloud1_bg, (800, 200))
    screen.blit(cloud2_bg, (1000, 170))
    screen.blit(cloud1_bg, (600, 50))
    pygame.display.update()
    clock.tick(120)

