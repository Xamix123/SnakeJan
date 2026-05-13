import pygame


class Obstacle:
    def __init__(self, position, size, image_path, cell_size, offset_x, offset_y):
        self.position = position  # [x, y] в клетках
        self.size = size          # сколько клеток занимает, например 3
        self.cell_size = cell_size
        self.offset_x = offset_x
        self.offset_y = offset_y

        image = pygame.image.load(image_path).convert_alpha()
        pixel_size = self.size * self.cell_size

        self.image = pygame.transform.smoothscale(
            image,
            (pixel_size, pixel_size)
        )

        self.cells = self.get_cells()

    def get_cells(self):
        cells = []

        start_x, start_y = self.position

        for y in range(start_y, start_y + self.size):
            for x in range(start_x, start_x + self.size):
                cells.append([x, y])

        return cells

    def draw(self, screen):
        x = self.offset_x + self.position[0] * self.cell_size
        y = self.offset_y + self.position[1] * self.cell_size

        screen.blit(self.image, (x, y))