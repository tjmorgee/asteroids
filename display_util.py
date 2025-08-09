import pygame
from constants import *
from player import Player

def show_game_over(screen, font, score, high_score, high_score_name):
    # Display game over screen
    screen.fill("black")
    game_over_surface = font.render("GAME OVER", True, (255, 0, 0))
    game_over_rect = game_over_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
    screen.blit(game_over_surface, game_over_rect)

    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(score_surface, score_rect)

    high_score_surface = font.render(f"High Score: {high_score} ({high_score_name})", True, (255, 255, 0))
    high_score_rect = high_score_surface.get_rect(center=(SCREEN_WIDTH // 2, 75))
    screen.blit(high_score_surface, high_score_rect)

    prompt_surface = font.render("Press any key to restart or ESC to quit", True, (200, 200, 200))
    prompt_rect = prompt_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
    screen.blit(prompt_surface, prompt_rect)

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                else:
                    waiting = False
                    return

def get_player_name(screen, font):
    name = ""
    prompt = font.render("Enter your name:", True, (255, 255, 255))
    while True:
        screen.fill("black")
        screen.blit(prompt, (SCREEN_WIDTH // 2 - prompt.get_width() // 2, SCREEN_HEIGHT // 2 - 40))
        name_surface = font.render(name, True, (255, 255, 0))
        screen.blit(name_surface, (SCREEN_WIDTH // 2 - name_surface.get_width() // 2, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.unicode.isprintable():
                    name += event.unicode