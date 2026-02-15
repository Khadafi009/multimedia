"""
Simple 2D Game - Avoid the Enemy
Controls:
Arrow Keys -> Move
R -> Restart after Game Over
ESC -> Quit
"""

import pygame
import random
import sys


WIDTH = 600
HEIGHT = 400
PLAYER_SIZE = 40
ENEMY_SIZE = 40
PLAYER_SPEED = 5
ENEMY_SPEED = 4


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple 2D Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)


def reset_game():
    """Reset player, enemy, and score."""
    player = pygame.Rect(WIDTH // 2, HEIGHT - 60, PLAYER_SIZE, PLAYER_SIZE)
    enemy = pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), 0, ENEMY_SIZE, ENEMY_SIZE)
    score = 0
    game_over = False
    return player, enemy, score, game_over


def draw_text(text):
    img = font.render(text, True, (255, 255, 255))
    rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(img, rect)


def main():
    player, enemy, score, game_over = reset_game()
    running = True

    while running:
        clock.tick(60)
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if game_over and event.key == pygame.K_r:
                    player, enemy, score, game_over = reset_game()

        keys = pygame.key.get_pressed()

        if not game_over:
            if keys[pygame.K_LEFT] and player.x > 0:
                player.x -= PLAYER_SPEED
            if keys[pygame.K_RIGHT] and player.x < WIDTH - PLAYER_SIZE:
                player.x += PLAYER_SPEED
            if keys[pygame.K_UP] and player.y > 0:
                player.y -= PLAYER_SPEED
            if keys[pygame.K_DOWN] and player.y < HEIGHT - PLAYER_SIZE:
                player.y += PLAYER_SPEED

            enemy.y += ENEMY_SPEED

            if enemy.y > HEIGHT:
                enemy.y = 0
                enemy.x = random.randint(0, WIDTH - ENEMY_SIZE)
                score += 1

            if player.colliderect(enemy):
                game_over = True

        pygame.draw.rect(screen, (0, 150, 255), player)
        pygame.draw.rect(screen, (255, 50, 50), enemy)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        if game_over:
            draw_text("GAME OVER")
            restart_text = font.render("Press R to Restart", True, (255, 255, 255))
            screen.blit(restart_text, (WIDTH // 2 - 150, HEIGHT // 2 + 40))

        pygame.display.flip()

        if keys[pygame.K_ESCAPE]:
            running = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
