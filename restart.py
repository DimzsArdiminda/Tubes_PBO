import pygame
import sys

pygame.init()

# ukuran jendela
screen_width = 640
screen_height = 480

# membuat jendela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Contoh Tombol Restart")

# inisialisasi font dan teks
font = pygame.font.Font(None, 36)
text = font.render("Restart", True, (255, 255, 255))

# ukuran tombol
button_width = 120
button_height = 50

# membuat rect untuk tombol
button_rect = pygame.Rect((screen_width // 2) - (button_width // 2),
                          (screen_height // 2) - (button_height // 2),
                          button_width, button_height)

# fungsi untuk memulai ulang program
def restart_game():
    # tambahkan logika untuk memulai ulang program
    start_menu.run()

# loop utama program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
            restart_game()

    # menggambar tombol ke layar
    pygame.draw.rect(screen, (0, 0, 255), button_rect)
    screen.blit(text, (button_rect.x + (button_width // 2) - (text.get_width() // 2),
                       button_rect.y + (button_height // 2) - (text.get_height() // 2)))

    pygame.display.flip()
