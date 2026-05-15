import pygame


class Obstacle:
    """
    Represents a static obstacle on the game field.

    An obstacle occupies a square area of size x size cells.
    The snake loses if it collides with any occupied cell.
    """
    def __init__(self, position, size, image_path, cell_size, offset_x, offset_y):
        """
        Initialize the obstacle.

        Args:
            position (list[int]): Top-left position of the obstacle in grid cells [x, y].
            size (int): Obstacle size in cells (e.g. 3 means 3x3 cells).
            image_path (str): Path to the obstacle image.
            cell_size (int): Size of one grid cell in pixels.
            offset_x (int): Horizontal offset of the game field.
            offset_y (int): Vertical offset of the game field.
        """
         # Position of the top-left corner in grid coordinates.
        self.position = position
         # Size of the obstacle in grid cells. 
        self.size = size
        # Rendering settings.
        self.cell_size = cell_size
        self.offset_x = offset_x
        self.offset_y = offset_y

        # Load and scale the obstacle image.
        image = pygame.image.load(image_path).convert_alpha()
        pixel_size = self.size * self.cell_size

        self.image = pygame.transform.smoothscale(image, (pixel_size, pixel_size))

        # Precompute all grid cells occupied by the obstacle.
        self.cells = self.get_cells()

    def get_cells(self):
        """
        Return a list of all grid cells occupied by the obstacle.

        Returns:
            list[list[int]]: List of [x, y] coordinates.
        """
        cells = []

        start_x, start_y = self.position

        for y in range(start_y, start_y + self.size):
            for x in range(start_x, start_x + self.size):
                cells.append([x, y])

        return cells

    def draw(self, screen):
        """
        Draw the obstacle on the screen.

        Args:
            screen (pygame.Surface): Target surface for rendering.
        """
         # Convert grid coordinates to pixel coordinates.
        x = self.offset_x + self.position[0] * self.cell_size
        y = self.offset_y + self.position[1] * self.cell_size

        # Draw the obstacle image.
        screen.blit(self.image, (x, y))
