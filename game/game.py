import pygame
from entities.snake import Snake
from entities.food import Food
from entities.obstacle import Obstacle
from ui.menu import Menu
from ui.level_select import LevelSelect
from ui.leaderboard import Leaderboard
from ui.score_panel import ScorePanel
from ui.name_input import NameInput
from managers.sound_manager import SoundManager
from managers.asset_manager import AssetManager
from managers.leaderboard_manager import LeaderboardManager

from settings import (
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
    GRID_COLOR,
    LEVEL_PANEL_PATH,
    LEVELS,
    GAME_OVER_PANEL_PATH,
    ROCK_OBSTACLE_PATH,
    SCORE_POINT
)


#TODO класс избыточный необходимо раскидать его по подклассам и сделать более синтаксически корректным добавить комменты сгруппировать логику и вынести все что можно по разным классам а так же константы 

class Game:
    def __init__(self):
        pygame.init()
        self.state = "menu"
        

        self.screen = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            pygame.FULLSCREEN
        )

        pygame.display.set_caption("Snake")

        self.init_managers()
        self.init_fonts()
        
        self.menu = Menu(
            self.screen,
            self.asset_manager,
            self.main_font,
            self.author_font
        )
        self.menu_background = self.menu.background
        self.background = self.menu.background

        self.sound_manager.play_main_theme()

        self.game_over_screen = self.asset_manager.load_image(
            "game_over_panel",
            GAME_OVER_PANEL_PATH
        )
        self.game_over_rect = self.game_over_screen.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        )

        self.clock = pygame.time.Clock()
        self.running = True
        self.snake = Snake()
        self.food = None
        self.game_over = False
        self.score = 0
        self.move_timer = 0
        self.selected_level = None
        self.play_area = None
        self.obstacles = []

        self.level_select = LevelSelect(
            self.screen,
            self.asset_manager,
            self.menu_background
        )

        self.leaderboard_manager = LeaderboardManager()

        self.leaderboard = Leaderboard(
            self.screen,
            self.asset_manager,
            self.menu_background,
            self.leaderboard_font,
            self.leaderboard_score_font,
            self.leaderboard_manager
        )

        self.score_panel = ScorePanel(
            self.screen,
            self.asset_manager,
            self.score_font
        )

        self.name_input = NameInput(
            self.screen,
            self.main_font,
            self.leaderboard_score_font
        )


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
                    if self.state in (
                        "playing",
                        "level_select",
                        "leaderboard",
                        "enter_name"
                    ):
                        self.state = "menu"
                        self.sound_manager.play_main_theme()
                    else:
                        self.running = False

                elif event.key == pygame.K_r and self.game_over:
                    self.restart()

            if self.state == "menu":
                action = self.menu.handle_event(event)

                if action == "level_select":
                    self.state = "level_select"

                elif action == "leaderboard":
                    self.state = "leaderboard"
                    self.sound_manager.play_leaderboard_theme(False)

                elif action == "exit":
                    self.running = False

            elif self.state == "playing":
                self.handle_game_events(event)

            elif self.state == "level_select":
                level_key = self.level_select.handle_event(event)
                if level_key:
                    self.apply_level(level_key)
                    self.restart()
                    self.state = "playing"
                        
            elif self.state == "leaderboard":
                self.leaderboard.handle_event(event)
            elif self.state == "enter_name":
                player_name = self.name_input.handle_event(event)

                if player_name:
                    map_name = self.selected_level or "Undefined" #TODO make constant

                    self.leaderboard_manager.add_score(
                        map_name,
                        player_name,
                        self.score
                    )

                    self.leaderboard.active_tab = map_name
                    self.state = "leaderboard"
                    self.sound_manager.play_leaderboard_theme(False)


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

        if self.is_outside_play_area(head):
            self.finish_game()
            return

        for obstacle in self.obstacles:
            if head in obstacle.cells:
                self.finish_game()
                return

        if head == self.food.position:
            self.sound_manager.play_food_sound()
            self.snake.grow = True
            self.snake.open_mouth()
            self.score += SCORE_POINT

            if self.check_win():
                self.finish_game()
                return

            self.food.respawn(self.get_forbidden_cells())

        if self.snake.check_collision():
            self.finish_game()
            
    def draw(self):
        self.screen.blit(self.background, (0, 0))

        if self.state == "menu":
            self.menu.draw()

        elif self.state == "playing":
            self.food.draw(self.screen)

            for obstacle in self.obstacles:
                obstacle.draw(self.screen)

            self.snake.draw(self.screen)

            self.score_panel.draw(self.score)

            if self.game_over:
                self.draw_game_over()
        elif self.state == "level_select":
            self.level_select.draw()
        elif self.state == "leaderboard":
            self.leaderboard.draw()
        elif self.state == "enter_name":
            self.food.draw(self.screen)

            for obstacle in self.obstacles:
                obstacle.draw(self.screen)

            self.snake.draw(self.screen)

            self.score_panel.draw(self.score)

            self.name_input.draw()

        pygame.display.flip()
        
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

        self.screen.blit(self.game_over_screen, self.game_over_rect)

    def finish_game(self):
        map_name = self.selected_level or "Undefined" #TODO сделай константой

        if self.leaderboard_manager.is_high_score(map_name, self.score):
            self.name_input.start()
            self.state = "enter_name"

            # если побил рекорд — сразу включаем музыку лидерборда
            self.sound_manager.play_leaderboard_theme(False)

        else:
            self.game_over = True

            # если рекорда нет — проигрываем звук поражения
            self.sound_manager.play_game_over_sound()

    def check_win(self):
        total_cells = GRID_COLUMNS * GRID_ROWS
        occupied_cells = len(self.get_forbidden_cells())

        return occupied_cells >= total_cells

    def restart(self):
        self.snake = Snake()
        level_data = LEVELS[self.selected_level]
        self.food = Food(level_data["food"])
        self.food.respawn(self.get_forbidden_cells())
        self.score = 0
        self.move_timer = 0
        self.game_over = False
        if not self.sound_manager.is_music_playing():
            self.sound_manager.play_main_theme()
        
    def quit(self):
        self.sound_manager.stop_music()
        pygame.quit()

    def apply_level(self, level_key):
        self.selected_level = level_key
        level_data = LEVELS[level_key]

        self.play_area = level_data.get("play_area")
        self.food = Food(level_data["food"])
        self.food.respawn(self.get_forbidden_cells())

        self.background = self.asset_manager.load_scaled_image(
            f"{level_key}_background",
            level_data["background"],
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            alpha=False
        )
        self.obstacles = []

        for obstacle_data in level_data["obstacles"]:
            obstacle = Obstacle(
                position=obstacle_data["position"],
                size=obstacle_data["size"],
                image_path=obstacle_data["image"],
                cell_size=CELL_SIZE,
                offset_x=OFFSET_X,
                offset_y=OFFSET_Y
            )

            self.obstacles.append(obstacle)

    def get_forbidden_cells(self):
        forbidden = []

        forbidden.extend(self.snake.body)

        for obstacle in self.obstacles:
            forbidden.extend(obstacle.cells)

        if self.play_area:
            for x in range(GRID_COLUMNS):
                for y in range(GRID_ROWS):
                    cell = [x, y]

                    if self.is_outside_play_area(cell):
                        forbidden.append(cell)

        return forbidden
    
    def is_outside_play_area(self, cell):
        if not self.play_area:
            return False

        x, y = cell

        return (
            x < self.play_area["x_min"] or
            x > self.play_area["x_max"] or
            y < self.play_area["y_min"] or
            y > self.play_area["y_max"]
        )
    
    def init_managers(self):
        self.asset_manager = AssetManager()
        self.sound_manager = SoundManager()
        
    def init_fonts(self):
        self.main_font = pygame.font.SysFont("Arial", 48)
        self.score_font = pygame.font.SysFont("Arial", 64, True)
        self.leaderboard_font = pygame.font.SysFont("Arial", 28)
        self.leaderboard_score_font = pygame.font.SysFont("Arial", 48, True)
        self.author_font = pygame.font.Font(None, 64)