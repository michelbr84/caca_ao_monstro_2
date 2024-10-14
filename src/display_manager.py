import pygame

class DisplayManager:
    def __init__(self, screen, assets_manager):
        self.screen = screen
        self.assets_manager = assets_manager

    def render_background(self):
        """
        Renderiza o fundo da grade.
        """
        background_image = self.assets_manager.get_image('grid_background')
        self.screen.blit(background_image, (0, 0))

    def render_player(self, position):
        """
        Renderiza o jogador na posição especificada.
        """
        player_image = self.assets_manager.get_image('player')
        self.screen.blit(player_image, position)

    def render_monster(self, position):
        """
        Renderiza o monstro na posição especificada.
        """
        monster_image = self.assets_manager.get_image('monster')
        self.screen.blit(monster_image, position)

    def render_capture_effect(self, position):
        """
        Renderiza o efeito de captura na posição do monstro.
        """
        capture_effect_image = self.assets_manager.get_image('capture_effect')
        self.screen.blit(capture_effect_image, position)

    def render_escape_effect(self, position):
        """
        Renderiza o efeito de fuga na posição do monstro.
        """
        escape_effect_image = self.assets_manager.get_image('escape_effect')
        self.screen.blit(escape_effect_image, position)

    def update_display(self):
        """
        Atualiza a tela para refletir as mudanças.
        """
        pygame.display.update()
