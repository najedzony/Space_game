from constants import *


def inpt():

    # Ta funkcja jest odpowiedzialna za pobranie nazwy gracza
    # i wyświetlenie jej na ekran

    name_text = LOST_FONT.render("Write your name and press enter!", 1, WHITE)
    word = ""
    letters = [
        pygame.K_a,
        pygame.K_b,
        pygame.K_c,
        pygame.K_d,
        pygame.K_e,
        pygame.K_f,
        pygame.K_g,
        pygame.K_h,
        pygame.K_i,
        pygame.K_j,
        pygame.K_k,
        pygame.K_l,
        pygame.K_m,
        pygame.K_n,
        pygame.K_o,
        pygame.K_p,
        pygame.K_q,
        pygame.K_r,
        pygame.K_s,
        pygame.K_t,
        pygame.K_u,
        pygame.K_v,
        pygame.K_x,
        pygame.K_y,
        pygame.K_z,
    ]
    WIN.blit(name_text, (WIDTH / 2 - name_text.get_width() / 2, HEIGHT / 2))
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key in letters:
                    word += chr(event.key)
                if event.key == pygame.K_RETURN:
                    done = False
                if event.key == pygame.K_BACKSPACE:
                    word = word[:-1]
        name = LOST_FONT.render(word, 1, WHITE)
        WIN.blit(BACKGROUND, (0, 0))
        WIN.blit(name_text,
                 (WIDTH / 2 - name_text.get_width() / 2, HEIGHT / 2))
        WIN.blit(name, (WIDTH / 2 - name.get_width() / 2, HEIGHT * 2 // 3))
        pygame.display.flip()
    return word
