import random

from configs.display import WINDOW_WIDTH, WINDOW_HEIGHT
from configs.gameplay import (
    CELL_SIZE,
    GRID_COLUMNS,
    GRID_ROWS,
    OFFSET_X,
    OFFSET_Y,
)

from configs.levels import LEVELS
from game.entities.obstacle import Obstacle


class LevelManager:
    """
    Manages all level-related data and logic.

    The manager is responsible for:
    - loading level configuration;
    - loading the background image;
    - creating static and random obstacles;
    - providing the food image path;
    - calculating forbidden cells;
    - checking obstacle collisions;
    - checking the win condition.
    """

    def __init__(self, asset_manager):
        """
        Initialize the level manager.

        Args:
            asset_manager (AssetManager): Manager used to load images.
        """
        self.asset_manager = asset_manager

        # Currently selected level key.
        self.selected_level = None

        # Configuration data of the selected level.
        self.level_data = None

        # Loaded background image.
        self.background = None

        # Optional playable area restrictions.
        self.play_area = None

        # List of Obstacle objects.
        self.obstacles = []

    def load_level(self, level_key):
        """
        Load the specified level.

        Args:
            level_key (str): Level identifier.
        """
        self.selected_level = level_key
        self.level_data = LEVELS[level_key]
        self.play_area = self.level_data.get("play_area")

        if level_key == "random":
            self.load_random_level()
            return

        self.background = self.asset_manager.load_scaled_image(
            f"{level_key}_background",
            self.level_data["background"],
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            alpha=False,
        )

        self.obstacles = self.create_obstacles(self.level_data["obstacles"])

    def load_random_level(self):
        """
        Load the procedural random level.

        The random level uses:
        - a fixed chaotic background;
        - a random food image;
        - randomly generated obstacles.
        """
        food_path = random.choice(self.level_data["foods"])

        # Save the selected food image path.
        self.level_data["food"] = food_path

        # Load the random level background.
        self.background = self.asset_manager.load_scaled_image(
            "background",
            self.level_data["background"],
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            alpha=False,
        )

        # Generate random obstacles.
        self.obstacles = self.create_random_obstacles()

    def create_obstacles(self, obstacles_data):
        """
        Create obstacle objects from configuration data.

        Args:
            obstacles_data (list[dict]): Obstacle configuration list.

        Returns:
            list[Obstacle]: Created obstacles.
        """

        obstacles = []

        for obstacle_data in obstacles_data:
            obstacle = Obstacle(
                position=obstacle_data["position"],
                size=obstacle_data["size"],
                image_path=obstacle_data["image"],
                cell_size=CELL_SIZE,
                offset_x=OFFSET_X,
                offset_y=OFFSET_Y,
            )

            obstacles.append(obstacle)

        return obstacles

    def create_random_obstacles(self):
        """
        Generate random obstacles for the random level.

        Returns:
            list[Obstacle]: Generated obstacles.
        """
        obstacles = []

        min_count, max_count = self.level_data["obstacle_count"]
        obstacle_count = random.randint(min_count, max_count)

        attempts = 0
        max_attempts = 200

        while len(obstacles) < obstacle_count and attempts < max_attempts:
            attempts += 1

            obstacle_template = random.choice(self.level_data["obstacle_pool"])
            size = obstacle_template["size"]

            position = [
                random.randint(0, GRID_COLUMNS - size),
                random.randint(0, GRID_ROWS - size),
            ]

            obstacle_data = {
                "image": obstacle_template["image"],
                "position": position,
                "size": size,
            }

            new_obstacle = Obstacle(
                position=obstacle_data["position"],
                size=obstacle_data["size"],
                image_path=obstacle_data["image"],
                cell_size=CELL_SIZE,
                offset_x=OFFSET_X,
                offset_y=OFFSET_Y,
            )

            if self.is_obstacle_place_free(new_obstacle, obstacles):
                obstacles.append(new_obstacle)

        return obstacles

    def is_obstacle_place_free(self, new_obstacle, existing_obstacles):
        """
        Check whether an obstacle can be placed.

        Args:
            new_obstacle (Obstacle): Obstacle to validate.
            existing_obstacles (list[Obstacle]):
                Already placed obstacles.

        Returns:
            bool: True if the position is valid.
        """
        for cell in new_obstacle.cells:
            if self.is_outside_play_area(cell):
                return False

            for obstacle in existing_obstacles:
                if cell in obstacle.cells:
                    return False

        return True

    def get_food_image_path(self):
        """
        Return the food image path for the current level.

        Returns:
            str: Path to the food image.
        """
        return self.level_data["food"]

    def get_forbidden_cells(self, snake_body):
        """
        Return all cells where food cannot spawn.

        Args:
            snake_body (list[list[int]]): Snake body cells.

        Returns:
            list[list[int]]: Forbidden cells.
        """
        forbidden = []

        # Snake body cells.
        forbidden.extend(snake_body)

        # Obstacle cells.
        for obstacle in self.obstacles:
            forbidden.extend(obstacle.cells)

        # Cells outside the allowed play area.
        if self.play_area:
            for x in range(GRID_COLUMNS):
                for y in range(GRID_ROWS):
                    cell = [x, y]

                    if self.is_outside_play_area(cell):
                        forbidden.append(cell)

        return forbidden

    def is_outside_play_area(self, cell):
        """
        Check whether a cell is outside the allowed play area.

        Args:
            cell (list[int]): Grid coordinates [x, y].

        Returns:
            bool: True if the cell is outside.
        """
        if not self.play_area:
            return False

        x, y = cell

        return (
            x < self.play_area["x_min"]
            or x > self.play_area["x_max"]
            or y < self.play_area["y_min"]
            or y > self.play_area["y_max"]
        )

    def has_obstacle_collision(self, cell):
        """
        Check whether a cell collides with an obstacle.

        Args:
            cell (list[int]): Grid coordinates [x, y].

        Returns:
            bool: True if the cell is occupied.
        """
        for obstacle in self.obstacles:
            if cell in obstacle.cells:
                return True

        return False

    def draw_obstacles(self, screen):
        """
        Draw all obstacles.

        Args:
            screen (pygame.Surface): Target surface.
        """
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def check_win(self, snake_body):
        """
        Check whether the snake occupies all available cells.

        Args:
            snake_body (list[list[int]]): Snake body cells.

        Returns:
            bool: True if the player has won.
        """
        available_cells = 0

        for x in range(GRID_COLUMNS):
            for y in range(GRID_ROWS):
                cell = [x, y]

                if self.is_outside_play_area(cell):
                    continue

                if self.has_obstacle_collision(cell):
                    continue

                available_cells += 1

        return len(snake_body) >= available_cells
