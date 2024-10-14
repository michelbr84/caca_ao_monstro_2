import pytest
from monster import Monster

def test_monster_initial_position():
    """Testa se o monstro é posicionado aleatoriamente na grade."""
    grid_size = 5
    monster = Monster(grid_size)
    
    x, y = monster.position
    assert 0 <= x < grid_size  # A posição inicial deve estar dentro dos limites da grade
    assert 0 <= y < grid_size

def test_monster_movement():
    """Testa se o monstro se move para uma nova posição aleatória dentro da grade."""
    grid_size = 5
    monster = Monster(grid_size)
    initial_position = monster.position
    
    monster.move(grid_size)
    new_position = monster.position
    
    assert new_position != initial_position  # A nova posição deve ser diferente da posição inicial
    assert 0 <= new_position[0] < grid_size  # A nova posição deve estar dentro dos limites da grade
    assert 0 <= new_position[1] < grid_size
