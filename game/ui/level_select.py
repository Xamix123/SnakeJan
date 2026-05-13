from settings import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    LEVEL_PANEL_PATH,
    LEVELS,
)

from ui.level_button import LevelButton

class LevelSelect:
    def __init__(self, screen, asset_manager, menu_background):
        self.screen = screen
        self.asset_manager = asset_manager
        self.menu_background = menu_background

        self.level_buttons = {}

        self.setup()

    def setup(self):
        panel_width = int(WINDOW_WIDTH * 0.75)
        panel_height = int(
            panel_width * WINDOW_HEIGHT / WINDOW_WIDTH
        )

        self.panel = self.asset_manager.load_scaled_image(
            "level_panel",
            LEVEL_PANEL_PATH,
            (panel_width, panel_height)
        )

        self.panel_rect = self.panel.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        )

        level_size = panel_width // 6
        gap = 40

        levels = ["spring", "summer", "autumn", "winter"]

        total_width = level_size * len(levels) + gap * (len(levels) - 1)

        start_x = self.panel_rect.centerx - total_width // 2
        start_y = self.panel_rect.centery - level_size // 2

        for index, level_key in enumerate(levels):
            image = self.asset_manager.load_image(
                f"{level_key}_panel",
                LEVELS[level_key]["panel"]
            )

            hover_image = self.asset_manager.load_image(
                f"{level_key}_panel_hover",
                LEVELS[level_key]["panel_hover"]
            )

            x = start_x + index * (level_size + gap)
            y = start_y

            self.level_buttons[level_key] = LevelButton(
                level_key,
                image,
                hover_image,
                x,
                y,
                level_size
            )

    def draw(self):
        self.screen.blit(self.menu_background, (0, 0))
        self.screen.blit(self.panel, self.panel_rect)

        for button in self.level_buttons.values():
            button.draw(self.screen)

    def handle_event(self, event):
        for level_key, button in self.level_buttons.items():
            if button.is_clicked(event):
                return level_key

        return None