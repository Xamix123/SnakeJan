class GameSession:
    """
    Stores mutable data for the current game session.

    The session contains:
    - current score;
    - movement timer;
    - game over flag.

    This class is used to keep all runtime state in one place
    and makes restarting the game easier.
    """

    def __init__(self):
        """
        Initialize a new game session.
        """
        self.reset()

    def reset(self):
        """
        Reset the session to its initial state.
        """
        # Current player score.
        self.score = 0

        # Accumulated time used to control snake movement.
        self.move_timer = 0

        # Indicates whether the game has ended.
        self.game_over = False
