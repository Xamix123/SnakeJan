import random
import pygame

from settings import (
    CELL_SIZE,
    GRID_COLUMNS,
    GRID_ROWS,
    OFFSET_X,
    OFFSET_Y
)

class Food:
    def __init__(self):
        self.color = (220, 30, 30)
        self.position = self.generate_position()

    def generate_position(self):
        x = random.randint(0, GRID_COLUMNS - 1)
        y = random.randint(0, GRID_ROWS - 1)

        return [x, y]

    def respawn(self):
        self.position = self.generate_position()

    def draw(self, screen):
        x = OFFSET_X + self.position[0] * CELL_SIZE
        y = OFFSET_Y + self.position[1] * CELL_SIZE

        pygame.draw.rect(
            screen,
            self.color,
            (x, y, CELL_SIZE, CELL_SIZE)
        )