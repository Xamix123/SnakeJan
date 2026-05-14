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
    def __init__(self, asset_manager):
        self.asset_manager = asset_manager

        self.selected_level = None
        self.level_data = None
        self.background = None
        self.play_area = None
        self.obstacles = []

    def load_level(self, level_key):
        self.selected_level = level_key
        self.level_data = LEVELS[level_key]

        self.play_area = self.level_data.get("play_area")
        self.background = self.asset_manager.load_scaled_image(
            f"{level_key}_background",
            self.level_data["background"],
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            alpha=False,
        )

        self.obstacles = self.create_obstacles(self.level_data["obstacles"])

    def create_obstacles(self, obstacles_data):
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

    def get_food_image_path(self):
        return self.level_data["food"]

    def get_forbidden_cells(self, snake_body):
        forbidden = []

        forbidden.extend(snake_body)

        for obstacle in self.obstacles:
            forbidden.extend(obstacle.cells)

        if self.play_area:
            for x in range(GRID_COLUMNS):
                for y in range(GRID_ROWS):
                    cell = [x, y]

                    if self.is_outside_play_area(cell):
                        forbidden.append(cell)

        return forbidden

    def is_outside_play_area(self, cell):
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
        for obstacle in self.obstacles:
            if cell in obstacle.cells:
                return True

        return False

    def draw_obstacles(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def check_win(self, snake_body):
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
