from configs.display import WINDOW_WIDTH

from configs.ui import SCORE_PANEL_PATH


class ScorePanel:
    def __init__(self, screen, asset_manager, score_font):
        self.screen = screen
        self.asset_manager = asset_manager
        self.score_font = score_font

        self.panel = None
        self.rect = None

        self.setup()

    def setup(self):
        panel_width = int(WINDOW_WIDTH * 0.15)

        original_panel = self.asset_manager.load_image("score_panel", SCORE_PANEL_PATH)

        # calculation for proportion
        panel_height = int(
            panel_width * original_panel.get_height() / original_panel.get_width()
        )

        self.panel = self.asset_manager.scale_image(
            original_panel, (panel_width, panel_height)
        )

        self.rect = self.panel.get_rect(topright=(WINDOW_WIDTH, 0))

    def draw(self, score):
        self.screen.blit(self.panel, self.rect)

        score_text = self.score_font.render(str(score), True, (80, 55, 25))

        text_x = self.rect.left + self.rect.width * 0.75
        text_y = self.rect.top + self.rect.height * 0.65

        score_text_rect = score_text.get_rect(center=(text_x, text_y))

        self.screen.blit(score_text, score_text_rect)
