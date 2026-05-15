from configs.display import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)

from configs.ui import (
    AUTHOR,
    LOGO_IMAGE_PATH,
    BUTTON_IMAGE_PATH,
    BUTTON_HOVER_IMAGE_PATH,
    MENU_LOGO_WIDTH_RATIO,
    MENU_LOGO_CENTER_Y_RATIO,
    MENU_BUTTON_WIDTH_RATIO,
    MENU_BUTTON_HEIGHT_RATIO,
    MENU_BUTTON_START_OFFSET_Y,
    MENU_BUTTON_GAP,
    MENU_AUTHOR_MARGIN,
)

from configs.colors import AUTHOR_TEXT_COLOR
from configs.visual import MENU_BACKGROUND_PATH

from game.ui.button import Button


class Menu:
    """
    Represents the main menu screen.

    The menu contains:
    - background image;
    - game logo;
    - Play, Leaderboard and Exit buttons;
    - author signature.
    """

    def __init__(self, screen, asset_manager, main_font, author_font):
        """
        Initialize the main menu.

        Args:
            screen (pygame.Surface): Target surface.
            asset_manager (AssetManager): Manager used to load images.
            main_font (pygame.font.Font): Font for buttons.
            author_font (pygame.font.Font): Font for author text.
        """
        self.screen = screen
        self.asset_manager = asset_manager
        self.main_font = main_font
        self.author_font = author_font

        self.setup()

    def setup(self):
        """
        Load all menu assets and create buttons.
        """
        # Load and scale background image.
        self.background = self.asset_manager.load_scaled_image(
            "menu_background",
            MENU_BACKGROUND_PATH,
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            alpha=False,
        )

        # Load logo image.
        logo = self.asset_manager.load_image(
            "logo",
            LOGO_IMAGE_PATH,
        )

        # Calculate logo size.
        logo_width = int(WINDOW_WIDTH * MENU_LOGO_WIDTH_RATIO)

        logo_height = int(logo_width * logo.get_height() / logo.get_width())

        # Scale logo.
        self.logo_image = self.asset_manager.scale_image(
            logo,
            (logo_width, logo_height),
        )

        # Center logo.
        self.logo_rect = self.logo_image.get_rect(
            center=(
                WINDOW_WIDTH // 2,
                int(WINDOW_HEIGHT * MENU_LOGO_CENTER_Y_RATIO),
            )
        )

        # Load button images.
        self.button_image = self.asset_manager.load_image(
            "button",
            BUTTON_IMAGE_PATH,
        )

        self.button_hover_image = self.asset_manager.load_image(
            "button_hover",
            BUTTON_HOVER_IMAGE_PATH,
        )

        self.create_buttons()

    def create_buttons(self):
        """
        Create menu buttons.
        """
        button_width = int(WINDOW_WIDTH * MENU_BUTTON_WIDTH_RATIO)

        button_height = int(WINDOW_HEIGHT * MENU_BUTTON_HEIGHT_RATIO)

        center_x = WINDOW_WIDTH // 2

        start_y = WINDOW_HEIGHT // 2 + MENU_BUTTON_START_OFFSET_Y

        gap = button_height + MENU_BUTTON_GAP

        self.buttons = {
            "play": Button(
                "Play",
                center_x,
                start_y,
                button_width,
                button_height,
                self.main_font,
                self.button_image,
                self.button_hover_image,
            ),
            "leaderboard": Button(
                "Leaderboard",
                center_x,
                start_y + gap,
                button_width,
                button_height,
                self.main_font,
                self.button_image,
                self.button_hover_image,
            ),
            "exit": Button(
                "Exit",
                center_x,
                start_y + gap * 2,
                button_width,
                button_height,
                self.main_font,
                self.button_image,
                self.button_hover_image,
            ),
        }

    def draw(self):
        """
        Draw the menu screen.
        """
        # Draw background and logo.
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.logo_image, self.logo_rect)

        # Draw buttons.
        for button in self.buttons.values():
            button.draw(self.screen)

        # Render author text.
        author_text = self.author_font.render(
            f"Created by {AUTHOR}",
            True,
            AUTHOR_TEXT_COLOR,
        )

        # Position author text in the bottom-right corner.
        author_rect = author_text.get_rect(
            bottomright=(
                WINDOW_WIDTH - MENU_AUTHOR_MARGIN,
                WINDOW_HEIGHT - MENU_AUTHOR_MARGIN,
            )
        )

        self.screen.blit(author_text, author_rect)

    def handle_event(self, event):
        """
        Handle menu button clicks.

        Args:
            event (pygame.event.Event): Pygame event.

        Returns:
            str | None:
                Next game state or None.
        """
        if self.buttons["play"].is_clicked(event):
            return "level_select"

        if self.buttons["leaderboard"].is_clicked(event):
            return "leaderboard"

        if self.buttons["exit"].is_clicked(event):
            return "exit"

        return None
