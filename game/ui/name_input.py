import pygame

from configs.display import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)


class NameInput:
    def __init__(self, screen, title_font, input_font, max_length=10):
        self.screen = screen
        self.title_font = title_font
        self.input_font = input_font
        self.max_length = max_length

        self.player_name = ""
        self.active = False

    def start(self):
        self.player_name = ""
        self.active = True

    def handle_event(self, event):
        if not self.active:
            return None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                name = self.player_name.strip()

                if not name:
                    name = "Player"

                self.active = False
                return name

            elif event.key == pygame.K_ESCAPE:
                self.active = False
                return "Player"

            elif event.key == pygame.K_BACKSPACE:
                self.player_name = self.player_name[:-1]

            else:
                if (
                    len(self.player_name) < self.max_length
                    and event.unicode.isprintable()
                    and event.unicode not in "\r\n\t"
                ):
                    self.player_name += event.unicode

        return None

    def draw(self):
        if not self.active:
            return

        # Затемнение фона
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

        # Заголовок
        title_text = self.title_font.render("New High Score!", True, (255, 220, 90))

        title_rect = title_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100)
        )

        self.screen.blit(title_text, title_rect)

        # Подсказка
        subtitle_text = self.input_font.render(
            "Enter your name:", True, (255, 255, 255)
        )

        subtitle_rect = subtitle_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 40)
        )

        self.screen.blit(subtitle_text, subtitle_rect)

        # Текущее имя
        display_name = self.player_name
        if pygame.time.get_ticks() % 1000 < 500:
            display_name += "|"

        if not display_name.strip("|"):
            display_name = "|"

        name_text = self.input_font.render(display_name, True, (255, 255, 255))

        name_rect = name_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20)
        )

        self.screen.blit(name_text, name_rect)

        # Инструкция
        hint_text = self.input_font.render(
            "Press Enter to confirm", True, (180, 180, 180)
        )

        hint_rect = hint_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 80)
        )

        self.screen.blit(hint_text, hint_rect)
