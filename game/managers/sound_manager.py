import pygame

from configs.audio import (
    MAIN_THEME_PATH,
    LEADERBOARD_THEME_PATH,
    FOOD_EAT_SOUND_PATH,
    GAME_OVER_SOUND_PATH,
    DEFAULT_SOUND_VOLUME,
    DEFAULT_MUSIC_VOLUME,
    MUSIC_LOOP,
)


class SoundManager:
    """
    Manages all audio in the game.

    The manager is responsible for:
    - initializing the pygame mixer;
    - loading sound effects;
    - playing background music;
    - playing sound effects;
    - controlling music and sound volumes.
    """
    def __init__(self):
        """
        Initialize the sound manager and preload sound effects.
        """
        # Initialize pygame audio subsystem.
        pygame.mixer.init()
        # Identifier of the currently playing music track.
        self.current_music = None
        
        # Preload sound effects.
        self.sounds = {
            "food": pygame.mixer.Sound(FOOD_EAT_SOUND_PATH),
            "game_over": pygame.mixer.Sound(GAME_OVER_SOUND_PATH),
        }

        # Apply default volume to all sound effects.
        for sound in self.sounds.values():
            sound.set_volume(DEFAULT_SOUND_VOLUME)

    def play_music(self, path, loop=True):
        """
        Load and play background music.

        Args:
            path (str): Path to the music file.
            loop (bool): Whether to loop the music indefinitely.
        """
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(DEFAULT_MUSIC_VOLUME)
        pygame.mixer.music.play(
            MUSIC_LOOP if loop else 0
        )
    def play_main_theme(self):
        """
        Play the main menu theme.
        """
        self.play_music(MAIN_THEME_PATH)
        self.current_music = "main_theme"

    def play_leaderboard_theme(self, restart=True):
        """
        Play the leaderboard theme.

        Args:
            restart (bool):
                If False and the leaderboard music is already playing,
                the track will not restart.
        """
        if self.current_music == "leaderboard" and not restart:
            return

        pygame.mixer.music.load(LEADERBOARD_THEME_PATH)
        pygame.mixer.music.play(MUSIC_LOOP)
        self.current_music = "leaderboard"

    def stop_music(self):
        """
        Stop the currently playing music.
        """
        pygame.mixer.music.stop()

    def is_music_playing(self):
        """
        Check whether music is currently playing.

        Returns:
            bool: True if music is playing.
        """
        return pygame.mixer.music.get_busy()

    def play_sound(self, name):
        """
        Play a sound effect by name.

        Args:
            name (str): Sound identifier.
        """
        if name in self.sounds:
            self.sounds[name].play()

    def play_food_sound(self):
        """
        Play the food consumption sound effect.
        """
        self.play_sound("food")

    def play_game_over_sound(self):
        """
        Play the game over sound effect.
        """
        self.play_sound("game_over")

    def set_music_volume(self, volume):
        """
        Set the background music volume.

        Args:
            volume (float): Volume in range 0.0 to 1.0.
        """
        self.music_volume = volume
        pygame.mixer.music.set_volume(volume)

    def set_sound_volume(self, volume):
        """
        Set the volume for all sound effects.

        Args:
            volume (float): Volume in range 0.0 to 1.0.
        """
        self.sound_volume = volume
        for sound in self.sounds.values():
            sound.set_volume(volume)
