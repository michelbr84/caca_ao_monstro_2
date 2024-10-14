import random

def is_within_bounds(x: int, y: int, grid_size: int) -> bool:
    """
    Verifica se as coordenadas (x, y) estão dentro dos limites da grade.
    """
    return 0 <= x < grid_size and 0 <= y < grid_size

def generate_random_position(grid_size: int) -> tuple:
    """
    Gera uma nova posição aleatória dentro dos limites da grade.
    """
    x = random.randint(0, grid_size - 1)
    y = random.randint(0, grid_size - 1)
    return (x, y)

def calculate_manhattan_distance(pos1: tuple, pos2: tuple) -> int:
    """
    Calcula a distância Manhattan entre duas posições (pos1 e pos2).
    A distância Manhattan é a soma das diferenças absolutas entre as coordenadas.
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def validate_input(input_str: str, grid_size: int) -> tuple:
    """
    Valida se a entrada do jogador é numérica e se está dentro dos limites da grade.
    Exemplo de entrada válida: "2 3" para linha 2, coluna 3.
    Retorna uma tupla (x, y) se for válida, ou None se for inválida.
    """
    try:
        x, y = map(int, input_str.split())
        if is_within_bounds(x, y, grid_size):
            return (x, y)
        else:
            print(f"Coordenadas fora dos limites! Deve ser entre 0 e {grid_size - 1}.")
    except ValueError:
        print("Entrada inválida! Por favor, digite dois números inteiros separados por espaço.")
    return None
