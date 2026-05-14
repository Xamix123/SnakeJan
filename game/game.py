import pygame
from .entities.snake import Snake
from .entities.food import Food
from .ui.menu import Menu
from .ui.level_select import LevelSelect
from .ui.leaderboard import Leaderboard
from .ui.score_panel import ScorePanel
from .ui.game_over_overlay import GameOverOverlay
from .ui.name_input import NameInput
from .managers.sound_manager import SoundManager
from .managers.asset_manager import AssetManager
from .managers.leaderboard_manager import LeaderboardManager
from .managers.level_manager import LevelManager
from .managers.font_manager import FontManager
from .game_state import GameState
from .game_session import GameSession

from configs.display import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FPS,
)

from configs.gameplay import (
    SNAKE_SPEED,
    SCORE_POINT,
    DEFAULT_MAP_NAME,
)


class Game:
    def __init__(self):
        pygame.init()
        self.state = GameState.MENU

        self.screen = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN
        )

        pygame.display.set_caption("Snake")

        self.init_managers()

        self.menu = Menu(
            self.screen,
            self.asset_manager,
            self.font_manager.main_font,
            self.font_manager.author_font,
        )
        self.sound_manager.play_main_theme()

        self.game_over_overlay = GameOverOverlay()
        self.clock = pygame.time.Clock()
        self.running = True
        self.snake = Snake()
        self.food = None

        self.session = GameSession()

        self.level_select = LevelSelect(
            self.screen, self.asset_manager, self.menu.background
        )

        self.leaderboard_manager = LeaderboardManager()

        self.leaderboard = Leaderboard(
            self.screen,
            self.asset_manager,
            self.menu.background,
            self.font_manager.leaderboard_font,
            self.font_manager.leaderboard_score_font,
            self.leaderboard_manager,
        )

        self.score_panel = ScorePanel(
            self.screen, self.asset_manager, self.font_manager.score_font
        )

        self.name_input = NameInput(
            self.screen,
            self.font_manager.main_font,
            self.font_manager.leaderboard_score_font,
        )

    def init_managers(self):
        self.asset_manager = AssetManager()
        self.sound_manager = SoundManager()
        self.level_manager = LevelManager(self.asset_manager)
        self.font_manager = FontManager()

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
                        GameState.PLAYING,
                        GameState.LEVEL_SELECT,
                        GameState.LEADERBOARD,
                        GameState.ENTER_NAME,
                    ):
                        self.state = GameState.MENU
                        self.sound_manager.play_main_theme()
                    else:
                        self.running = False

                elif event.key == pygame.K_r and self.session.game_over:
                    self.restart()

            if self.state == GameState.MENU:
                action = self.menu.handle_event(event)

                if action == "level_select":
                    self.state = GameState.LEVEL_SELECT

                elif action == "leaderboard":
                    self.state = GameState.LEADERBOARD
                    self.sound_manager.play_leaderboard_theme(False)

                elif action == "exit":
                    self.running = False

            elif self.state == GameState.PLAYING:
                self.handle_game_events(event)

            elif self.state == GameState.LEVEL_SELECT:
                level_key = self.level_select.handle_event(event)
                if level_key:
                    self.apply_level(level_key)
                    self.restart()
                    self.state = GameState.PLAYING

            elif self.state == GameState.LEADERBOARD:
                self.leaderboard.handle_event(event)
            elif self.state == GameState.ENTER_NAME:
                player_name = self.name_input.handle_event(event)

                if player_name:
                    map_name = self.level_manager.selected_level or DEFAULT_MAP_NAME

                    self.leaderboard_manager.add_score(
                        map_name, player_name, self.session.score
                    )

                    self.leaderboard.active_tab = map_name
                    self.state = GameState.LEADERBOARD
                    self.sound_manager.play_leaderboard_theme(False)

    def handle_game_events(self, event):
        if event.type == pygame.KEYDOWN:

            if self.session.game_over:
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
        if self.state != GameState.PLAYING:
            return

        if self.session.game_over:
            return

        self.session.move_timer += 1

        if self.session.move_timer < FPS // SNAKE_SPEED:
            return

        self.session.move_timer = 0

        self.snake.move()

        head = self.snake.body[0]

        if self.level_manager.is_outside_play_area(head):
            self.finish_game()
            return

        if self.level_manager.has_obstacle_collision(head):
            self.finish_game()
            return

        if head == self.food.position:
            self.sound_manager.play_food_sound()
            self.snake.grow = True
            self.snake.open_mouth()
            self.session.score += SCORE_POINT

            if self.level_manager.check_win(self.snake.body):
                self.finish_game()
                return

            self.food.respawn(self.level_manager.get_forbidden_cells(self.snake.body))

        if self.snake.check_collision():
            self.finish_game()

    def draw(self):
        if self.state in (
            GameState.PLAYING,
            GameState.ENTER_NAME,
        ):
            self.screen.blit(self.level_manager.background, (0, 0))
        else:
            self.screen.blit(self.menu.background, (0, 0))

        if self.state == GameState.MENU:
            self.menu.draw()

        elif self.state == GameState.PLAYING:
            self.food.draw(self.screen)

            self.level_manager.draw_obstacles(self.screen)

            self.snake.draw(self.screen)

            self.score_panel.draw(self.session.score)

            if self.session.game_over:
                self.game_over_overlay.draw(self.screen)
        elif self.state == GameState.LEVEL_SELECT:
            self.level_select.draw()
        elif self.state == GameState.LEADERBOARD:
            self.leaderboard.draw()
        elif self.state == GameState.ENTER_NAME:
            self.food.draw(self.screen)

            self.level_manager.draw_obstacles(self.screen)

            self.snake.draw(self.screen)

            self.score_panel.draw(self.session.score)

            self.name_input.draw()

        pygame.display.flip()

    def finish_game(self):
        map_name = self.level_manager.selected_level or DEFAULT_MAP_NAME

        if self.leaderboard_manager.is_high_score(map_name, self.session.score):
            self.name_input.start()
            self.state = GameState.ENTER_NAME

            # если побил рекорд — сразу включаем музыку лидерборда
            self.sound_manager.play_leaderboard_theme(False)

        else:
            self.session.game_over = True

            # если рекорда нет — проигрываем звук поражения
            self.sound_manager.play_game_over_sound()

    def restart(self):
        self.snake = Snake()

        self.food = Food(self.level_manager.get_food_image_path())

        self.food.respawn(self.level_manager.get_forbidden_cells(self.snake.body))

        self.session.reset()

        if not self.sound_manager.is_music_playing():
            self.sound_manager.play_main_theme()

    def quit(self):
        self.sound_manager.stop_music()
        pygame.quit()

    def apply_level(self, level_key):
        self.level_manager.load_level(level_key)

        self.food = Food(self.level_manager.get_food_image_path())

        self.food.respawn(self.level_manager.get_forbidden_cells(self.snake.body))
