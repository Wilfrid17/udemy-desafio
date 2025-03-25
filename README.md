# Jogo de Tradução

## Descrição
Este é um jogo educativo desenvolvido em Python usando a biblioteca Pygame. O objetivo é testar e aprimorar o conhecimento do jogador em tradução de palavras entre português e inglês. O jogador deve selecionar a categoria de palavras e responder corretamente dentro do tempo limite de 10 segundos.

## Tecnologias Utilizadas
- Python
- Pygame
- Random
- Time
- OS
- SYS

## Como Jogar
1. Ao iniciar o jogo, o jogador deve selecionar uma categoria de palavras (Animais, Objetos, Natureza ou Números).
2. Uma palavra em português será exibida e o jogador deve selecionar a tradução correta entre quatro opções.
3. Cada resposta correta aumenta a pontuação.
4. O jogador tem 10 segundos para responder cada pergunta.
5. O jogo salva automaticamente a pontuação acumulada.

## Instalação
### Requisitos
- Python 3.x instalado
- Biblioteca Pygame instalada

### Passos para instalar
1. Clone ou baixe o repositório.
2. Instale o Pygame executando o seguinte comando:
   ```sh
   pip install pygame
   ```
3. Execute o arquivo principal do jogo:
   ```sh
   python main.py
   ```

## Estrutura do Código
O código é estruturado em diferentes seções:
- **Importação de Bibliotecas**: Importa as bibliotecas necessárias.
- **Definição de Cores e Tela**: Define as cores em RGB e cria a janela do jogo.
- **Definição de Fontes e Variáveis**: Configura fontes de texto e variáveis iniciais.
- **Banco de Palavras**: Dicionário contendo palavras e suas traduções.
- **Funções Principais**:
  - `carregar_pontuacao()`: Lê a pontuação salva do arquivo.
  - `salvar_pontuacao()`: Salva a pontuação atual no arquivo.
  - `nova_pergunta()`: Seleciona uma palavra aleatória e gera opções de resposta.
  - `exibir_texto()`: Renderiza e exibe textos na tela.
  - `menu_categorias()`: Exibe a tela de seleção de categoria.
  - `menu_inicial()`: Exibe a tela inicial do jogo.
  - `jogo()`: Controla a lógica principal do jogo.

## Controles
- **Mouse**: Clique nas opções de resposta para selecionar a tradução correta.
- **Botão Fechar**: Fecha o jogo.

## Melhorias Futuras
- Adição de mais categorias de palavras.
- Implementação de níveis de dificuldade.
- Modo multiplayer.
- Sons e efeitos visuais aprimorados.
- Adicionar suporte a diferentes idiomas além do inglês e português.

## Autor
Desenvolvido por [Seu Nome].

## Licença
Este projeto está licenciado sob a MIT License.

