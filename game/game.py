import pygame
from snake import Snake
from food import Food
from button import Button
from level_button import LevelButton

from settings import (
    AUTHOR,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    CELL_SIZE,
    GRID_COLUMNS,
    GRID_ROWS,
    GAME_WIDTH,
    GAME_HEIGHT,
    OFFSET_X,
    OFFSET_Y,
    FPS,
    SNAKE_SPEED,
    BACKGROUND_COLOR,
    GRID_COLOR,
    MAIN_THEME_PATH,
    LEADERBOARD_THEME_PATH,
    FOOD_EAT_SOUND_PATH,
    GAME_OVER_SOUND_PATH,
    LOGO_IMAGE_PATH,
    MENU_BACKGROUND_PATH,
    BUTTON_IMAGE_PATH,
    BUTTON_HOVER_IMAGE_PATH,
    LEVEL_PANEL_PATH,
    LEVELS,
    GAME_OVER_PANEL_PATH,
    LEADERBOARD_PANEL_PATH,
    LEADERBOARD_TAB_PATH,
    LEADERBOARD_TAB_HOVER_PATH,
    LEADERBOARD_TAB_ACTIVE_PATH
)


#TODO класс избыточный необходимо раскидать его по подклассам и сделать более синтаксически корректным добавить комменты сгруппировать логику и вынести все что можно по разным классам а так же константы 

