import pytest
from grid import Grid

def test_grid_creation():
    """Testa se a grade é criada corretamente com o tamanho certo."""
    grid_size = 5
    grid = Grid(grid_size)
    
    assert len(grid.grid) == grid_size  # A grade deve ter o número correto de linhas
    assert len(grid.grid[0]) == grid_size  # Cada linha da grade deve ter o número correto de colunas

def test_is_valid_position():
    """Testa se as posições são validadas corretamente."""
    grid_size = 5
    grid = Grid(grid_size)
    
    assert grid.is_valid_position(0, 0) == True  # Posição válida no canto superior esquerdo
    assert grid.is_valid_position(4, 4) == True  # Posição válida no canto inferior direito
    assert grid.is_valid_position(5, 5) == False  # Posição fora dos limites

def test_update_positions():
    """Testa se as posições do jogador e do monstro são atualizadas corretamente na grade."""
    grid_size = 5
    grid = Grid(grid_size)
    player_pos = (1, 1)
    monster_pos = (3, 3)
    
    grid.update_positions(player_pos, monster_pos)
    
    assert grid.grid[1][1] == 'P'  # Posição do jogador
    assert grid.grid[3][3] == 'M'  # Posição do monstro
