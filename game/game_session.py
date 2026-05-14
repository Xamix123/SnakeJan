class GameSession:
    def __init__(self):
        self.reset()

    def reset(self):
        self.score = 0
        self.move_timer = 0
        self.game_over = False
