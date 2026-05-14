import pygame

from configs.display import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)

from configs.ui import GAME_OVER_PANEL_PATH


class GameOverOverlay:
    def __init__(self):
        self.image = pygame.image.load(GAME_OVER_PANEL_PATH).convert_alpha()

        self.rect = self.image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

        self.overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, 150))

    def draw(self, screen):
        screen.blit(self.overlay, (0, 0))
        screen.blit(self.image, self.rect)
