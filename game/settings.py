import pygame
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MUSIC_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "music",
    "MainTheme.mp3"
)

#UI

BUTTON_IMAGE_PATH = os.path.join(
    BASE_DIR, 
    "assets", 
    "images", 
    "ui", 
    "button.png"
)

BUTTON_HOVER_IMAGE_PATH = os.path.join(
    BASE_DIR, 
    "assets", 
    "images", 
    "ui", 
    "button_hover.png"
)

LOGO_IMAGE_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "images",
    "ui",
    "logo.png"
)

#Background Images

MENU_BACKGROUND_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "images",
    "background",
    "main_menu_background.png"
)

SUMMER_BACKGROUND_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "images",
    "background",
    "background_s1.png"
)

AUTUMN_BACKGROUND_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "images",
    "background",
    "background_s2.png"
)

APPLE_IMAGE_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "images",
    "apple.png"
)

SNAKE_HEAD_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "images",
    "snake",
    "snake_head.png"
)

SNAKE_BODY_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "images",
    "snake",
    "snake_body.png"
)

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