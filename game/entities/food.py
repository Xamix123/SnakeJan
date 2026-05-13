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
    def __init__(self, image_path):
        self.position = [0, 0]

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (CELL_SIZE, CELL_SIZE)
        )

    def respawn(self, forbidden_cells):
        while True:
            position = [
                random.randint(0, GRID_COLUMNS - 1),
                random.randint(0, GRID_ROWS - 1)
            ]

            if position not in forbidden_cells:
                self.position = position
                break

    def draw(self, screen):
        x = OFFSET_X + self.position[0] * CELL_SIZE
        y = OFFSET_Y + self.position[1] * CELL_SIZE

        screen.blit(self.image, (x, y))