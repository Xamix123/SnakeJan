from .paths import asset_path

AUTHOR = "Тур Ян ІПЗ-113к9"

BUTTON_IMAGE_PATH = asset_path("common", "images", "ui", "buttons", "button.png")

BUTTON_HOVER_IMAGE_PATH = asset_path(
    "common", "images", "ui", "buttons", "button_hover.png"
)

LOGO_IMAGE_PATH = asset_path("common", "images", "ui", "branding", "logo.png")

LEVEL_PANEL_PATH = asset_path("common", "images", "ui", "panels", "level_panel.png")

SCORE_PANEL_PATH = asset_path("common", "images", "ui", "panels", "score_panel.png")

GAME_OVER_PANEL_PATH = asset_path(
    "common", "images", "ui", "panels", "game_over_panel.png"
)

LEADERBOARD_PANEL_PATH = asset_path(
    "common", "images", "ui", "leaderboard", "leaderboard.png"
)

LEADERBOARD_TAB_PATH = asset_path(
    "common", "images", "ui", "leaderboard", "leaderboard_tab.png"
)

LEADERBOARD_TAB_HOVER_PATH = asset_path(
    "common", "images", "ui", "leaderboard", "leaderboard_tab_hover.png"
)

LEADERBOARD_TAB_ACTIVE_PATH = asset_path(
    "common", "images", "ui", "leaderboard", "leaderboard_tab_active.png"
)

#NAME INPUT CONSTANTS

NAME_INPUT_MAX_LENGTH = 10

NAME_INPUT_TITLE_OFFSET_Y = -100
NAME_INPUT_SUBTITLE_OFFSET_Y = -40
NAME_INPUT_VALUE_OFFSET_Y = 20
NAME_INPUT_HINT_OFFSET_Y = 80

NAME_INPUT_CURSOR_BLINK_INTERVAL = 1000
NAME_INPUT_CURSOR_VISIBLE_TIME = 500

DEFAULT_PLAYER_NAME = "Player"

#SCORE PANEL CONSTANTS

SCORE_PANEL_WIDTH_RATIO = 0.15

SCORE_TEXT_OFFSET_X_RATIO = 0.75
SCORE_TEXT_OFFSET_Y_RATIO = 0.65

SCORE_PANEL_TOP_RIGHT = (0, 0)

# Menu layout

MENU_LOGO_WIDTH_RATIO = 1 / 3
MENU_LOGO_CENTER_Y_RATIO = 1 / 5

MENU_BUTTON_WIDTH_RATIO = 1 / 4
MENU_BUTTON_HEIGHT_RATIO = 1 / 8

MENU_BUTTON_START_OFFSET_Y = -40
MENU_BUTTON_GAP = 25

MENU_AUTHOR_MARGIN = 20

# Leaderboard panel
LEADERBOARD_PANEL_WIDTH_RATIO = 0.65

# Tabs
LEADERBOARD_TAB_WIDTH_RATIO = 0.12
LEADERBOARD_TAB_GAP_RATIO = 0.010
LEADERBOARD_TAB_OFFSET_Y_RATIO = 0.25

# Score table
LEADERBOARD_ROW_COUNT = 5

LEADERBOARD_TABLE_LEFT_RATIO = 0.15
LEADERBOARD_TABLE_RIGHT_RATIO = 1.00
LEADERBOARD_TABLE_TOP_RATIO = 0.35
LEADERBOARD_ROW_HEIGHT_RATIO = 0.105

LEADERBOARD_NAME_OFFSET_X_RATIO = 0.05
LEADERBOARD_SCORE_OFFSET_X_RATIO = 0.20
