import pygame


class FontManager:
    """
    Creates and stores all fonts used in the game UI.

    Centralizing font initialization in one place makes it easier
    to maintain a consistent visual style and adjust font sizes.
    """
    def __init__(self):
        """
        Initialize all fonts used throughout the application.
        """
        # Main font used for menus and standard UI text.
        self.main_font = pygame.font.SysFont("Arial", 36)
        # Font used for displaying the current score.
        self.score_font = pygame.font.SysFont("Arial", 48, True)
        # Font used for leaderboard player names.
        self.leaderboard_font = pygame.font.SysFont("Arial", 20)
        # Font used for leaderboard scores.
        self.leaderboard_score_font = pygame.font.SysFont("Arial", 30, True)
        # Font used for the author name in the main menu.
        self.author_font = pygame.font.Font(None, 48)
