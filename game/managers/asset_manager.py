import pygame


class AssetManager:
    def __init__(self):
        self.images = {}

    def load_image(self, name, path, alpha=True):
        image = pygame.image.load(path)

        if alpha:
            image = image.convert_alpha()
        else:
            image = image.convert()

        self.images[name] = image
        return image

    def get_image(self, name):
        return self.images[name]

    def scale_image(self, image, size):
        return pygame.transform.scale(image, size)

    def load_scaled_image(self, name, path, size, alpha=True):
        image = self.load_image(name, path, alpha)
        image = self.scale_image(image, size)
        self.images[name] = image
        return image