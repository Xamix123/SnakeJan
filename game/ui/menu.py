from settings import (
    AUTHOR,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    LOGO_IMAGE_PATH,
    MENU_BACKGROUND_PATH,
    BUTTON_IMAGE_PATH,
    BUTTON_HOVER_IMAGE_PATH,
)

from ui.button import Button


class Menu:
    def __init__(self, screen, asset_manager, main_font, author_font):
        self.screen = screen
        self.asset_manager = asset_manager
        self.main_font = main_font
        self.author_font = author_font

        self.setup()

    def setup(self):
        self.background = self.asset_manager.load_scaled_image(
            "menu_background",
            MENU_BACKGROUND_PATH,
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            alpha=False
        )

        logo = self.asset_manager.load_image("logo", LOGO_IMAGE_PATH)

        logo_width = WINDOW_WIDTH // 3
        logo_height = int(logo_width * logo.get_height() / logo.get_width())

        self.logo_image = self.asset_manager.scale_image(
            logo,
            (logo_width, logo_height)
        )

        self.logo_rect = self.logo_image.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 5)
        )

        self.button_image = self.asset_manager.load_image(
            "button",
            BUTTON_IMAGE_PATH
        )

        self.button_hover_image = self.asset_manager.load_image(
            "button_hover",
            BUTTON_HOVER_IMAGE_PATH
        )

        self.create_buttons()

    def create_buttons(self):
        button_width = WINDOW_WIDTH // 4
        button_height = WINDOW_HEIGHT // 8

        center_x = WINDOW_WIDTH // 2
        start_y = WINDOW_HEIGHT // 2 - 40
        gap = button_height + 25

        self.buttons = {
            "play": Button(
                "Play",
                center_x,
                start_y,
                button_width,
                button_height,
                self.main_font,
                self.button_image,
                self.button_hover_image
            ),
            "leaderboard": Button(
                "Leaderboard",
                center_x,
                start_y + gap,
                button_width,
                button_height,
                self.main_font,
                self.button_image,
                self.button_hover_image
            ),
            "exit": Button(
                "Exit",
                center_x,
                start_y + gap * 2,
                button_width,
                button_height,
                self.main_font,
                self.button_image,
                self.button_hover_image
            ),
        }

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.logo_image, self.logo_rect)

        for button in self.buttons.values():
            button.draw(self.screen)

        author_text = self.author_font.render(
            f"Created by {AUTHOR}",
            True,
            (255, 255, 255)
        )

        author_rect = author_text.get_rect(
            bottomright=(WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20)
        )

        self.screen.blit(author_text, author_rect)

    def handle_event(self, event):
        if self.buttons["play"].is_clicked(event):
            return "level_select"

        if self.buttons["leaderboard"].is_clicked(event):
            return "leaderboard"

        if self.buttons["exit"].is_clicked(event):
            return "exit"

        return None