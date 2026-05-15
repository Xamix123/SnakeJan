import pygame

from configs.display import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)

from configs.ui import (
    LEADERBOARD_PANEL_PATH,
    LEADERBOARD_TAB_PATH,
    LEADERBOARD_TAB_HOVER_PATH,
    LEADERBOARD_TAB_ACTIVE_PATH,
)

from configs.colors import (
    LEADERBOARD_ACTIVE_TAB_TEXT_COLOR,
    LEADERBOARD_HOVER_TAB_TEXT_COLOR,
    LEADERBOARD_TAB_TEXT_COLOR,
    LEADERBOARD_SCORE_TEXT_COLOR,
)

from configs.ui import (
    LEADERBOARD_PANEL_WIDTH_RATIO,
    LEADERBOARD_TAB_WIDTH_RATIO,
    LEADERBOARD_TAB_GAP_RATIO,
    LEADERBOARD_TAB_OFFSET_Y_RATIO,
    LEADERBOARD_TABLE_LEFT_RATIO,
    LEADERBOARD_TABLE_RIGHT_RATIO,
    LEADERBOARD_TABLE_TOP_RATIO,
    LEADERBOARD_ROW_HEIGHT_RATIO,
    LEADERBOARD_NAME_OFFSET_X_RATIO,
    LEADERBOARD_SCORE_OFFSET_X_RATIO,
    LEADERBOARD_ROW_COUNT,
)


