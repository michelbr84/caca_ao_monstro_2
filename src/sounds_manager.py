import pygame

class SoundsManager:
    def __init__(self):
        """
        Inicializa o gerenciador de sons.
        """
        pygame.mixer.init()  # Inicializa o mixer de sons do Pygame
        self.sounds = {}
        self.music_volume = 0.5  # Volume padrão da música de fundo
        self.effects_volume = 0.7  # Volume padrão dos efeitos sonoros

    def load_sounds(self):
        """
        Carrega todos os sons necessários para o jogo.
        """
        self.sounds['capture'] = pygame.mixer.Sound('assets/sounds/capture_sound.wav')
        self.sounds['escape'] = pygame.mixer.Sound('assets/sounds/escape_sound.wav')
        self.sounds['move'] = pygame.mixer.Sound('assets/sounds/move_sound.wav')

        # Configura o volume para os efeitos sonoros
        self.sounds['capture'].set_volume(self.effects_volume)
        self.sounds['escape'].set_volume(self.effects_volume)
        self.sounds['move'].set_volume(self.effects_volume)

    def play_music(self, music_file='assets/sounds/background_music.mp3'):
        """
        Toca a música de fundo em loop contínuo.
        """
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.set_volume(self.music_volume)  # Configura o volume da música de fundo
        pygame.mixer.music.play(-1)  # Toca a música em loop infinito

    def stop_music(self):
        """
        Para a reprodução da música de fundo.
        """
        pygame.mixer.music.stop()

    def play_sound(self, sound_name):
        """
        Toca um som de efeito com base no nome fornecido.
        """
        if sound_name in self.sounds:
            self.sounds[sound_name].play()
        else:
            print(f"Erro: Som '{sound_name}' não encontrado.")

    def set_music_volume(self, volume):
        """
        Ajusta o volume da música de fundo.
        """
        self.music_volume = volume
        pygame.mixer.music.set_volume(self.music_volume)

    def set_effects_volume(self, volume):
        """
        Ajusta o volume dos efeitos sonoros.
        """
        self.effects_volume = volume
        for sound in self.sounds.values():
            sound.set_volume(self.effects_volume)