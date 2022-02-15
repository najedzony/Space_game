from ship import *


class Enemy(Ship):

    # Ta klasa zajmuje się obiektami naszych przeciwników

    COLOR_MAP = {
        "red": (RED_SPACESHIP, RED_LASER, RED_LASER_VEL, RED_VEL),
        "green": (GREEN_SPACESHIP, GREEN_LASER, GREEN_LASER_VEL, GREEN_VEL),
        "blue": (BLUE_SPACESHIP, BLUE_LASER, BLUE_LASER_VEL, BLUE_VEL),
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img, self.laser_vel, self.vel = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        # Funkcja odpowiedzialna za ruch
        self.y += vel

    def shoot(self):
        # Funkcja odpowiedzialna za strzelanie
        if self.cool_down_counter == 0:
            laser = Laser(self.x - 20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
