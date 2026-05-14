import pygame


class FontManager:
    def __init__(self):
        self.main_font = pygame.font.SysFont("Arial", 36)
        self.score_font = pygame.font.SysFont("Arial", 48, True)
        self.leaderboard_font = pygame.font.SysFont("Arial", 20)
        self.leaderboard_score_font = pygame.font.SysFont("Arial", 30, True)
        self.author_font = pygame.font.Font(None, 48)
