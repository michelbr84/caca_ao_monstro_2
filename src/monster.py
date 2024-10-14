import random

class Monster:
    def __init__(self, grid_size: int):
        """
        Inicializa o monstro em uma posição aleatória dentro da grade.
        """
        self.position = self.generate_random_position(grid_size)

    def generate_random_position(self, grid_size: int) -> tuple:
        """
        Gera uma nova posição aleatória dentro dos limites da grade.
        """
        x = random.randint(0, grid_size - 1)
        y = random.randint(0, grid_size - 1)
        return (x, y)

    def move(self, grid_size: int):
        """
        Move o monstro para uma nova posição aleatória na grade.
        Atualiza a posição do monstro.
        """
        self.position = self.generate_random_position(grid_size)
