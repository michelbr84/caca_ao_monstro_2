import pytest
from player import Player

def test_player_initialization():
    """Testa se o jogador é inicializado corretamente sem uma posição fixa."""
    player = Player()
    print("Inicializando o jogador...")  # Adiciona print para diagnóstico
    
    assert player.position is None  # O jogador não tem uma posição fixa no início
    print("Jogador inicializado corretamente!")  # Adiciona print para diagnóstico

def test_guess_position(monkeypatch):
    """Testa se a entrada do jogador é recebida corretamente."""
    player = Player()

    # Simula a entrada do usuário (linha 2, coluna 3)
    monkeypatch.setattr('builtins.input', lambda _: '2 3')
    print("Simulando entrada do jogador: 2 3")  # Adiciona print antes de receber a entrada
    
    guess = player.guess_position()
    
    print(f"Jogador fez a tentativa: {guess}")  # Verifica se a entrada foi capturada
    
    assert guess == (2, 3)  # A entrada deve ser corretamente convertida para um par de coordenadas
    print("Entrada capturada corretamente!")  # Adiciona print para diagnóstico

def test_validate_guess():
    """Testa se a entrada do jogador é validada corretamente."""
    player = Player()

    # Testa uma entrada válida dentro da grade
    assert player.validate_guess(2, 3, 5) == True  # Posição válida dentro da grade 5x5
    print("Validação de entrada válida funcionando corretamente!")  # Adiciona print para diagnóstico

    # Testa uma entrada fora dos limites da grade
    assert player.validate_guess(5, 5, 5) == False  # Posição fora dos limites da grade
    print("Validação de entrada fora dos limites funcionando corretamente!")  # Adiciona print para diagnóstico
