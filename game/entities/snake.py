import pygame

from configs.gameplay import (
    CELL_SIZE,
    GRID_COLUMNS,
    GRID_ROWS,
    OFFSET_X,
    OFFSET_Y,
    MOUTH_OPEN_DURATION,
    INITIAL_SNAKE_BODY,
    INITIAL_DIRECTION,
)

from configs.visual import (
    SNAKE_HEAD_PATH,
    SNAKE_BODY_PATH,
    SNAKE_HEAD_OPEN_PATH,
)


class Snake:
    """
    Represents the snake controlled by the player.

    The class is responsible for:
    - storing the snake body segments;
    - handling movement and growth;
    - changing movement direction;
    - drawing the snake;
    - animating the mouth opening;
    - detecting collisions with itself.
    """

    def __init__(self, asset_manager):
        """
        Initialize the snake with its default state.

        Args:
            asset_manager (AssetManager):
                Shared manager used for loading and caching images.
        """
        # Save asset manager reference.
        self.asset_manager = asset_manager

        # Initial body segments in grid coordinates.
        self.body = [segment.copy() for segment in INITIAL_SNAKE_BODY]

        # Current movement direction.
        self.direction = INITIAL_DIRECTION.copy()

        # Prevents multiple direction changes before the next move.
        self.direction_changed = False

        # If True, the snake grows on the next move.
        self.grow = False

        # Load and scale snake images.
        self.head_image = self.asset_manager.load_scaled_image(
            "snake_head",
            SNAKE_HEAD_PATH,
            (CELL_SIZE, CELL_SIZE),
        )

        self.head_open_image = self.asset_manager.load_scaled_image(
            "snake_head_open",
            SNAKE_HEAD_OPEN_PATH,
            (CELL_SIZE, CELL_SIZE),
        )

        self.body_image = self.asset_manager.load_scaled_image(
            "snake_body",
            SNAKE_BODY_PATH,
            (CELL_SIZE, CELL_SIZE),
        )

        # Timestamp until which the mouth remains open.
        self.mouth_open_until = 0

    def change_direction(self, new_direction):
        """
        Change the snake movement direction.

        Only one direction change is allowed between moves.
        Direct reversal is not allowed.

        Args:
            new_direction (list[int]): New direction vector [x, y].
        """
        # Ignore additional direction changes before the next move.
        if self.direction_changed:
            return

        # Prevent reversing into the opposite direction.
        if (
            new_direction[0] == -self.direction[0]
            and new_direction[1] == -self.direction[1]
        ):
            return

        self.direction = new_direction
        self.direction_changed = True

    def move(self):
        """
        Move the snake by one cell.

        The snake wraps around screen edges.
        If the grow flag is set, the tail is preserved.
        Otherwise, the last segment is removed.
        """
        # Copy current head position.
        head = self.body[0].copy()

        # Move head in the current direction.
        head[0] += self.direction[0]
        head[1] += self.direction[1]

        # Horizontal wrapping.
        if head[0] >= GRID_COLUMNS:
            head[0] = 0
        elif head[0] < 0:
            head[0] = GRID_COLUMNS - 1

        # Vertical wrapping.
        if head[1] >= GRID_ROWS:
            head[1] = 0
        elif head[1] < 0:
            head[1] = GRID_ROWS - 1

        # Insert new head at the beginning of the body.
        self.body.insert(0, head)

        # Remove tail unless the snake should grow.
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

        # Allow changing direction again after movement.
        self.direction_changed = False

    def draw(self, screen):
        """
        Draw the snake on the screen.

        Args:
            screen (pygame.Surface): Target surface for rendering.
        """
        for index, segment in enumerate(self.body):
            # Convert grid coordinates to pixel coordinates.
            x = OFFSET_X + segment[0] * CELL_SIZE
            y = OFFSET_Y + segment[1] * CELL_SIZE

            # Draw head or body segment.
            if index == 0:
                image = self.get_rotated_head()
            else:
                image = self.body_image

            screen.blit(image, (x, y))

    def get_rotated_head(self):
        """
        Return the head image rotated according to movement direction.

        Returns:
            pygame.Surface: Rotated head image.
        """
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
        """
        Open the snake mouth for a short animation period.
        """
        self.mouth_open_until = (
            pygame.time.get_ticks() + MOUTH_OPEN_DURATION
        )

    def get_current_head_image(self):
        """
        Return the current head image.

        Returns:
            pygame.Surface:
                Open-mouth image if animation is active,
                otherwise the default head image.
        """
        if pygame.time.get_ticks() < self.mouth_open_until:
            return self.head_open_image

        return self.head_image

    def check_collision(self):
        """
        Check whether the snake collided with itself.

        Returns:
            bool: True if the head intersects with the body.
        """
        head = self.body[0]
        return head in self.body[1:]
