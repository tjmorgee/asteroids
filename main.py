
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from display_util import *
from destruction import DestructionAnimation

def main():
    # Initialize pygame, set up screen, and clock
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("background-music.ogg")
    pygame.mixer.music.play(-1)
    game_clock = pygame.time.Clock()
    dt = 0
    score = 0
    font = pygame.font.SysFont(None, 36)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pygame.image.load("stars.png").convert()

    # Load high score
    try:
        with open("highscore.txt", "r") as f:
            line = f.read().strip()
            if ":" in line:
                name_part, score_part = line.split(":", 1)
                high_score_name = name_part.strip()
                high_score = int(score_part.strip())
            else:
                high_score = int(line)
                high_score_name = ""
    except Exception:
        high_score = 0
        high_score_name = ""

    # Set up sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    animations = pygame.sprite.Group()

    # Set up containers for sprites
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    DestructionAnimation.containers = (animations, drawable)

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
                    animations.add(DestructionAnimation(asteroid.position))
                    asteroid.split()
                    shot.kill()
                    score += 1
                    break
            if asteroid.check_collisions(my_player):
                if score > high_score:
                    player_name = get_player_name(screen, font)
                    high_score = score
                    high_score_name = player_name
                    with open("highscore.txt", "w") as f:
                        f.write(f"{high_score_name}: {high_score}")
                pygame.mixer.music.stop()
                show_game_over(screen, font, score, high_score, high_score_name)
                pygame.quit()
                main()

        # Draw everything
        screen.blit(background, (0, 0))
        for player in drawable:
            player.draw(screen)
            animations.update(dt)
            animations.draw(screen)

        # Render and display score
        score_surface = font.render(f"{score}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(SCREEN_WIDTH // 2, 60))
        screen.blit(score_surface, score_rect)

        # Render high score
        high_score_surface = font.render(f"High Score: {high_score} ({high_score_name})", True, (255, 255, 0))
        high_score_rect = high_score_surface.get_rect(center=(SCREEN_WIDTH // 2, 25))
        screen.blit(high_score_surface, high_score_rect)

        # Flip display
        pygame.display.flip()

        # Tick clock
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
