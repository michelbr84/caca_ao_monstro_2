class Grid:
    def __init__(self, size: int):
        """
        Inicializa a grade de tamanho size x size.
        """
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]  # Cria uma grade vazia 5x5

    def is_valid_position(self, x: int, y: int) -> bool:
        """
        Verifica se a posição (x, y) está dentro dos limites da grade.
        """
        return 0 <= x < self.size and 0 <= y < self.size

    def update_positions(self, player_pos: tuple, monster_pos: tuple):
        """
        Atualiza as posições do jogador e do monstro na grade (opcional).
        """
        # Primeiro, limpa a grade
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]

        # Atualiza a grade com as novas posições
        px, py = player_pos
        mx, my = monster_pos
        self.grid[px][py] = 'P'  # 'P' para o jogador
        self.grid[mx][my] = 'M'  # 'M' para o monstro

    def display(self):
        """
        Exibe a grade no terminal.
        """
        for row in self.grid:
            print(" | ".join([str(cell) if cell is not None else "." for cell in row]))
            print("-" * (self.size * 4 - 1))
