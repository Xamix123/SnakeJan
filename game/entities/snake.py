import pygame

from configs.gameplay import (
    CELL_SIZE,
    GRID_COLUMNS,
    GRID_ROWS,
    OFFSET_X,
    OFFSET_Y,
    MOUTH_OPEN_DURATION,
)

from configs.visual import (
    SNAKE_HEAD_PATH,
    SNAKE_BODY_PATH,
    SNAKE_HEAD_OPEN_PATH,
)


class Snake:
    def __init__(self):
        self.body = [[5, 5], [4, 5], [3, 5]]

        self.direction = [1, 0]
        self.grow = False

        self.head_image = self.load_image(SNAKE_HEAD_PATH)
        self.head_open_image = self.load_image(SNAKE_HEAD_OPEN_PATH)
        self.body_image = self.load_image(SNAKE_BODY_PATH)

        self.mouth_open_until = 0

    def load_image(self, path):
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))

    def change_direction(self, new_direction):
        if (
            new_direction[0] == -self.direction[0]
            and new_direction[1] == -self.direction[1]
        ):
            return

        self.direction = new_direction

    def move(self):
        head = self.body[0].copy()

        head[0] += self.direction[0]
        head[1] += self.direction[1]

        if head[0] >= GRID_COLUMNS:
            head[0] = 0
        elif head[0] < 0:
            head[0] = GRID_COLUMNS - 1

        if head[1] >= GRID_ROWS:
            head[1] = 0
        elif head[1] < 0:
            head[1] = GRID_ROWS - 1

        self.body.insert(0, head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def draw(self, screen):
        for index, segment in enumerate(self.body):
            x = OFFSET_X + segment[0] * CELL_SIZE
            y = OFFSET_Y + segment[1] * CELL_SIZE

            if index == 0:
                image = self.get_rotated_head()
            else:
                image = self.body_image

            screen.blit(image, (x, y))

    def get_rotated_head(self):
        current_image = self.get_current_head_image()

        if self.direction == [1, 0]:
            return current_image

        if self.direction == [-1, 0]:
            return pygame.transform.rotate(current_image, 180)

        if self.direction == [0, -1]:
            return pygame.transform.rotate(current_image, 90)

        if self.direction == [0, 1]:
            return pygame.transform.rotate(current_image, -90)

        return current_image

    def open_mouth(self):
        self.mouth_open_until = pygame.time.get_ticks() + MOUTH_OPEN_DURATION

    def get_current_head_image(self):
        if pygame.time.get_ticks() < self.mouth_open_until:
            return self.head_open_image

        return self.head_image

    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:]
