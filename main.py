
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Initialize pygame, set up screen, and clock
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set up containers for sprites
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Create player and asteroid field
    my_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update game state
        for player in updatable:
            player.update(dt)

        # Check collisions
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collisions(shot):
                    asteroid.split()
                    shot.kill()
                    break # Exit inner loop to avoid modifying the group during iteration
            if asteroid.check_collisions(my_player):
                print("Game Over!")
                pygame.quit()
                return
            
        # Draw everything
        screen.fill("black")
        for player in drawable:
            player.draw(screen)

        # Flip display
        pygame.display.flip()

        # Tick clock
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
