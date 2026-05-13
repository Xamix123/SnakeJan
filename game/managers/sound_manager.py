import pygame

from settings import (
    MAIN_THEME_PATH,
    LEADERBOARD_THEME_PATH,
    FOOD_EAT_SOUND_PATH,
    GAME_OVER_SOUND_PATH,
    DEFAULT_SOUND_VOLUME,
    DEFAULT_MUSIC_VOLUME,
    MUSIC_LOOP
)

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.current_music = None

        self.sounds = {
            "food": pygame.mixer.Sound(FOOD_EAT_SOUND_PATH),
            "game_over": pygame.mixer.Sound(GAME_OVER_SOUND_PATH),
        }

        for sound in self.sounds.values():
            sound.set_volume(DEFAULT_SOUND_VOLUME)

    def play_music(self, path, loop=True):
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(DEFAULT_MUSIC_VOLUME)
        pygame.mixer.music.play(MUSIC_LOOP if loop else 0) #TODO endless play music in loop

    def play_main_theme(self):
        self.play_music(MAIN_THEME_PATH)
        self.current_music = "main_theme"

    def play_leaderboard_theme(self, restart=True):
        if self.current_music == "leaderboard" and not restart:
            return

        pygame.mixer.music.load(LEADERBOARD_THEME_PATH)
        pygame.mixer.music.play(-1)
        self.current_music = "leaderboard"

    def stop_music(self):
        pygame.mixer.music.stop()

    def is_music_playing(self):
        return pygame.mixer.music.get_busy()

    def play_sound(self, name):
        if name in self.sounds:
            self.sounds[name].play()

    def play_food_sound(self):
        self.play_sound("food")

    def play_game_over_sound(self):
        self.play_sound("game_over")

    def set_music_volume(self, volume):
        self.music_volume = volume
        pygame.mixer.music.set_volume(volume)

    def set_sound_volume(self, volume):
        self.sound_volume = volume
        for sound in self.sounds.values():
            sound.set_volume(volume)