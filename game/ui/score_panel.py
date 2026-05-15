from configs.display import WINDOW_WIDTH

from configs.ui import (
    SCORE_PANEL_PATH,
    SCORE_PANEL_WIDTH_RATIO,
    SCORE_TEXT_OFFSET_X_RATIO,
    SCORE_TEXT_OFFSET_Y_RATIO,
)

from configs.colors import SCORE_TEXT_COLOR


class ScorePanel:
    """
    Displays the current score in a decorative panel.

    The panel is positioned in the top-right corner of the screen.
    """

    def __init__(self, screen, asset_manager, score_font):
        """
        Initialize the score panel.

        Args:
            screen (pygame.Surface): Target surface.
            asset_manager (AssetManager): Manager used to load images.
            score_font (pygame.font.Font): Font used to render the score.
        """
        self.screen = screen
        self.asset_manager = asset_manager
        self.score_font = score_font

        # Scaled panel image.
        self.panel = None

        # Rectangle used for positioning the panel.
        self.rect = None

        self.setup()

    def setup(self):
        """
        Load and scale the score panel image.
        """
        # Calculate panel width as a fraction of the window width.
        panel_width = int(WINDOW_WIDTH * SCORE_PANEL_WIDTH_RATIO)

        # Load the original panel image.
        original_panel = self.asset_manager.load_image(
            "score_panel",
            SCORE_PANEL_PATH,
        )

        # Preserve the original aspect ratio.
        panel_height = int(
            panel_width * original_panel.get_height() / original_panel.get_width()
        )

        # Create the scaled panel image.
        self.panel = self.asset_manager.scale_image(
            original_panel,
            (panel_width, panel_height),
        )

        # Position the panel in the top-right corner.
        self.rect = self.panel.get_rect(topright=(WINDOW_WIDTH, 0))

    def draw(self, score):
        """
        Draw the score panel and current score.

        Args:
            score (int): Current player score.
        """
        # Draw the panel background.
        self.screen.blit(self.panel, self.rect)

        # Render the score text.
        score_text = self.score_font.render(
            str(score),
            True,
            SCORE_TEXT_COLOR,
        )

        # Calculate score text position relative to the panel.
        text_x = self.rect.left + self.rect.width * SCORE_TEXT_OFFSET_X_RATIO

        text_y = self.rect.top + self.rect.height * SCORE_TEXT_OFFSET_Y_RATIO

        # Center the score text at the calculated position.
        score_text_rect = score_text.get_rect(center=(text_x, text_y))

        # Draw the score text.
        self.screen.blit(score_text, score_text_rect)
