import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

    drawable_g = pygame.sprite.Group()
    updatable_g = pygame.sprite.Group()
    asteroid_g = pygame.sprite.Group()
    shot_g = pygame.sprite.Group()

    Player.containers = (drawable_g, updatable_g)
    Asteroid.containers = (asteroid_g, drawable_g, updatable_g)
    AsteroidField.containers = updatable_g
    Shot.containers = (shot_g, drawable_g, updatable_g)

    asteroid_field = AsteroidField()

    player = Player(x, y, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable_g:
            obj.update(dt)
        
        for obj in asteroid_g:
            if obj.collition(player):
                print("Game over!")
                return

            for bullet in shot_g:
                if obj.collition(bullet):
                    obj.split()
                    bullet.kill()

        screen.fill((0,0,0))
        
        for obj in drawable_g:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
