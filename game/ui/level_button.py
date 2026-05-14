import pygame


class LevelButton:
    def __init__(self, level_key, image, hover_image, x, y, size):
        self.level_key = level_key

        self.image = pygame.transform.scale(image, (size, size))
        self.hover_image = pygame.transform.scale(hover_image, (size, size))
        self.rect = pygame.Rect(x, y, size, size)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.hover_image, self.rect)
        else:
            screen.blit(self.image, self.rect)

    def is_clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )
