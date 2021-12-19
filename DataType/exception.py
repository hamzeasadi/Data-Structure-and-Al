import os
import pygame
import random
import math
from pygame.locals import (
RLEACCEL, K_UP, K_DOWN, K_RIGHT, K_LEFT, K_ESCAPE, KEYDOWN, QUIT
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TETHA = math.pi/4
def circle_path(r, step, center=300):
    x = int(center + r*math.sin(step))
    y = int(center + r*math.cos(step))
    return x, y

# define player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # self.surf = pygame.Surface((25, 25))
        self.surf = pygame.image.load("jet.png").convert()
        # self.surf.fill((245, 66, 212))
        # self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        # self.surf = pygame.Surface((10, 10))
        # self.surf.fill((0, 0, 0))
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
        center=(
        random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
        random.randint(0, SCREEN_HEIGHT)
        )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right<0:
            self.kill()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    player = Player()

    all_sprites.add(player)

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 250)

    running = True
    step = math.pi
    while running:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == ADDENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()

        screen.fill(color=(58, 146, 158))
        # surface = pygame.Surface((50, 50))
        # surface.fill(color=(141, 58, 158))
        # this rect is same as surface
        # rect = surface.get_rect()
        # screen.blit(source=surface, dest=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        # screen.blit(source=surface, dest=(x+100, y+100))
        # screen.blit(source=player.surf, dest=((SCREEN_WIDTH/2, SCREEN_HEIGHT/2)))
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            running = False

        pygame.display.flip()
if __name__ == '__main__':
    main()
