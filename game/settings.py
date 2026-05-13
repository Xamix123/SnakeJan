import pygame
import os

#music and sounds section
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

DEFAULT_MUSIC_VOLUME = 0.3
DEFAULT_SOUND_VOLUME = 0.5
MUSIC_LOOP = -1

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

SNAKE_HEAD_OPEN_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "common",
    "images",
    "snake",
    "snake_head_mouth_open.png"
)

MOUTH_OPEN_DURATION = 1000  # miliseconds

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
        "background": os.path.join(BASE_DIR, "assets", "levels", "spring", "images", "backgrounds", "background.png"),
        "food": os.path.join(BASE_DIR, "assets", "common", "images", "food", "apple.png"),
        "obstacles": []
    },
    "summer": {
        "panel": os.path.join(BASE_DIR, "assets", "levels", "summer", "images", "panels", "panel.png"),
        "panel_hover": os.path.join(BASE_DIR, "assets", "levels", "summer", "images", "panels", "panel_hover.png"),
        "background": os.path.join(BASE_DIR, "assets", "levels", "summer", "images", "backgrounds", "background.png"),
        "food": os.path.join(BASE_DIR, "assets", "common", "images", "food", "apple.png"),
        "obstacles": [
            {
                "type": "rock",
                "image": os.path.join(
                    BASE_DIR,
                    "assets",
                    "common",
                    "images",
                    "obstacles",
                    "rock.png"
                ),
                "position": [12, 6],
                "size": 3
            },
            {
                "type": "rock",
                "image": os.path.join(
                    BASE_DIR,
                    "assets",
                    "common",
                    "images",
                    "obstacles",
                    "rock_with_grass.png"
                ),
                "position": [10, 15],
                "size": 4
            },
            {
                "type": "rock",
                "image": os.path.join(
                    BASE_DIR,
                    "assets",
                    "common",
                    "images",
                    "obstacles",
                    "rock.png"
                ),
                "position": [4, 18],
                "size": 3
            },
            {
                "type": "tree",
                "image": os.path.join(
                    BASE_DIR,
                    "assets",
                    "common",
                    "images",
                    "obstacles",
                    "tree.png"
                ),
                "position": [24, 10],
                "size": 6
            },
        ]
    },
    "autumn": {
        "panel": os.path.join(BASE_DIR, "assets", "levels", "autumn", "images", "panels", "panel.png"),
        "panel_hover": os.path.join(BASE_DIR, "assets", "levels", "autumn", "images", "panels", "panel_hover.png"),
        "background": os.path.join(BASE_DIR, "assets", "levels", "autumn", "images", "backgrounds", "background.png"),
        "food": os.path.join(BASE_DIR, "assets", "common", "images", "food", "apple.png"),
        "play_area": {
            "x_min": 2,
            "x_max": 39,
            "y_min": 2,
            "y_max": 21
        },
        "obstacles": [
            {
                "type": "tree",
                "image": os.path.join(
                    BASE_DIR,
                    "assets",
                    "common",
                    "images",
                    "obstacles",
                    "autumn_tree.png"
                ),
                "position": [28, 13],
                "size": 8
            }
        ]
    },
    "winter": {
        "panel": os.path.join(BASE_DIR, "assets", "levels", "winter", "images", "panels", "panel.png"),
        "panel_hover": os.path.join(BASE_DIR, "assets", "levels", "winter", "images", "panels", "panel_hover.png"),
        "background": os.path.join(BASE_DIR, "assets", "levels", "winter", "images", "backgrounds", "background.png"),
        "food": os.path.join(BASE_DIR, "assets", "common", "images", "food", "orange.png"),
        "obstacles": [
            {
                "type": "tree",
                "image": os.path.join(
                    BASE_DIR,
                    "assets",
                    "common",
                    "images",
                    "obstacles",
                    "snowman.png"
                ),
                "position": [9, 7],
                "size": 4
            },
            {
                "type": "tree",
                "image": os.path.join(
                    BASE_DIR,
                    "assets",
                    "common",
                    "images",
                    "obstacles",
                    "snowman.png"
                ),
                "position": [18, 7],
                "size": 4
            },
            {
                "type": "tree",
                "image": os.path.join(
                    BASE_DIR,
                    "assets",
                    "common",
                    "images",
                    "obstacles",
                    "snowman.png"
                ),
                "position": [27, 7],
                "size": 4
            },
            {
                "type": "tree",
                "image": os.path.join(
                    BASE_DIR,
                    "assets",
                    "common",
                    "images",
                    "obstacles",
                    "snowman.png"
                ),
                "position": [9, 15],
                "size": 4
            },
            {
                "type": "tree",
                "image": os.path.join(
                    BASE_DIR,
                    "assets",
                    "common",
                    "images",
                    "obstacles",
                    "snowman.png"
                ),
                "position": [18, 15],
                "size": 4
            },
            {
                "type": "tree",
                "image": os.path.join(
                    BASE_DIR,
                    "assets",
                    "common",
                    "images",
                    "obstacles",
                    "snowman.png"
                ),
                "position": [27, 15],
                "size": 4
            }
        ]
    }
}

SCORE_PANEL_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "common",
    "images",
    "ui",
    "panels",
    "score_panel.png"
)

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

ROCK_OBSTACLE_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "common",
    "images",
    "obstacles",
    "rock.png"
)

AUTHOR = "Тур Ян ІПЗ-113к9";


pygame.init()

info = pygame.display.Info()

WINDOW_WIDTH = info.current_w
WINDOW_HEIGHT = info.current_h

CELL_SIZE = 92

GRID_COLUMNS = WINDOW_WIDTH // CELL_SIZE
GRID_ROWS = WINDOW_HEIGHT // CELL_SIZE

OFFSET_X = (WINDOW_WIDTH - GRID_COLUMNS * CELL_SIZE) // 2
OFFSET_Y = (WINDOW_HEIGHT - GRID_ROWS * CELL_SIZE) // 2

GAME_WIDTH = GRID_COLUMNS * CELL_SIZE
GAME_HEIGHT = GRID_ROWS * CELL_SIZE

FPS = 60
SNAKE_SPEED = 10

BACKGROUND_COLOR = (245, 245, 245)
GRID_COLOR = (180, 180, 180)

SCORE_POINT = 10