class Leaderboard:
    """
    Displays the leaderboard screen.

    The screen contains:
    - decorative panel;
    - tabs for each level;
    - top five scores for the selected level.
    """

    def __init__(
        self,
        screen,
        asset_manager,
        menu_background,
        leaderboard_font,
        leaderboard_score_font,
        leaderboard_manager,
    ):
        """
        Initialize the leaderboard screen.

        Args:
            screen (pygame.Surface): Target surface.
            asset_manager (AssetManager): Manager used to load images.
            menu_background (pygame.Surface): Background image.
            leaderboard_font (pygame.font.Font): Font for tab labels.
            leaderboard_score_font (pygame.font.Font): Font for score rows.
            leaderboard_manager (LeaderboardManager):
                Source of leaderboard data.
        """
        self.screen = screen
        self.asset_manager = asset_manager
        self.menu_background = menu_background
        self.leaderboard_font = leaderboard_font
        self.leaderboard_score_font = leaderboard_score_font
        self.leaderboard_manager = leaderboard_manager

        # Currently selected tab.
        self.active_tab = "spring"

        # Available leaderboard tabs.
        self.tabs = [
            "spring",
            "summer",
            "autumn",
            "winter",
            "random",
        ]

        # Human-readable tab titles.
        self.tab_names = {
            "spring": "Spring",
            "summer": "Summer",
            "autumn": "Autumn",
            "winter": "Winter",
            "random": "Random",
        }

        # Rectangles used for click detection.
        self.tab_rects = {}

        self.setup()

    def setup(self):
        """
        Load and prepare leaderboard assets.
        """
        self.panel = self.asset_manager.load_image(
            "leaderboard_panel",
            LEADERBOARD_PANEL_PATH,
        )

        panel_width = int(WINDOW_WIDTH * LEADERBOARD_PANEL_WIDTH_RATIO)

        panel_height = int(
            panel_width * self.panel.get_height() / self.panel.get_width()
        )

        self.panel = self.asset_manager.scale_image(
            self.panel,
            (panel_width, panel_height),
        )

        self.rect = self.panel.get_rect(
            center=(
                WINDOW_WIDTH // 2,
                WINDOW_HEIGHT // 2,
            )
        )

        # Load tab images.
        self.tab = self.asset_manager.load_image(
            "leaderboard_tab",
            LEADERBOARD_TAB_PATH,
        )

        self.tab_hover = self.asset_manager.load_image(
            "leaderboard_tab_hover",
            LEADERBOARD_TAB_HOVER_PATH,
        )

        self.tab_active = self.asset_manager.load_image(
            "leaderboard_tab_active",
            LEADERBOARD_TAB_ACTIVE_PATH,
        )

    def draw(self):
        """
        Draw the leaderboard screen.
        """
        self.screen.blit(self.menu_background, (0, 0))
        self.screen.blit(self.panel, self.rect)

        self.draw_tabs()
        self.draw_scores()

    def draw_tabs(self):
        """
        Draw leaderboard tabs.
        """
        self.tab_rects = {}

        panel = self.rect
        mouse_pos = pygame.mouse.get_pos()

        tab_count = len(self.tabs)

        tab_width = int(panel.width * LEADERBOARD_TAB_WIDTH_RATIO)

        tab_height = int(tab_width * self.tab.get_height() / self.tab.get_width())

        tab_gap = int(panel.width * LEADERBOARD_TAB_GAP_RATIO)

        total_tabs_width = tab_count * tab_width + (tab_count - 1) * tab_gap

        start_x = panel.centerx - total_tabs_width // 2

        start_y = panel.top + int(panel.height * LEADERBOARD_TAB_OFFSET_Y_RATIO)

        for index, level_key in enumerate(self.tabs):
            x = start_x + index * (tab_width + tab_gap)
            y = start_y

            rect = pygame.Rect(
                x,
                y,
                tab_width,
                tab_height,
            )

            self.tab_rects[level_key] = rect

            if level_key == self.active_tab:
                tab_image = self.tab_active
                text_color = LEADERBOARD_ACTIVE_TAB_TEXT_COLOR
            elif rect.collidepoint(mouse_pos):
                tab_image = self.tab_hover
                text_color = LEADERBOARD_HOVER_TAB_TEXT_COLOR
            else:
                tab_image = self.tab
                text_color = LEADERBOARD_TAB_TEXT_COLOR

            tab_image = self.asset_manager.scale_image(
                tab_image,
                (tab_width, tab_height),
            )

            self.screen.blit(tab_image, rect)

            text = self.leaderboard_font.render(
                self.tab_names[level_key],
                True,
                text_color,
            )

            text_rect = text.get_rect(center=rect.center)

            self.screen.blit(text, text_rect)

    def draw_scores(self):
        """
        Draw top scores for the selected tab.
        """
        panel = self.rect
        scores = self.leaderboard_manager.get_scores(self.active_tab)

        table_left = panel.left + int(panel.width * LEADERBOARD_TABLE_LEFT_RATIO)

        table_right = panel.left + int(panel.width * LEADERBOARD_TABLE_RIGHT_RATIO)

        row_y = panel.top + int(panel.height * LEADERBOARD_TABLE_TOP_RATIO)

        row_height = int(panel.height * LEADERBOARD_ROW_HEIGHT_RATIO)

        name_x = table_left + int(panel.width * LEADERBOARD_NAME_OFFSET_X_RATIO)

        score_x = table_right - int(panel.width * LEADERBOARD_SCORE_OFFSET_X_RATIO)

        for index in range(LEADERBOARD_ROW_COUNT):
            if index < len(scores):
                record = scores[index]
                name = record["name"]
                score = str(record["score"])
            else:
                name = "---"
                score = "0"

            y = row_y + index * row_height

            row_rect = pygame.Rect(
                table_left,
                y,
                table_right - table_left,
                row_height,
            )

            name_text = self.leaderboard_score_font.render(
                name,
                True,
                LEADERBOARD_SCORE_TEXT_COLOR,
            )

            score_text = self.leaderboard_score_font.render(
                score,
                True,
                LEADERBOARD_SCORE_TEXT_COLOR,
            )

            name_rect = name_text.get_rect(midleft=(name_x, row_rect.centery))

            score_rect = score_text.get_rect(midright=(score_x, row_rect.centery))

            self.screen.blit(name_text, name_rect)
            self.screen.blit(score_text, score_rect)

    def handle_event(self, event):
        """
        Handle tab clicks.

        Args:
            event (pygame.event.Event): Pygame event.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for level_key, rect in self.tab_rects.items():
                if rect.collidepoint(event.pos):
                    self.active_tab = level_key
