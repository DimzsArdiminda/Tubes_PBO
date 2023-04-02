import pygame
import menu0

pygame.init()
pygame.font.init()


if __name__ == '__main__':
    # Set up the screen 800 600
    screen = pygame.display.set_mode((800, 600))

    # Show the start menu
    start_menu = menu0.StartMenu(screen)
    start_menu.run()

    # # Show the end menu
    # end_menu = menu0.EndMenu(screen)
    # end_menu.run()



