from enum import Enum


class GameState(Enum):
    """
    Defines all possible states of the game.

    The game uses a finite state machine to switch between
    different screens and modes.
    """

    # Main menu screen.
    MENU = "menu"

    # Active gameplay state.
    PLAYING = "playing"

    # Level selection screen.
    LEVEL_SELECT = "level_select"

    # Leaderboard screen.
    LEADERBOARD = "leaderboard"

    # Player name input screen shown after a high score.
    ENTER_NAME = "enter_name"