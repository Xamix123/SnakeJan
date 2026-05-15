import pygame

from configs.display import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)

from configs.colors import (
    OVERLAY_COLOR,
    HIGH_SCORE_TITLE_COLOR,
    NAME_INPUT_TEXT_COLOR,
    NAME_INPUT_HINT_COLOR,
)

from configs.ui import (
    NAME_INPUT_MAX_LENGTH,
    NAME_INPUT_TITLE_OFFSET_Y,
    NAME_INPUT_SUBTITLE_OFFSET_Y,
    NAME_INPUT_VALUE_OFFSET_Y,
    NAME_INPUT_HINT_OFFSET_Y,
    NAME_INPUT_CURSOR_BLINK_INTERVAL,
    NAME_INPUT_CURSOR_VISIBLE_TIME,
    DEFAULT_PLAYER_NAME,
)


class NameInput:
    """
    Displays the high score name input overlay.

    The overlay allows the player to enter their name
    after achieving a new high score.
    """

    def __init__(
        self,
        screen,
        title_font,
        input_font,
        max_length=NAME_INPUT_MAX_LENGTH,
    ):
        """
        Initialize the name input overlay.

        Args:
            screen (pygame.Surface): Target surface.
            title_font (pygame.font.Font): Font for the title text.
            input_font (pygame.font.Font): Font for input and hint text.
            max_length (int): Maximum allowed name length.
        """
        self.screen = screen
        self.title_font = title_font
        self.input_font = input_font
        self.max_length = max_length

        # Current player name being entered.
        self.player_name = ""

        # Indicates whether the input overlay is active.
        self.active = False

    def start(self):
        """
        Activate the input overlay and clear the current name.
        """
        self.player_name = ""
        self.active = True

    def handle_event(self, event):
        """
        Handle keyboard input.

        Args:
            event (pygame.event.Event): Pygame event.

        Returns:
            str | None:
                Entered player name if input is completed,
                otherwise None.
        """
        if not self.active:
            return None

        # Confirm input.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                name = self.player_name.strip()

                if not name:
                    name = DEFAULT_PLAYER_NAME

                self.active = False
                return name
            # Cancel input.
            elif event.key == pygame.K_ESCAPE:
                self.active = False
                return DEFAULT_PLAYER_NAME
            # Remove the last character.
            elif event.key == pygame.K_BACKSPACE:
                self.player_name = self.player_name[:-1]
            # Append printable characters.
            else:
                if (
                    len(self.player_name) < self.max_length
                    and event.unicode.isprintable()
                    and event.unicode not in "\r\n\t"
                ):
                    self.player_name += event.unicode

        return None

    def draw(self):
        """
        Draw the name input overlay.
        """
        if not self.active:
            return

        # Create a semi-transparent dark overlay.
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        overlay.fill(OVERLAY_COLOR)

        # Draw the darkened background.
        self.screen.blit(overlay, (0, 0))

        # Render the title.
        title_text = self.title_font.render(
            "New High Score!", True, (HIGH_SCORE_TITLE_COLOR)
        )

        title_rect = title_text.get_rect(
            center=(
                WINDOW_WIDTH // 2,
                WINDOW_HEIGHT // 2 + NAME_INPUT_TITLE_OFFSET_Y,
            )
        )

        self.screen.blit(title_text, title_rect)

        # Render the subtitle.
        subtitle_text = self.input_font.render(
            "Enter your name:", True, (NAME_INPUT_TEXT_COLOR)
        )

        subtitle_rect = subtitle_text.get_rect(
            center=(
                WINDOW_WIDTH // 2,
                WINDOW_HEIGHT // 2 + NAME_INPUT_SUBTITLE_OFFSET_Y,
            )
        )

        self.screen.blit(subtitle_text, subtitle_rect)

        # Prepare the displayed name.
        display_name = self.player_name

        # Show a blinking cursor.
        if (
            pygame.time.get_ticks() % NAME_INPUT_CURSOR_BLINK_INTERVAL
            < NAME_INPUT_CURSOR_VISIBLE_TIME
        ):
            display_name += "|"

        # Show only the cursor if the name is empty.
        if not display_name.strip("|"):
            display_name = "|"

        # Render the entered name.
        name_text = self.input_font.render(display_name, True, (255, 255, 255))

        name_rect = name_text.get_rect(
            center=(
                WINDOW_WIDTH // 2,
                WINDOW_HEIGHT // 2 + NAME_INPUT_VALUE_OFFSET_Y,
            )
        )

        self.screen.blit(name_text, name_rect)

        # Render the confirmation hint.
        hint_text = self.input_font.render(
            "Press Enter to confirm", True, (NAME_INPUT_HINT_COLOR)
        )

        hint_rect = hint_text.get_rect(
            center=(
                WINDOW_WIDTH // 2,
                WINDOW_HEIGHT // 2 + NAME_INPUT_HINT_OFFSET_Y,
            )
        )

        self.screen.blit(hint_text, hint_rect)
