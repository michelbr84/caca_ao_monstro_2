class Player:
    def __init__(self):
        """Inicializa o jogador sem posição definida."""
        self.position = None

    def guess_position(self):
        """
        Recebe a entrada do jogador para adivinhar a posição (linha, coluna).
        Solicita ao jogador que insira uma linha e coluna separadas por espaço.
        Retorna um par de inteiros (linha, coluna).
        """
        print("Esperando a entrada do jogador...")  # Para diagnóstico
        guess = input("Digite a linha e a coluna separadas por espaço: ")  # Solicita a entrada do jogador
        print(f"Entrada recebida: {guess}")  # Para diagnóstico, verifica a entrada recebida
        x, y = map(int, guess.split())  # Converte a entrada em inteiros
        return x, y

    def validate_guess(self, x, y, grid_size):
        """
        Valida se a tentativa do jogador está dentro dos limites da grade.
        Retorna True se a tentativa estiver dentro dos limites, False caso contrário.
        
        Parâmetros:
        - x (int): Coordenada da linha.
        - y (int): Coordenada da coluna.
        - grid_size (int): Tamanho da grade (por exemplo, 5 para uma grade 5x5).
        """
        return 0 <= x < grid_size and 0 <= y < grid_size
