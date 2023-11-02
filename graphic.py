import pygame
from enum import Enum
from game_class import Direction

screen_width = 400  # window width
screen_height = 320  # window height
row_count = 0  # get from reading
column_count = 0  # get from reading
delay = 0  # in milisecond (ms). The delay before passing a turn
tile_width = 0  # in pixel
score = 1000

""" Display pygame window (copied from wiki) """
def showWindow():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    running = True
    
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    showWindow()
