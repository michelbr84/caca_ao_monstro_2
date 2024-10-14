
# Caça ao Monstro 2

## Descrição

**Caça ao Monstro 2** é a continuação do jogo clássico de adivinhação "Caça ao Monstro". Nesta nova versão, o jogo inclui gráficos e sons, além de ajustes de dificuldade para proporcionar uma experiência mais dinâmica e divertida. O objetivo continua o mesmo: capturar o monstro antes que ele escape, mas agora o jogador pode se guiar por dicas visuais e auditivas, e o monstro pode tentar fugir!

## Novos Recursos

- **Gráficos em Tela**: Agora o jogador e o monstro são representados por imagens em uma grade visível.
- **Sons e Música de Fundo**: O jogo inclui efeitos sonoros para movimentação, captura, fuga, e uma música de fundo para criar uma atmosfera mais envolvente.
- **Ajustes de Dificuldade**: Três níveis de dificuldade (fácil, médio, difícil) que ajustam o número de turnos, a velocidade do monstro e o tempo até o monstro tentar escapar.
- **Mensagens de Feedback**: Mensagens visuais claras são exibidas para informar o jogador sobre a proximidade do monstro, a captura ou a fuga.

## Como Instalar

### Pré-requisitos

- **Python 3.8 ou superior** deve estar instalado no seu sistema.
- Dependências adicionais estão listadas no arquivo `requirements.txt`.

### Instalação do Projeto

1. **Clone o Repositório**:

   
   git clone https://github.com/SEU_USUARIO/caca_ao_monstro_2.git
   cd caca_ao_monstro_2
   

2. **Crie e Ative um Ambiente Virtual** (opcional, mas recomendado):

   No Windows:
   
   python -m venv venv
   .\venv\Scripts\activate
   

   No macOS/Linux:
   
   python3 -m venv venv
   source venv/bin/activate
   

3. **Instale as Dependências**:

   Use o arquivo `requirements.txt` para instalar as bibliotecas necessárias, incluindo o Pygame:

   
   pip install -r requirements.txt
   

### Dependências Principais

- **Pygame**: Usado para renderizar os gráficos e tocar os sons.
- **Python**: Versão 3.8 ou superior.

Se precisar instalar o **Pygame** manualmente:


pip install pygame


## Como Jogar

### Iniciar o Jogo

1. **Execute o Jogo**:

   Navegue até a pasta `src` e execute o jogo:

   
   cd src
   python game.py
   

2. **Tela de Título e Menu**:

   Você será apresentado à tela de título, onde pode selecionar:

   - `1. Iniciar Jogo`: Começar uma nova partida.
   - `2. Sair`: Fechar o jogo.

   Para selecionar, basta digitar o número correspondente (1 ou 2) no teclado.

3. **Escolha a Dificuldade**:

   Depois de selecionar `Iniciar Jogo`, você escolherá a dificuldade do jogo:

   - **Fácil**: Mais turnos disponíveis, e o monstro demora mais para escapar.
   - **Médio**: Configuração equilibrada para uma experiência padrão.
   - **Difícil**: Menos turnos e o monstro escapa mais rapidamente.

   Digite a dificuldade desejada (fácil, médio ou difícil).

4. **Escolha o Tamanho da Grade**:

   O próximo passo é escolher o tamanho da grade em que o monstro se moverá. O tamanho mínimo é 3x3 e o máximo é 10x10. Digite o valor desejado e o jogo começará.

### Jogabilidade

- **Objetivo**: Capture o monstro antes que ele escape ou que suas tentativas acabem.
- **Movimentos**: Digite as coordenadas da linha e coluna separadas por espaço (exemplo: `2 3`) para tentar capturar o monstro.
- **Dicas e Feedback**: 
  - O jogo fornecerá dicas sobre a proximidade do monstro com base na sua tentativa, com mensagens visuais e sonoras.
  - Quanto mais perto do monstro, mais intensas serão as dicas.
- **Movimento do Monstro**: O monstro se moverá após cada tentativa errada, e tentará escapar após metade dos turnos.

## Exemplos de Jogabilidade

### Iniciando o Jogo:


Jogo está iniciando...
Escolha a dificuldade: fácil, médio ou difícil
Digite a dificuldade desejada: médio
Escolha o tamanho da grade (mínimo 3x3, máximo 10x10):
Digite o tamanho da grade: 5
Bem-vindo ao Caça ao Monstro! Tente capturar o monstro em até 10 tentativas.


### Exemplo de Palpite:


Digite a linha e a coluna separadas por espaço: 2 3
Você está perto! Continue tentando.
Tentativas restantes: 9


### Exemplo de Captura:


Parabéns! Você capturou o monstro!


### Exemplo de Fuga:


O monstro escapou! Você perdeu!


## Recursos de Mídia

Os arquivos de mídia, como **imagens** e **sons**, estão armazenados na pasta `assets/`.

- **Imagens**:
  - `player.png`: Imagem que representa o jogador.
  - `monster.png`: Imagem do monstro que deve ser capturado.
  - `grid_background.png`: Imagem do fundo da grade.
  - `capture_effect.png`: Efeito visual para a captura do monstro.
  - `escape_effect.png`: Efeito visual para quando o monstro escapa.

- **Sons**:
  - `background_music.mp3`: Música de fundo tocada durante o jogo.
  - `move_sound.wav`: Som que toca quando o monstro ou o jogador se movem.
  - `capture_sound.wav`: Som para quando o monstro é capturado.
  - `escape_sound.wav`: Som tocado quando o monstro escapa.

## Guia para Personalização de Imagens e Sons

Se você deseja modificar as imagens e sons do jogo, siga os passos abaixo:

### Personalizando as Imagens

1. Navegue até a pasta `assets/images/` e substitua qualquer uma das imagens existentes pelos seus próprios arquivos.
2. As imagens precisam seguir o mesmo nome de arquivo para serem reconhecidas pelo jogo. Por exemplo:
   - `player.png` (representa o jogador)
   - `monster.png` (representa o monstro)
3. As imagens precisam estar no formato `.png` e de preferência ter o tamanho original (1024x1024) para garantir boa qualidade de renderização.
4. Se desejar usar imagens com tamanhos diferentes, você pode ajustar o código no arquivo `assets_manager.py` para redimensionar as imagens carregadas.

### Personalizando os Sons

1. Navegue até a pasta `assets/sounds/` e substitua qualquer um dos arquivos de som pelos seus próprios.
2. Certifique-se de que os novos arquivos mantenham o mesmo nome, como:
   - `background_music.mp3` (música de fundo)
   - `move_sound.wav` (som de movimento)
   - `capture_sound.wav` (som de captura)
   - `escape_sound.wav` (som de fuga)
3. Os arquivos de som devem estar nos formatos `.mp3` ou `.wav` para garantir compatibilidade.

### Nota:
- Se você adicionar novos sons ou imagens, será necessário atualizar o código em `assets_manager.py` e `sounds_manager.py` para incluir e gerenciar esses novos recursos.
- Teste sempre a qualidade visual e auditiva após a substituição dos arquivos para garantir uma boa experiência de jogo.

## Contribuição

Se você deseja contribuir com o projeto, siga os passos abaixo:

1. Faça um **fork** do projeto.
2. Crie uma nova **branch** para sua funcionalidade ou correção.
3. Envie um **pull request** quando sua contribuição estiver pronta.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
