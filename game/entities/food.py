import random
import pygame

from configs.gameplay import (
    CELL_SIZE,
    GRID_COLUMNS,
    GRID_ROWS,
    OFFSET_X,
    OFFSET_Y,
)


class Food:
    """
    Represents a food object that appears on the game field.

    The food is displayed as an image and can respawn at a random free
    cell that is not occupied by the snake or obstacles.
    """

    def __init__(self, image_path):
        """
        Initialize the food object.

        Args:
            image_path (str): Path to the food image file.
        """
        self.position = [0, 0]
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))

    def respawn(self, forbidden_cells):
        """
        Generate a new random position for the food.

        The new position must not intersect with any cell from
        forbidden_cells.

        Args:
            forbidden_cells (list[list[int]]): Cells that cannot be used
                for food placement.
        """
        while True:
            position = [
                random.randint(0, GRID_COLUMNS - 1),
                random.randint(0, GRID_ROWS - 1),
            ]

            if position not in forbidden_cells:
                self.position = position
                break

    def draw(self, screen):
        """
        Draw the food on the screen.

        Args:
            screen (pygame.Surface): Surface where the food will be drawn.
        """
        x = OFFSET_X + self.position[0] * CELL_SIZE
        y = OFFSET_Y + self.position[1] * CELL_SIZE

        screen.blit(self.image, (x, y))
