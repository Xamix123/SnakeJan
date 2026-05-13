import pygame

from settings import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    LEADERBOARD_PANEL_PATH,
    LEADERBOARD_TAB_PATH,
    LEADERBOARD_TAB_HOVER_PATH,
    LEADERBOARD_TAB_ACTIVE_PATH,
)

 
class Leaderboard:
    def __init__(
        self,
        screen,
        asset_manager,
        menu_background,
        leaderboard_font,
        leaderboard_score_font,
        leaderboard_manager
    ):
        self.screen = screen
        self.asset_manager = asset_manager
        self.menu_background = menu_background
        self.leaderboard_font = leaderboard_font
        self.leaderboard_score_font = leaderboard_score_font
        self.leaderboard_manager = leaderboard_manager

        self.active_tab = "spring"

        self.tabs = ["spring", "summer", "autumn", "winter", "random"]

        self.tab_names = {
            "spring": "Spring",
            "summer": "Summer",
            "autumn": "Autumn",
            "winter": "Winter",
            "random": "Random",
        }

        self.tab_rects = {}

        self.setup()

    def setup(self):
        self.panel = self.asset_manager.load_image(
            "leaderboard_panel",
            LEADERBOARD_PANEL_PATH
        )

        panel_width = int(WINDOW_WIDTH * 0.65)
        panel_height = int(
            panel_width * self.panel.get_height() / self.panel.get_width()
        )

        self.panel = self.asset_manager.scale_image(
            self.panel,
            (panel_width, panel_height)
        )

        self.rect = self.panel.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        )

        self.tab = self.asset_manager.load_image(
            "leaderboard_tab",
            LEADERBOARD_TAB_PATH
        )

        self.tab_hover = self.asset_manager.load_image(
            "leaderboard_tab_hover",
            LEADERBOARD_TAB_HOVER_PATH
        )

        self.tab_active = self.asset_manager.load_image(
            "leaderboard_tab_active",
            LEADERBOARD_TAB_ACTIVE_PATH
        )

    def draw(self):
        self.screen.blit(self.menu_background, (0, 0))
        self.screen.blit(self.panel, self.rect)

        self.draw_tabs()
        self.draw_scores()

    def draw_tabs(self):
        self.tab_rects = {}

        panel = self.rect
        mouse_pos = pygame.mouse.get_pos()

        tab_count = len(self.tabs)
        tab_width = int(panel.width * 0.12)
        tab_height = int(tab_width * self.tab.get_height() / self.tab.get_width())
        tab_gap = int(panel.width * 0.010)

        total_tabs_width = tab_count * tab_width + (tab_count - 1) * tab_gap
        start_x = panel.centerx - total_tabs_width // 2
        start_y = panel.top + int(panel.height * 0.25)

        for index, level_key in enumerate(self.tabs):
            x = start_x + index * (tab_width + tab_gap)
            y = start_y

            rect = pygame.Rect(x, y, tab_width, tab_height)
            self.tab_rects[level_key] = rect

            if level_key == self.active_tab:
                tab_image = self.tab_active
                text_color = (255, 220, 90)
            elif rect.collidepoint(mouse_pos):
                tab_image = self.tab_hover
                text_color = (80, 45, 15)
            else:
                tab_image = self.tab
                text_color = (60, 35, 15)

            tab_image = self.asset_manager.scale_image(
                tab_image,
                (tab_width, tab_height)
            )

            self.screen.blit(tab_image, rect)

            text = self.leaderboard_font.render(
                self.tab_names[level_key],
                True,
                text_color
            )

            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)

    def draw_scores(self):
        panel = self.rect
        scores = self.leaderboard_manager.get_scores(self.active_tab)
        #TODO MAKE CONSTANTS 
        row_count = 5
        
        table_left = panel.left + int(panel.width * 0.15)
        table_right = panel.left + int(panel.width)

        row_y = panel.top + int(panel.height * 0.35) 
        row_height = int(panel.height * 0.105)
        name_x = table_left + int(panel.width * 0.05)
        score_x = table_right - int(panel.width * 0.20)

        text_color = (70, 45, 20) # TODO COLOR CONSTANT

        for index in range(row_count):
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
                row_height
            )

            name_text = self.leaderboard_score_font.render(
                name,
                True,
                text_color
            )

            score_text = self.leaderboard_score_font.render(
                score,
                True,
                text_color
            )
            name_rect = name_text.get_rect(
                midleft=(name_x, row_rect.centery)
            )

            score_rect = score_text.get_rect(
                midright=(score_x, row_rect.centery)
            )

            self.screen.blit(name_text, name_rect)
            self.screen.blit(score_text, score_rect)


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for level_key, rect in self.tab_rects.items():
                if rect.collidepoint(event.pos):
                    self.active_tab = level_key