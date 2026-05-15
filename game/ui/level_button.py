import pygame


class LevelButton:
    """
    Represents a clickable level selection button.

    Each button displays:
    - a default image;
    - a hover image shown when the mouse cursor is over it.

    The button returns its associated level key when selected.
    """

    def __init__(
        self,
        level_key,
        image,
        hover_image,
        x,
        y,
        size,
    ):
        """
        Initialize the level button.

        Args:
            level_key (str): Level identifier (e.g. "spring").
            image (pygame.Surface): Default button image.
            hover_image (pygame.Surface): Image displayed on hover.
            x (int): Left coordinate in pixels.
            y (int): Top coordinate in pixels.
            size (int): Width and height of the square button.
        """
        # Identifier of the level associated with this button.
        self.level_key = level_key

        # Scale images to the desired button size.
        self.image = pygame.transform.scale(
            image,
            (size, size),
        )

        self.hover_image = pygame.transform.scale(
            hover_image,
            (size, size),
        )

        # Rectangle used for positioning and click detection.
        self.rect = pygame.Rect(
            x,
            y,
            size,
            size,
        )

    def draw(self, screen):
        """
        Draw the button.

        If the mouse cursor is over the button,
        the hover image is displayed.

        Args:
            screen (pygame.Surface): Target surface.
        """
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.hover_image, self.rect)
        else:
            screen.blit(self.image, self.rect)

    def is_clicked(self, event):
        """
        Check whether the button was clicked.

        Args:
            event (pygame.event.Event): Pygame event.

        Returns:
            bool: True if the left mouse button was pressed
            inside the button area.
        """
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )