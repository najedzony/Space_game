import pygame


def collide(obj1, obj2):
    # Funkcja odpowiedzialna za sprawdzanie kolizji między obiektami
    offset_x, offset_y = obj2.x - obj1.x, obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


class Laser:

    # Klasa odpowiedzialna za lasery, którymi strzela gracz i przeciwnicy

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(img)

    def draw(self, window):
        # Funkcja do rysowania lasera
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        # Funkcja do ruchu lasera
        self.y += vel

    def off_screen(self, height):
        # Funkcja do sprawdzenia, czy laser nie jest poza ekranem
        return not (self.y < height and self.y > 0)

    def collision(self, obj):
        # Funkcja do sprawdzania kolizji
        return collide(obj, self)
