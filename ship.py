from constants import *
from laser import *


class Ship:

    # Główna klasa z której dziedziczą zarówno
    # statki przeciwników jak i statek gracza

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        # Funkcja rysująca statek jak i lasery, którymi strzela
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        # Funkcja, która odpowiada za ruch laserów i sprawdzanie kolizji
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cooldown(self):
        # Funkcja, która odpowiada za to,
        # aby statki nie mogły strzelać non-stop,
        # tylko aby była przerwa między strzałami
        if self.cool_down_counter >= COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        # Funkcja odpowiedzialna za strzał
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        # Getter szerokości
        return self.ship_img.get_width()

    def get_height(self):
        # Getter wysokości
        return self.ship_img.get_height()
