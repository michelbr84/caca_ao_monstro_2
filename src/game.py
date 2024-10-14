import pygame
from player import Player
from monster import Monster
from grid import Grid
from assets_manager import AssetsManager  # Importa o AssetsManager para gerenciar imagens
from sounds_manager import SoundsManager  # Importa o SoundsManager para gerenciar sons

class Game:
    def __init__(self, grid_size=5, max_turns=10, difficulty="medium"):
        """
        Inicializa o jogo com a grade, jogador, monstro, assets, sons e o número máximo de turnos.
        A dificuldade afeta o número de turnos e quando o monstro pode escapar.
        """
        # Inicializa Pygame
        pygame.init()

        # Configura a tela (cada célula será de 64x64 pixels)
        self.cell_size = 64  # Tamanho de cada célula da grade
        self.screen_size = (grid_size * self.cell_size, grid_size * self.cell_size)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Caça ao Monstro 2")

        # Inicializa o AssetsManager e carrega as imagens
        self.assets_manager = AssetsManager()
        self.assets_manager.load_images()

        # Inicializa o SoundsManager e carrega os sons
        self.sounds_manager = SoundsManager()
        self.sounds_manager.load_sounds()

        # Redimensiona as imagens para o tamanho de 64x64 pixels
        self.player_image = pygame.transform.scale(self.assets_manager.get_image('player'), (self.cell_size, self.cell_size))
        self.monster_image = pygame.transform.scale(self.assets_manager.get_image('monster'), (self.cell_size, self.cell_size))
        self.grid_background = pygame.transform.scale(self.assets_manager.get_image('grid_background'), self.screen_size)

        self.grid_size = grid_size
        self.grid = Grid(self.grid_size)
        self.player = Player()
        self.monster = Monster(self.grid_size)

        # Configurações de dificuldade ajustam o número de turnos e tempo de escapada do monstro
        self.set_difficulty(difficulty, max_turns)

        # Inicia a música de fundo
        self.sounds_manager.play_music()

    def set_difficulty(self, difficulty, max_turns):
        """
        Ajusta o número de turnos e o tempo de escapada do monstro com base na dificuldade.
        """
        if difficulty == "easy":
            self.turns_left = max_turns + 5  # Mais turnos no modo fácil
            self.escape_turn = int(self.turns_left / 2) + 3  # O monstro demora mais para escapar
        elif difficulty == "hard":
            self.turns_left = max_turns - 2  # Menos turnos no modo difícil
            self.escape_turn = int(self.turns_left / 2) - 1  # O monstro escapa mais rápido
        else:
            self.turns_left = max_turns  # Configuração padrão (modo médio)
            self.escape_turn = int(self.turns_left / 2)

    def show_title_screen(self):
        """
        Exibe a tela de título e o menu inicial.
        """
        title_font = pygame.font.Font(None, 60)  # Ajuste do tamanho da fonte
        menu_font = pygame.font.Font(None, 50)

        title_text = title_font.render("Caça ao Monstro 2", True, (255, 255, 255))
        start_text = menu_font.render("1. Iniciar Jogo", True, (255, 255, 255))
        quit_text = menu_font.render("2. Sair", True, (255, 255, 255))

        running = True
        while running:
            self.screen.fill((0, 0, 0))  # Fundo preto

            # Centraliza o texto na tela
            title_rect = title_text.get_rect(center=(self.screen_size[0] // 2, self.screen_size[1] // 4))
            start_rect = start_text.get_rect(center=(self.screen_size[0] // 2, self.screen_size[1] // 2))
            quit_rect = quit_text.get_rect(center=(self.screen_size[0] // 2, (self.screen_size[1] // 2) + 50))

            # Desenha o texto
            self.screen.blit(title_text, title_rect)
            self.screen.blit(start_text, start_rect)
            self.screen.blit(quit_text, quit_rect)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        return "start"  # Jogador escolhe iniciar o jogo
                    elif event.key == pygame.K_2:
                        pygame.quit()
                        quit()  # Jogador escolhe sair

    def play(self):
        """
        Inicia o loop principal do jogo.
        O jogador faz tentativas, e o monstro se move após cada tentativa errada.
        """
        result = self.show_title_screen()

        if result == "start":
            print(f"Bem-vindo ao Caça ao Monstro! Tente capturar o monstro em até {self.turns_left} tentativas.")
            print("Dica: O monstro pode tentar escapar após metade dos turnos!\n")

            running = True
            while self.turns_left > 0 and running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                # Obtém a tentativa do jogador
                guess = self.get_player_guess()

                # Verifica se o jogador capturou o monstro
                if self.check_capture(guess):
                    print("Parabéns! Você capturou o monstro!")
                    self.sounds_manager.play_sound('capture')  # Toca o som de captura
                    self.render_capture_effect(guess)
                    self.show_feedback_message("Você capturou o monstro!")
                    break

                # Fornece feedback sobre a proximidade do monstro
                self.give_feedback(self.calculate_distance(guess, self.monster.position))

                # O monstro se move após cada tentativa falha
                self.monster.move(self.grid_size)
                self.sounds_manager.play_sound('move')  # Toca o som de movimento

                # Renderizar o jogo (imagens do jogador, monstro e grade)
                self.render_game(guess)

                # Reduz o número de tentativas restantes
                self.turns_left -= 1
                print(f"Tentativas restantes: {self.turns_left}\n")

                if self.turns_left == 0:
                    print("Você perdeu! O monstro escapou.\n")
                    self.sounds_manager.play_sound('escape')  # Toca o som de fuga
                    self.render_escape_effect(self.monster.position)
                    self.show_feedback_message("O monstro escapou!")

            pygame.quit()

    def get_player_guess(self):
        """
        Obtém a tentativa do jogador e garante que ela esteja dentro dos limites da grade.
        """
        while True:
            guess = self.player.guess_position()
            if self.player.validate_guess(guess[0], guess[1], self.grid_size):
                return guess
            print("Tentativa fora dos limites. Tente novamente.\n")

    def check_capture(self, player_pos: tuple) -> bool:
        """
        Verifica se o jogador capturou o monstro.
        """
        return player_pos == self.monster.position

    def calculate_distance(self, player_pos: tuple, monster_pos: tuple) -> int:
        """
        Calcula a distância Manhattan entre o jogador e o monstro.
        """
        return abs(player_pos[0] - monster_pos[0]) + abs(player_pos[1] - monster_pos[1])

    def give_feedback(self, distance: int):
        """
        Fornece feedback ao jogador sobre a proximidade do monstro.
        Quanto menor a distância, mais perto o jogador está.
        """
        feedback_messages = {
            0: "Você capturou o monstro!",
            1: "Você está muito perto! Continue atento!",
            2: "Você está perto! O monstro está a uma curta distância!",
            3: "Você está no caminho certo, o monstro está relativamente próximo.",
            4: "Você está no caminho certo, o monstro está relativamente próximo.",
            5: "Você está se afastando, o monstro está um pouco mais longe.",
            6: "Você está se afastando, o monstro está um pouco mais longe.",
        }

        # Escolher a mensagem com base na distância
        print(feedback_messages.get(distance, "Você está muito longe! O monstro está longe de sua posição atual."))

    def render_game(self, player_position):
        """
        Renderiza a tela do jogo com o fundo, jogador e monstro.
        """
        # Renderiza o fundo da grade redimensionado
        self.screen.blit(self.grid_background, (0, 0))

        # Renderiza o jogador na posição correta, redimensionado para 64x64 pixels
        self.screen.blit(self.player_image, (player_position[0] * self.cell_size, player_position[1] * self.cell_size))

        # Renderiza o monstro na posição correta, redimensionado para 64x64 pixels
        self.screen.blit(self.monster_image, (self.monster.position[0] * self.cell_size, self.monster.position[1] * self.cell_size))

        # Atualiza a tela para mostrar as alterações
        pygame.display.update()

    def render_capture_effect(self, position):
        """
        Renderiza o efeito de captura na posição do monstro.
        """
        capture_effect = pygame.transform.scale(self.assets_manager.get_image('capture_effect'), (self.cell_size, self.cell_size))
        if capture_effect:
            self.screen.blit(capture_effect, (position[0] * self.cell_size, position[1] * self.cell_size))
        pygame.display.update()

    def render_escape_effect(self, position):
        """
        Renderiza o efeito de fuga na posição do monstro.
        """
        escape_effect = pygame.transform.scale(self.assets_manager.get_image('escape_effect'), (self.cell_size, self.cell_size))
        if escape_effect:
            self.screen.blit(escape_effect, (position[0] * self.cell_size, position[1] * self.cell_size))
        pygame.display.update()

    def show_feedback_message(self, message):
        """
        Exibe uma mensagem de feedback no centro da tela, por exemplo, quando o monstro é capturado ou escapa.
        """
        font = pygame.font.Font(None, 40)
        text = font.render(message, True, (255, 255, 255))
        self.screen.fill((0, 0, 0))  # Limpa a tela
        self.screen.blit(text, (self.screen_size[0] // 2 - text.get_width() // 2, self.screen_size[1] // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(3000)  # Exibe a mensagem por 3 segundos


# Iniciar o jogo com escolha de dificuldade e tamanho da grade
if __name__ == "__main__":
    print("Escolha a dificuldade: fácil, médio ou difícil")
    difficulty = input("Digite a dificuldade desejada: ").lower()

    print("Escolha o tamanho da grade (mínimo 3x3, máximo 10x10):")
    grid_size = int(input("Digite o tamanho da grade: "))
    grid_size = max(3, min(grid_size, 10))  # Limita a grade entre 3 e 10

    jogo = Game(grid_size=grid_size, difficulty=difficulty)
    jogo.play()
