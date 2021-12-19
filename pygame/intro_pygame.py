import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HIGHT = 600

black = (0,0,0)
white = (255,255,255)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
    pygame.display.set_caption('SIMPLE GAME')
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            print(event)


        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()