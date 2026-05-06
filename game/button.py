import pygame


class Button:
    def __init__(self, text, center_x, center_y, width, height, font):
        self.text = text
        self.font = font

        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (center_x, center_y)

        self.color = (220, 220, 220)
        self.hover_color = (180, 180, 180)
        self.text_color = (0, 0, 0)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            color = self.hover_color
        else:
            color = self.color

        pygame.draw.rect(screen, color, self.rect, border_radius=15)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )