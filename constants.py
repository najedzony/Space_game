import pygame
import os

# W tym pliku znajdują się wszystkie stałe, których używam w reszcie programu

pygame.font.init()
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")
FPS = 60

# Enemy ships
RED_SPACESHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_red_small.png"))
BLUE_SPACESHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_blue_small.png"))
GREEN_SPACESHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_green_small.png")
)

# Player ship
YELLOW_SPACESHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_yellow.png"))

# Bullets
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_yellow.png"))

# Enemy vel
GREEN_LASER_VEL = 5
BLUE_LASER_VEL = 8
RED_LASER_VEL = 15

RED_VEL = 3
GREEN_VEL = 1
BLUE_VEL = 2

# Background
BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join(
        "assets", "background-black.png")), (WIDTH, HEIGHT)
)

MAIN_FONT = pygame.font.SysFont("comicsans", 50)
LOST_FONT = pygame.font.SysFont("comcsans", 60)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PLAYER_VEL = 7
LASER_VEL = 10
COOLDOWN = 10
