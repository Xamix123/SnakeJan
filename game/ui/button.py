import pygame

from configs.colors import BUTTON_TEXT_COLOR


class Button:
    """
    Represents an interactive UI button.

    The button consists of:
    - a background image;
    - a hover image displayed when the mouse is over the button;
    - centered text rendered on top of the image.
    """

    def __init__(
        self, text, center_x, center_y, width, height, font, image, hover_image
    ):
        """
        Initialize the button.

        Args:
            text (str): Text displayed on the button.
            center_x (int): X coordinate of the button center.
            center_y (int): Y coordinate of the button center.
            width (int): Button width in pixels.
            height (int): Button height in pixels.
            font (pygame.font.Font): Font used to render the text.
            image (pygame.Surface): Default button image.
            hover_image (pygame.Surface): Image shown on mouse hover.
        """
        # Button caption.
        self.text = text

        # Font used to render the caption.
        self.font = font

        # Button rectangle used for rendering and click detection.
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (center_x, center_y)

        # Scale images to the button size.
        self.image = pygame.transform.scale(image, (width, height))
        self.hover_image = pygame.transform.scale(hover_image, (width, height))

        # Text color.
        self.text_color = BUTTON_TEXT_COLOR

    def draw(self, screen):
        """
        Draw the button on the screen.

        If the mouse cursor is over the button,
        the hover image is displayed.

        Args:
            screen (pygame.Surface): Target surface.
        """

        mouse_pos = pygame.mouse.get_pos()

        # Select the appropriate image depending on hover state.
        image = self.hover_image if self.rect.collidepoint(mouse_pos) else self.image

        # Draw the button background.
        screen.blit(image, self.rect)

        # Render and center the text.
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        # Draw the text.
        screen.blit(text_surface, text_rect)

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
