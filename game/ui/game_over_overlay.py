import pygame

from configs.display import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)

from configs.ui import GAME_OVER_PANEL_PATH

from configs.colors import OVERLAY_COLOR


class GameOverOverlay:
    """
    Displays the game over overlay.

    The overlay consists of:
    - a semi-transparent dark background;
    - a centered game over panel image.
    """
    def __init__(self):
        """
        Initialize the game over overlay.
        """
        # Load the game over panel image.
        self.image = pygame.image.load(GAME_OVER_PANEL_PATH).convert_alpha()

        # Center the panel on the screen.
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

        # Create a semi-transparent dark overlay.
        self.overlay = pygame.Surface(
            (WINDOW_WIDTH, WINDOW_HEIGHT), 
            pygame.SRCALPHA
        )
        # RGBA color: black with 150 alpha.
        self.overlay.fill(OVERLAY_COLOR)

    def draw(self, screen):
        """
        Draw the game over overlay.

        Args:
            screen (pygame.Surface): Target surface.
        """
        # Draw the darkened background.
        screen.blit(self.overlay, (0, 0))
        # Draw the centered game over panel.
        screen.blit(self.image, self.rect)
