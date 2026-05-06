import pygame
from settings import (
    CELL_SIZE,
    GRID_COLUMNS,
    GRID_ROWS,
    OFFSET_X,
    OFFSET_Y
)


class Snake:
    def __init__(self):
        self.body = [
            [5, 5],
            [4, 5],
            [3, 5]
        ]

        self.direction = [1, 0]
        self.color = (0, 200, 0)
        self.grow = False

    def change_direction(self, new_direction):
        # запрет разворота на 180 градусов
        if new_direction[0] == -self.direction[0] and new_direction[1] == -self.direction[1]:
            return

        self.direction = new_direction

    def move(self):
        head = self.body[0].copy()

        head[0] += self.direction[0]
        head[1] += self.direction[1]

        max_x = GRID_COLUMNS
        max_y = GRID_ROWS
        # переход через экран
        if head[0] >= max_x:
            head[0] = 0

        elif head[0] < 0:
            head[0] = max_x - 1

        if head[1] >= max_y:
            head[1] = 0

        elif head[1] < 0:
            head[1] = max_y - 1

        self.body.insert(0, head)

        # если НЕ растем — удаляем хвост
        if not self.grow:
            self.body.pop()

        else:
            self.grow = False

    def draw(self, screen):
        for segment in self.body:
            x = OFFSET_X + segment[0] * CELL_SIZE
            y = OFFSET_Y + segment[1] * CELL_SIZE

            pygame.draw.rect(
                screen,
                self.color,
                (x, y, CELL_SIZE, CELL_SIZE)
            )

    def check_collision(self):
        head = self.body[0]

        # проверяем тело без головы
        if head in self.body[1:]:
            return True

        return False