class Game:
    def __init__(self):
        pygame.init()
        self.state = "menu"
        self.menu_font = pygame.font.SysFont("Arial", 48)

        self.screen = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            pygame.FULLSCREEN
        )
        pygame.display.set_caption("Snake")
        self.menu_background = pygame.image.load(MENU_BACKGROUND_PATH).convert()
        self.menu_background = pygame.transform.scale(
            self.menu_background,
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )

        self.button_image = pygame.image.load(BUTTON_IMAGE_PATH).convert_alpha()
        self.button_hover_image = pygame.image.load(BUTTON_HOVER_IMAGE_PATH).convert_alpha()

        self.logo_image = pygame.image.load(LOGO_IMAGE_PATH).convert_alpha()

        logo_width = WINDOW_WIDTH // 3
        logo_height = int(logo_width * self.logo_image.get_height() / self.logo_image.get_width())

        self.logo_image = pygame.transform.scale(
            self.logo_image,
            (logo_width, logo_height)
        )

        self.logo_rect = self.logo_image.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 5)
        )

        button_width = WINDOW_WIDTH // 4
        button_height = WINDOW_HEIGHT // 8

        center_x = WINDOW_WIDTH // 2
        start_y = WINDOW_HEIGHT // 2 - 40
        gap = button_height + 30

        self.buttons = {
            "play": Button("Play", center_x, start_y, button_width, button_height, self.menu_font, self.button_image, self.button_hover_image),
            "settings": Button("Settings", center_x, start_y + gap, button_width, button_height, self.menu_font, self.button_image, self.button_hover_image),
            "leaderboard": Button("Leaderboard", center_x, start_y + gap * 2, button_width, button_height, self.menu_font, self.button_image, self.button_hover_image),
            "exit": Button("Exit", center_x, start_y + gap * 3, button_width, button_height, self.menu_font, self.button_image, self.button_hover_image),
        }

        self.level_panel = pygame.image.load(LEVEL_PANEL_PATH).convert_alpha()

        panel_width = int(WINDOW_WIDTH * 0.75)
        panel_height = int(panel_width * self.level_panel.get_height() / self.level_panel.get_width())

        self.level_panel = pygame.transform.scale(
            self.level_panel,
            (panel_width, panel_height)
        )

        self.level_panel_rect = self.level_panel.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        )


        level_size = panel_width // 6
        gap = 40

        levels = ["spring", "summer", "autumn", "winter"]

        total_width = level_size * len(levels) + gap * (len(levels) - 1)

        start_x = self.level_panel_rect.centerx - total_width // 2
        start_y = self.level_panel_rect.centery - level_size // 2

        self.level_buttons = {}

        for index, level_key in enumerate(levels):
            image = pygame.image.load(LEVELS[level_key]["panel"]).convert_alpha()
            hover_image = pygame.image.load(LEVELS[level_key]["panel_hover"]).convert_alpha()

            x = start_x + index * (level_size + gap)
            y = start_y

            self.level_buttons[level_key] = LevelButton(
                level_key,
                image,
                hover_image,
                x,
                y,
                level_size
            )

        self.game_over_screen = pygame.image.load(GAME_OVER_PANEL_PATH).convert_alpha()
        self.game_over_rect = self.game_over_screen.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        )


        self.clock = pygame.time.Clock()
        self.running = True
        self.snake = Snake()
        self.food = Food()
        self.game_over = False
        self.font = pygame.font.SysFont("Arial", 48)
        self.score = 0
        self.score_font = pygame.font.SysFont("Arial", 32)
        self.move_timer = 0
        self.selected_level = None

        # music section initialization TODO возможно стоит вынести в отдельный метод чтобы вызывать в нужный момент тип play main theme play шото там и тд
        pygame.mixer.music.load(MAIN_THEME_PATH)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        self.food_eat_sound = pygame.mixer.Sound(FOOD_EAT_SOUND_PATH)
        self.food_eat_sound.set_volume(0.5) # TODO возможно получиться пределать под абстрактный звук посмотри во время рефакторинга

        self.game_over_sound = pygame.mixer.Sound(GAME_OVER_SOUND_PATH)
        self.game_over_sound.set_volume(0.5)


        #background
        self.background = pygame.image.load(MENU_BACKGROUND_PATH).convert()

        self.background = pygame.transform.scale(
            self.background,
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )

        self.leaderboard_panel = pygame.image.load(LEADERBOARD_PANEL_PATH).convert_alpha()

        leaderboard_width = int(WINDOW_WIDTH * 0.65)
        leaderboard_height = int(
            leaderboard_width * self.leaderboard_panel.get_height()
            / self.leaderboard_panel.get_width()
        )

        self.leaderboard_panel = pygame.transform.scale(
            self.leaderboard_panel,
            (leaderboard_width, leaderboard_height)
        )

        self.leaderboard_rect = self.leaderboard_panel.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        )

        self.leaderboard_tab = pygame.image.load(LEADERBOARD_TAB_PATH).convert_alpha()
        self.leaderboard_tab_hover = pygame.image.load(LEADERBOARD_TAB_HOVER_PATH).convert_alpha()
        self.leaderboard_tab_active = pygame.image.load(LEADERBOARD_TAB_ACTIVE_PATH).convert_alpha()

        self.active_leaderboard_tab = "spring"

        self.leaderboard_tabs = ["spring", "summer", "autumn", "winter", "random"]
        self.leaderboard_tab_names = {
            "spring": "Spring",
            "summer": "Summer",
            "autumn": "Autumn",
            "winter": "Winter",
            "random": "Random",
        }

        self.leaderboard_font = pygame.font.SysFont("Arial", 28)
        self.leaderboard_score_font = pygame.font.SysFont("Arial", 34)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(FPS)

        self.quit()

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state in ("playing", "level_select", "leaderboard"):
                        self.state = "menu"
                    else:
                        self.running = False

                elif event.key == pygame.K_r and self.game_over:
                    self.restart()

            if self.state == "menu":
                self.handle_menu_events(event)

            elif self.state == "playing":
                self.handle_game_events(event)

            elif self.state == "level_select":
                self.handle_level_select_events(event)


    def handle_menu_events(self, event):
        if self.buttons["play"].is_clicked(event):
            self.state = "level_select"

        elif self.buttons["settings"].is_clicked(event):
            print("Under development")

        elif self.buttons["leaderboard"].is_clicked(event):
            self.state = "leaderboard"

        elif self.buttons["exit"].is_clicked(event):
            self.running = False


    def handle_game_events(self, event):
        if event.type == pygame.KEYDOWN:

            if self.game_over:
                return

            if event.key == pygame.K_UP:
                self.snake.change_direction([0, -1])

            elif event.key == pygame.K_DOWN:
                self.snake.change_direction([0, 1])

            elif event.key == pygame.K_LEFT:
                self.snake.change_direction([-1, 0])

            elif event.key == pygame.K_RIGHT:
                self.snake.change_direction([1, 0])


    def update(self):
        if self.state != "playing":
            return

        if self.game_over:
            return

        self.move_timer += 1

        if self.move_timer < FPS // SNAKE_SPEED:
            return

        self.move_timer = 0

        self.snake.move()

        head = self.snake.body[0]

        if head == self.food.position:
            self.food_eat_sound.play()
            self.snake.grow = True
            self.score += 10 # TODO change to constant
            self.food.respawn()

        if self.snake.check_collision():
            self.game_over_sound.play()
            pygame.mixer.music.stop()
            self.game_over = True
            
    def draw(self):
        self.screen.blit(self.background, (0, 0))

        if self.state == "menu":
            self.draw_menu()

        elif self.state == "playing":
            self.food.draw(self.screen)
            self.snake.draw(self.screen)

            self.draw_score()

            if self.game_over:
                self.draw_game_over()
        elif self.state == "level_select":
            self.draw_level_select()
        elif self.state == "leaderboard":
            self.draw_leaderboard()

        pygame.display.flip()

    def draw_menu(self):
        self.screen.blit(self.menu_background, (0, 0))

        self.screen.blit(self.logo_image, self.logo_rect)

        for button in self.buttons.values():
            button.draw(self.screen)

        author_font = pygame.font.Font(None, 64)

        author_text = author_font.render(
            f"Created by {AUTHOR}",
            True,
            (255, 255, 255) # TODO константа белый цвет
        )

        author_rect = author_text.get_rect(
            bottomright=(WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20) # размеры должны быть константами 
        )

        self.screen.blit(author_text, author_rect)

    def handle_level_select_events(self, event):
        for level_key, button in self.level_buttons.items():
            if button.is_clicked(event):
                self.apply_level(level_key)
                self.restart()
                self.state = "playing"


    def draw_level_select(self):
        self.screen.blit(self.menu_background, (0, 0))

        self.screen.blit(self.level_panel, self.level_panel_rect)

        for button in self.level_buttons.values():
            button.draw(self.screen)
        
    def draw_grid(self):
        for x in range(OFFSET_X, OFFSET_X + GAME_WIDTH + 1, CELL_SIZE):
            pygame.draw.line(
                self.screen,
                GRID_COLOR,
                (x, OFFSET_Y),
                (x, OFFSET_Y + GAME_HEIGHT)
            )

        for y in range(OFFSET_Y, OFFSET_Y + GAME_HEIGHT + 1, CELL_SIZE):
            pygame.draw.line(
                self.screen,
                GRID_COLOR,
                (OFFSET_X, y),
                (OFFSET_X + GAME_WIDTH, y)
            )

    def draw_game_over(self):
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))

        # Game Over окно
        self.screen.blit(self.game_over_screen, self.game_over_rect)
    
    def draw_score(self): # TODO переделать 
        text = self.score_font.render(
            f"Score: {self.score}",
            True,
            (0, 0, 0)
        )

        self.screen.blit(text, (20, 20))

    def restart(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False
        if (pygame.mixer.music.get_busy() == False):
            pygame.mixer.music.load(MAIN_THEME_PATH)
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)

        
    def quit(self):
        pygame.quit()

    def apply_level(self, level_key):
        self.selected_level = level_key

        level_data = LEVELS[level_key]

        self.background = pygame.image.load(level_data["background"]).convert()
        self.background = pygame.transform.scale(
            self.background,
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )

    def handle_leaderboard_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for level_key, rect in self.leaderboard_tab_rects.items():
                if rect.collidepoint(event.pos):
                    self.active_leaderboard_tab = level_key

    def draw_leaderboard(self):
        self.screen.blit(self.menu_background, (0, 0))
        self.screen.blit(self.leaderboard_panel, self.leaderboard_rect)

        self.leaderboard_tab_rects = {}

        tab_width = int(self.leaderboard_rect.width * 0.18)
        tab_height = int(tab_width * self.leaderboard_tab.get_height() / self.leaderboard_tab.get_width())

        start_x = self.leaderboard_rect.left + 70
        start_y = self.leaderboard_rect.top + 135
        gap = tab_width + 8

        mouse_pos = pygame.mouse.get_pos()

        for index, level_key in enumerate(self.leaderboard_tabs):
            x = start_x + index * gap
            y = start_y

            rect = pygame.Rect(x, y, tab_width, tab_height)
            self.leaderboard_tab_rects[level_key] = rect

            if level_key == self.active_leaderboard_tab:
                tab_image = self.leaderboard_tab_active
                text_color = (255, 220, 90)
            elif rect.collidepoint(mouse_pos):
                tab_image = self.leaderboard_tab_hover
                text_color = (80, 45, 15)
            else:
                tab_image = self.leaderboard_tab
                text_color = (60, 35, 15)

            tab_image = pygame.transform.scale(tab_image, (tab_width, tab_height))
            self.screen.blit(tab_image, rect)

            text = self.leaderboard_font.render(
                self.leaderboard_tab_names[level_key],
                True,
                text_color
            )
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)

        fake_scores = [
            ("1.", "Jan", "120"),
            ("2.", "Player", "95"),
            ("3.", "Snake", "70"),
            ("4.", "Guest", "45"),
            ("5.", "---", "0"),
        ]

        list_x = self.leaderboard_rect.left + 170
        list_y = self.leaderboard_rect.top + 240
        row_gap = 62

        for index, record in enumerate(fake_scores):
            place, name, score = record
            y = list_y + index * row_gap

            row_text = self.leaderboard_score_font.render(
                f"{place}  {name:<10}  {score}",
                True,
                (70, 45, 20)
            )

            self.screen.blit(row_text, (list_x, y))