import pygame
from snake import Snake
from food import Food
from button import Button

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
    BACKGROUND_COLOR,
    GRID_COLOR
)


class Game:
    def __init__(self):
        self.state = "menu"
        self.menu_font = pygame.font.SysFont("Arial", 48)

        button_width = WINDOW_WIDTH // 3
        button_height = 70
        center_x = WINDOW_WIDTH // 2

        start_y = WINDOW_HEIGHT // 2 - 150
        gap = 90

        self.buttons = {
            "play": Button("Play", center_x, start_y, button_width, button_height, self.menu_font),
            "settings": Button("Settings", center_x, start_y + gap, button_width, button_height, self.menu_font),
            "records": Button("Leaderboard", center_x, start_y + gap * 2, button_width, button_height, self.menu_font),
            "exit": Button("Exit", center_x, start_y + gap * 3, button_width, button_height, self.menu_font),
        }
        
        pygame.init()

        self.screen = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            pygame.FULLSCREEN
        )
        pygame.display.set_caption("Snake")

        self.clock = pygame.time.Clock()
        self.running = True
        self.snake = Snake()
        self.food = Food()
        self.game_over = False
        self.font = pygame.font.SysFont("Arial", 48)
        self.score = 0
        self.score_font = pygame.font.SysFont("Arial", 32)
        self.move_timer = 0

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
                    if self.state == "playing":
                        self.state = "menu"
                    else:
                        self.running = False

                elif event.key == pygame.K_r and self.game_over:
                    self.restart()

            if self.state == "menu":
                self.handle_menu_events(event)

            elif self.state == "playing":
                self.handle_game_events(event)


    def handle_menu_events(self, event):
        if self.buttons["play"].is_clicked(event):
            self.restart()
            self.state = "playing"

        elif self.buttons["settings"].is_clicked(event):
            print("Настройки пока не реализованы")

        elif self.buttons["records"].is_clicked(event):
            print("Рекорды пока не реализованы")

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
            self.snake.grow = True
            self.score += 1
            self.food.respawn()

        if self.snake.check_collision():
            self.game_over = True
            
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)

        if self.state == "menu":
            self.draw_menu()

        elif self.state == "playing":
            self.draw_grid()

            self.food.draw(self.screen)
            self.snake.draw(self.screen)

            self.draw_score()

            if self.game_over:
                self.draw_game_over()

        pygame.display.flip()

    def draw_menu(self):
        title_font = pygame.font.SysFont("Arial", 72)

        title = title_font.render("SNAKE", True, (0, 0, 0))
        title_rect = title.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 280)
        )

        self.screen.blit(title, title_rect)

        for button in self.buttons.values():
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
        text = self.font.render(
            "GAME OVER | R - restart",
            True,
            (0, 0, 0)
        )

        text_rect = text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        )

        self.screen.blit(text, text_rect)
    
    def draw_score(self):
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
        
    def quit(self):
        pygame.quit()