import random
from constants import *
from ship import *
from laser import *
from player import *
from enemy import *
from data_base import *
from getting_name import *


def main(name):
    # Główna funkcja, w której znajduje się pętla, w której działa nasz program

    run = True
    clock = pygame.time.Clock()
    level = 0
    lives = 5

    enemies = []
    wave_length = 5
    lost = False
    lost_count = 0
    score = 0
    added_to_base = False

    player = Player(300, 650)

    def draw_window():
        # Funkcja, która wyświetla wszystko na ekranie
        WIN.blit(BACKGROUND, (0, 0))
        lives_text = MAIN_FONT.render("Lives: " + str(lives), 1, WHITE)
        level_text = MAIN_FONT.render("Level: " + str(level), 1, WHITE)

        WIN.blit(lives_text, (10, 10))
        WIN.blit(level_text, (WIDTH - level_text.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_text = LOST_FONT.render("You lost!!!", 1, WHITE)
            score_text = LOST_FONT.render(
                "Your score is: " + str(score), 1, WHITE)
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2))
            WIN.blit(score_text, (WIDTH/2 -
                     score_text.get_width()/2, HEIGHT * 2 // 3))

        pygame.display.update()

    while run:
        clock.tick(FPS)

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if not lost:
            score += 1

        draw_window()

        if lost:
            if lost_count > FPS * 3:
                run = False
                if not added_to_base:
                    add_score(name, score)
                    added_to_base = True
                    view_score()
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(
                    50, WIDTH - 100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT] and player.x - PLAYER_VEL > 0:
            player.x -= PLAYER_VEL
        if keys_pressed[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.get_width() < WIDTH:
            player.x += PLAYER_VEL
        if keys_pressed[pygame.K_UP] and player.y - PLAYER_VEL > 0:
            player.y -= PLAYER_VEL
        if keys_pressed[pygame.K_DOWN] and player.y + PLAYER_VEL + player.get_height() + 15 < HEIGHT:
            player.y += PLAYER_VEL
        if keys_pressed[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy.vel)
            enemy.move_lasers(enemy.laser_vel, player)

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)

            if random.randrange(0, 120) == 1:
                enemy.shoot()
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-LASER_VEL, enemies)


def main_menu():
    # Funkcja, która zajmuje się wyświetlaniem głównego menu
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    got_name = False
    while run:

        WIN.blit(BACKGROUND, (0, 0))
        if not got_name:
            name = inpt()
            got_name = True
        title_text = title_font.render("Press the mouse to begin...", 1, WHITE)
        WIN.blit(title_text, (WIDTH / 2 - title_text.get_width()/2, 350))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main(name)

    pygame.quit()


if __name__ == '__main__':
    main_menu()
