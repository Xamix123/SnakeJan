import pygame
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MAIN_THEME_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "common",
    "music",
    "main_theme.mp3"
)

LEADERBOARD_THEME_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "common",
    "music",
    "leaderboard_theme.mp3"
)

FOOD_EAT_SOUND_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "common",
    "sounds",
    "food_eat.wav"
)

GAME_OVER_SOUND_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "common",
    "sounds",
    "game_over.wav"
)

#UI

BUTTON_IMAGE_PATH = os.path.join(
    BASE_DIR, 
    "assets",
    "common",
    "images", 
    "ui",
    "buttons",
    "button.png"
)

BUTTON_HOVER_IMAGE_PATH = os.path.join(
    BASE_DIR, 
    "assets", 
    "common",
    "images", 
    "ui",
    "buttons",
    "button_hover.png"
)

LOGO_IMAGE_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "common",
    "images",
    "ui",
    "branding",
    "logo.png"
)

#Background Images

MENU_BACKGROUND_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "common",
    "images",
    "backgrounds",
    "main_menu_background.png"
)

APPLE_IMAGE_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "common",
    "images",
    "food",
    "apple.png"
)

SNAKE_HEAD_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "common",
    "images",
    "snake",
    "snake_head.png"
)

SNAKE_BODY_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "common",
    "images",
    "snake",
    "snake_body.png"
)

LEVEL_PANEL_PATH = os.path.join(
    BASE_DIR, "assets", "common", "images", "ui", "panels", "level_panel.png"
)

LEVELS = {
    "spring": {
        "panel": os.path.join(BASE_DIR, "assets", "levels", "spring", "images", "panels", "panel.png"),
        "panel_hover": os.path.join(BASE_DIR, "assets", "levels", "spring", "images", "panels", "panel_hover.png"),
        "background": os.path.join(BASE_DIR, "assets", "levels", "spring", "images", "backgrounds", "background.png")
    },
    "summer": {
        "panel": os.path.join(BASE_DIR, "assets", "levels", "summer", "images", "panels", "panel.png"),
        "panel_hover": os.path.join(BASE_DIR, "assets", "levels", "summer", "images", "panels", "panel_hover.png"),
        "background": os.path.join(BASE_DIR, "assets", "levels", "summer", "images", "backgrounds", "background.png"),
    },
    "autumn": {
        "panel": os.path.join(BASE_DIR, "assets", "levels", "autumn", "images", "panels", "panel.png"),
        "panel_hover": os.path.join(BASE_DIR, "assets", "levels", "autumn", "images", "panels", "panel_hover.png"),
        "background": os.path.join(BASE_DIR, "assets", "levels", "autumn", "images", "backgrounds", "background.png"),
    },
    "winter": {
        "panel": os.path.join(BASE_DIR, "assets", "levels", "winter", "images", "panels", "panel.png"),
        "panel_hover": os.path.join(BASE_DIR, "assets", "levels", "winter", "images", "panels", "panel_hover.png"),
        "background": os.path.join(BASE_DIR, "assets", "levels", "winter", "images", "backgrounds", "background.png"),
    }
}

GAME_OVER_PANEL_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "common",
    "images",
    "ui",
    "panels",
    "game_over_panel.png"
)

LEADERBOARD_PANEL_PATH = os.path.join(
    BASE_DIR, "assets", "common", "images", "ui", "leaderboard", "leaderboard.png"
)

LEADERBOARD_TAB_PATH = os.path.join(
    BASE_DIR, "assets", "common", "images", "ui", "leaderboard", "leaderboard_tab.png"
)

LEADERBOARD_TAB_HOVER_PATH = os.path.join(
    BASE_DIR, "assets", "common", "images", "ui", "leaderboard", "leaderboard_tab_hover.png"
)

LEADERBOARD_TAB_ACTIVE_PATH = os.path.join(
    BASE_DIR, "assets", "common", "images", "ui", "leaderboard", "leaderboard_tab_active.png"
)

AUTHOR = "Тур Ян ІПЗ-113к9";


pygame.init()

info = pygame.display.Info()

WINDOW_WIDTH = info.current_w
WINDOW_HEIGHT = info.current_h

GRID_COLUMNS = 40
GRID_ROWS = 25

CELL_SIZE = min(
    WINDOW_WIDTH // GRID_COLUMNS,
    WINDOW_HEIGHT // GRID_ROWS
)

GAME_WIDTH = GRID_COLUMNS * CELL_SIZE
GAME_HEIGHT = GRID_ROWS * CELL_SIZE

OFFSET_X = (WINDOW_WIDTH - GAME_WIDTH) // 2
OFFSET_Y = (WINDOW_HEIGHT - GAME_HEIGHT) // 2

FPS = 60
SNAKE_SPEED = 10

BACKGROUND_COLOR = (245, 245, 245)
GRID_COLOR = (180, 180, 180)