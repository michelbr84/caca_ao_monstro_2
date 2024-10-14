import os
import pygame

class AssetsManager:
    def __init__(self):
        """
        Inicializa o dicionário para armazenar as imagens carregadas.
        """
        self.images = {}
        self.assets_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images')

    def load_images(self):
        """
        Carrega as imagens do diretório 'assets/images' e armazena no dicionário 'images'.
        """
        try:
            # Usando o caminho absoluto para carregar as imagens
            self.images['player'] = self.load_image('player.png')
            self.images['monster'] = self.load_image('monster.png')
            self.images['grid_background'] = self.load_image('grid_background.png')
            self.images['capture_effect'] = self.load_image('capture_effect.png')
            self.images['escape_effect'] = self.load_image('escape_effect.png')

            print("Imagens carregadas com sucesso.")
        
        except pygame.error as e:
            print(f"Erro ao carregar as imagens: {e}")

    def load_image(self, image_name):
        """
        Carrega uma imagem a partir do nome do arquivo.
        
        :param image_name: Nome do arquivo da imagem a ser carregada.
        :return: Imagem carregada.
        """
        image_path = os.path.join(self.assets_path, image_name)
        if os.path.exists(image_path):
            return pygame.image.load(image_path).convert_alpha()
        else:
            print(f"Erro: Imagem '{image_name}' não encontrada no caminho: {image_path}")
            return None

    def get_image(self, name):
        """
        Retorna a imagem correspondente ao nome fornecido.
        
        :param name: Nome da imagem a ser retornada.
        :return: A imagem correspondente ao nome, ou None se não existir.
        """
        return self.images.get(name)
