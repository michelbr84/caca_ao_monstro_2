import pytest
from game import Game

def test_victory_condition(monkeypatch):
    """Testa se o jogador vence ao capturar o monstro."""
    game = Game(grid_size=5, max_turns=10)
    
    # Simula a entrada do jogador para capturar o monstro na primeira tentativa
    player_guess = game.monster.position
    print(f"Simulando captura do monstro na posição: {player_guess}")  # Adiciona o print para diagnóstico
    
    # Simula a entrada do jogador com a posição correta
    monkeypatch.setattr('builtins.input', lambda _: f'{player_guess[0]} {player_guess[1]}')
    
    # Inicia o jogo
    game.play()
    
    # Verifica se o jogador capturou o monstro antes de esgotar as tentativas
    assert game.turns_left > 0  # O jogador deve capturar o monstro antes de acabar as tentativas
    print("Jogador capturou o monstro!")  # Adiciona print para diagnóstico


def test_defeat_condition(monkeypatch):
    """Testa se o jogador perde quando o monstro escapa após esgotar as tentativas."""
    game = Game(grid_size=5, max_turns=2)  # Limita o número de turnos para 2
    
    # Simula a entrada do jogador para errar as tentativas
    print("Simulando tentativas erradas do jogador")  # Adiciona print para diagnóstico
    monkeypatch.setattr('builtins.input', lambda _: '0 0')  # Jogador sempre tenta (0, 0)
    
    # Inicia o jogo
    game.play()
    
    # Verifica se o monstro escapou após as tentativas esgotarem
    assert game.turns_left == 0  # O jogador deve perder quando as tentativas acabarem
    print("Monstro escapou e o jogador perdeu!")  # Adiciona print para diagnóstico
