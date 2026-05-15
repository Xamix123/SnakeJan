import pygame


class AssetManager:
    """
    Manages loading, caching, and scaling of image assets.

    The manager stores loaded images in memory to avoid loading
    the same file multiple times during the game.
    """
    def __init__(self):
        """
        Initialize the asset manager.
        """
        # Dictionary that stores loaded images by name.
        self.images = {}

    def load_image(self, name, path, alpha=True):
        """
        Load an image from disk and store it in the cache.

        Args:
            name (str): Unique key used to store the image.
            path (str): Path to the image file.
            alpha (bool): Whether to preserve transparency.

        Returns:
            pygame.Surface: Loaded image.
        """
        image = pygame.image.load(path)

        if alpha:
            image = image.convert_alpha()
        else:
            image = image.convert()

        self.images[name] = image
        return image

    def get_image(self, name):
        """
        Return a previously loaded image from the cache.

        Args:
            name (str): Image key.

        Returns:
            pygame.Surface: Cached image.
        """
        return self.images[name]

    def scale_image(self, image, size):
        """
        Scale an image to the specified size.

        Args:
            image (pygame.Surface): Source image.
            size (tuple[int, int]): Target size in pixels.

        Returns:
            pygame.Surface: Scaled image.
        """
        return pygame.transform.scale(image, size)

    def load_scaled_image(self, name, path, size, alpha=True):
        """
        Load an image, scale it, and store the scaled version.

        Args:
            name (str): Unique key used to store the image.
            path (str): Path to the image file.
            size (tuple[int, int]): Target size in pixels.
            alpha (bool): Whether to preserve transparency.

        Returns:
            pygame.Surface: Loaded and scaled image.
        """
        image = self.load_image(name, path, alpha)
        image = self.scale_image(image, size)
        self.images[name] = image
        return image
