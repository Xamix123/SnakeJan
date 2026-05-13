import pygame


class Button:
    def __init__(self, text, center_x, center_y, width, height, font, image, hover_image):
        self.text = text
        self.font = font

        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (center_x, center_y)

        self.image = pygame.transform.scale(image, (width, height))
        self.hover_image = pygame.transform.scale(hover_image, (width, height))

        self.text_color = (70, 45, 20)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        image = self.hover_image if self.rect.collidepoint(mouse_pos) else self.image
        screen.blit(image, self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )