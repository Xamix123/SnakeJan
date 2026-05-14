from enum import Enum


class GameState(Enum):
    MENU = "menu"
    PLAYING = "playing"
    LEVEL_SELECT = "level_select"
    LEADERBOARD = "leaderboard"
    ENTER_NAME = "enter_name"
