# Esse símbolo '#' é usado para escrever comentários, que são explicações para humanos.
# O computador ignora tudo que vem depois do '#' na mesma linha.

# Essa linha diz ao computador para pegar a biblioteca Pygame, que é como uma caixa de ferramentas para fazer jogos com gráficos.
import pygame

# Aqui pegamos a biblioteca random, que ajuda a escolher coisas de forma aleatória, como palavras para o jogo.
import random

# Essa biblioteca time serve para lidar com o tempo, como contar os segundos que o jogador tem para responder.
import time

# A biblioteca os ajuda a trabalhar com arquivos no computador, como salvar a pontuação do jogador.
import os

# A biblioteca sys dá controle sobre o programa, como fechar o jogo quando o jogador quiser.
import sys

# Essa linha ativa todas as ferramentas do Pygame para que possamos usá-las no jogo.
pygame.init()

# Aqui definimos algumas cores que vamos usar no jogo. Cada cor é feita de 3 números (vermelho, verde, azul), chamados RGB.
# Quanto maior o número (de 0 a 255), mais daquela cor aparece.
AZUL = (0, 122, 255)  # Um azul bonito, como o céu.
VERMELHO = (255, 122, 122)  # Um vermelho claro, como um tomate.
AMARELO = (255, 204, 0)  # Um amarelo brilhante, como o sol.
BRANCO = (255, 255, 255)  # Branco puro, como papel.
PRETO = (0, 0, 0)  # Preto total, como a noite.

# Aqui decidimos o tamanho da janela do jogo em pixels (pontinhos na tela).
# A largura é 500 pixels e a altura também é 500 pixels, formando um quadrado.
LARGURA, ALTURA = 500, 500

# Essa linha cria a janela do jogo com o tamanho que escolhemos. Tudo que aparece no jogo vai dentro dessa janela.
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Aqui colocamos o nome "Jogo de Tradução" na barra de título da janela, para o jogador saber o que está jogando.
pygame.display.set_caption("Jogo de Tradução")

# Definimos uma fonte (tipo de letra) para textos grandes, como perguntas. O número 50 é o tamanho da letra.
fonte_principal = pygame.font.Font(None, 50)

# Outra fonte, agora para textos menores, como a pontuação ou instruções. O número 30 é o tamanho.
fonte_secundaria = pygame.font.Font(None, 30)

# Aqui decidimos o nome do arquivo onde vamos guardar a pontuação do jogador, para não perder entre os jogos.
ARQUIVO_PONTUACAO = "pontuacao.txt"

# O jogo dá 10 segundos para cada pergunta. Esse é o tempo inicial.
TEMPO_INICIAL = 10

# A pontuação começa em zero, porque o jogador ainda não acertou nada.
PONTUACAO = 0

# O tempo restante para responder começa igual ao tempo inicial (10 segundos).
tempo_restante = TEMPO_INICIAL

# Essa variável guarda a resposta certa da pergunta atual, mas começa vazia (None significa "nada").
resposta_correta = None

# Essa variável diz se o jogo está acontecendo agora. Começa como False (falso), porque ainda não começamos.
jogando = False

# Aqui guardamos a categoria de palavras que o jogador escolheu, como "Animais". Começa vazia.
categoria_selecionada = None

# Uma lista vazia para lembrar quais palavras já apareceram no jogo, para não repetir.
palavras_usadas = []

# Esse é um dicionário (como uma lista de pares) com palavras em português e suas traduções em inglês.
# Está dividido em categorias, como "Animais" ou "Objetos".
categoria_palavras = {
    "Animais": {  # Categoria de animais.
        "Cachorro": "Dog",  # Palavra em português e sua tradução.
        "Gato": "Cat",
        "Cavalo": "Horse",
        "Vaca": "Cow",
        "Leão": "Lion",
        "Elefante": "Elephant",
        "Macaco": "Monkey",
        "Urso": "Bear",
        "Coelho": "Rabbit",
        "Lobo": "Wolf",
        "Raposa": "Fox",
        "Jacaré": "Alligator",
        "Cobra": "Snake",
        "Papagaio": "Parrot",
        "Tubarão": "Shark"
    },
    "Objetos": {  # Categoria de coisas que usamos.
        "Mesa": "Table",
        "Cadeira": "Chair",
        "Lâmpada": "Lamp",
        "Relógio": "Clock",
        "Telefone": "Phone",
        "Computador": "Computer",
        "Teclado": "Keyboard",
        "Mouse": "Mouse",
        "Janela": "Window",
        "Porta": "Door",
        "Caderno": "Notebook",
        "Caneta": "Pen",
        "Lápis": "Pencil",
        "Espelho": "Mirror",
        "Garrafa": "Bottle"
    },
    "Natureza": {  # Categoria de coisas da natureza.
        "Árvore": "Tree",
        "Flor": "Flower",
        "Folha": "Leaf",
        "Rio": "River",
        "Mar": "Sea",
        "Lago": "Lake",
        "Montanha": "Mountain",
        "Cachoeira": "Waterfall",
        "Pedra": "Rock",
        "Areia": "Sand",
        "Sol": "Sun",
        "Lua": "Moon",
        "Estrela": "Star",
        "Nuvem": "Cloud",
        "Vento": "Wind"
    },
    "Números": {  # Categoria de números por escrito.
        "Um": "One",
        "Dois": "Two",
        "Três": "Three",
        "Quatro": "Four",
        "Cinco": "Five",
        "Seis": "Six",
        "Sete": "Seven",
        "Oito": "Eight",
        "Nove": "Nine",
        "Dez": "Ten",
        "Onze": "Eleven",
        "Doze": "Twelve",
        "Treze": "Thirteen",
        "Quatorze": "Fourteen",
        "Quinze": "Fifteen"
    }
}

# Aqui criamos uma função (um pedaço de código que podemos usar várias vezes) para carregar a pontuação salva.
def carregar_pontuacao():
    global PONTUACAO  # Diz que vamos mudar a variável PONTUACAO que está fora da função.
    # Verifica se o arquivo de pontuação existe no computador.
    if os.path.exists(ARQUIVO_PONTUACAO):
        # Abre o arquivo para ler o que está dentro.
        with open(ARQUIVO_PONTUACAO, "r") as arquivo:
            try:  # Tenta fazer algo, mas está preparado para erros.
                # Lê o número do arquivo e transforma em um número inteiro para usar como pontuação.
                PONTUACAO = int(arquivo.read())
            except ValueError:  # Se der erro (como texto no lugar de número), a pontuação fica zero.
                PONTUACAO = 0

# Outra função para salvar a pontuação no arquivo.
def salvar_pontuacao():
    # Abre o arquivo para escrever (substitui o que já estava lá).
    with open(ARQUIVO_PONTUACAO, "w") as arquivo:
        # Escreve a pontuação como texto no arquivo.
        arquivo.write(str(PONTUACAO))

# Executa a função de carregar a pontuação assim que o jogo começa.
carregar_pontuacao()

# Função para criar uma nova pergunta para o jogador.
def nova_pergunta():
    global resposta_correta, palavras_usadas  # Usa essas variáveis que estão fora da função.
    # Pega as palavras da categoria que o jogador escolheu.
    palavras_traducao = categoria_palavras[categoria_selecionada]
    # Se já usamos todas as palavras, limpa a lista para começar de novo.
    if len(palavras_usadas) >= len(palavras_traducao):
        palavras_usadas.clear()
    # Escolhe uma palavra em português de forma aleatória.
    palavra_portugues = random.choice(list(palavras_traducao.keys()))
    # Se a palavra já foi usada, escolhe outra até achar uma nova.
    while palavra_portugues in palavras_usadas:
        palavra_portugues = random.choice(list(palavras_traducao.keys()))
    # Coloca a palavra na lista de usadas.
    palavras_usadas.append(palavra_portugues)
    # Pega a tradução correta dessa palavra.
    resposta_correta = palavras_traducao[palavra_portugues]
    # Cria uma lista com a resposta certa para mostrar ao jogador.
    opcoes = [resposta_correta]
    # Adiciona 3 respostas erradas à lista, para ter 4 opções no total.
    while len(opcoes) < 4:
        opcao_errada = random.choice(list(palavras_traducao.values()))
        # Só adiciona se a opção errada não estiver já na lista.
        if opcao_errada not in opcoes:
            opcoes.append(opcao_errada)
    # Embaralha as opções para a resposta certa não ficar sempre no mesmo lugar.
    random.shuffle(opcoes)
    # Dá ao jogo a palavra em português e as 4 opções.
    return palavra_portugues, opcoes

# Função para mostrar texto na tela em um lugar específico.
def exibir_texto(texto, fonte, cor, x, y):
    # Transforma o texto em uma imagem que o jogo pode mostrar, usando a fonte e cor escolhidas.
    superficie = fonte.render(texto, True, cor)
    # Descobre o tamanho da imagem do texto e centraliza ela nas posições x e y.
    retangulo = superficie.get_rect(center=(x, y))
    # Coloca a imagem do texto na tela.
    tela.blit(superficie, retangulo)

# Função para o menu onde o jogador escolhe a categoria.
def menu_categorias():
    global categoria_selecionada  # Usa a variável de fora para guardar a escolha.
    # Pinta a tela inteira de branco.
    tela.fill(BRANCO)
    # Mostra a instrução "Selecione uma categoria" no topo da tela.
    exibir_texto("Selecione uma categoria", fonte_principal, PRETO, LARGURA // 2, ALTURA // 4)
    # Pega a lista de categorias (Animais, Objetos, etc.).
    categorias = list(categoria_palavras.keys())
    # Mostra cada categoria na tela, uma embaixo da outra.
    for i, categoria in enumerate(categorias):
        y = ALTURA // 2 + i * 50  # Calcula a posição de cada categoria.
        exibir_texto(categoria.capitalize(), fonte_secundaria, AZUL, LARGURA // 2, y)
    # Atualiza a tela para o jogador ver tudo que desenhamos.
    pygame.display.flip()
    # Espera o jogador clicar em uma categoria.
    aguardando = True
    while aguardando:
        # Olha tudo que o jogador faz (como clicar ou fechar a janela).
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Se fechar a janela, o jogo acaba.
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:  # Se clicar com o mouse...
                x, y = pygame.mouse.get_pos()  # Pega onde o jogador clicou.
                # Vê se o clique foi em cima de uma categoria.
                for i, categoria in enumerate(categorias):
                    texto_y = ALTURA // 2 + i * 50
                    if texto_y - 20 < y < texto_y + 20:  # Se o clique está perto do texto...
                        categoria_selecionada = categoria  # Salva a categoria escolhida.
                        aguardando = False  # Para de esperar.

# Função para o menu inicial do jogo.
def menu_inicial():
    # Pinta a tela de branco.
    tela.fill(BRANCO)
    # Mostra o título "Jogo de Tradução" no topo.
    exibir_texto("Jogo de Tradução", fonte_principal, PRETO, LARGURA // 2, ALTURA // 4)
    # Mostra quantos pontos o jogador já tem.
    exibir_texto(f"Pontuação Acumulada: {PONTUACAO}", fonte_secundaria, PRETO, LARGURA // 2, ALTURA // 2)
    # Diz para o jogador clicar para começar.
    exibir_texto("Clique para Jogar", fonte_secundaria, AZUL, LARGURA // 2, ALTURA // 1.5)
    # Atualiza a tela.
    pygame.display.flip()
    # Espera o jogador clicar.
    aguardando = True
    while aguardando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fecha o jogo se a janela for fechada.
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONUP:  # Começa quando o jogador clica.
                aguardando = False

# Função principal que roda o jogo.
def jogo():
    global tempo_restante, PONTUACAO, resposta_correta, jogando  # Usa essas variáveis de fora.
    # Cria uma nova pergunta com uma palavra e 4 opções.
    palavra_portugues, opcoes = nova_pergunta()
    # Guarda o tempo atual para contar os segundos.
    ultima_vez = time.time()
    jogando = True  # O jogo começa!
    tempo_restante = TEMPO_INICIAL  # Dá 10 segundos para responder.
    while jogando:  # Enquanto o jogo está rolando...
        # Pinta a tela de branco para apagar o que estava antes.
        tela.fill(BRANCO)
        # Calcula quanto tempo passou desde a última vez que olhamos.
        agora = time.time()
        tempo_passado = agora - ultima_vez
        tempo_restante -= tempo_passado  # Tira o tempo que passou do tempo restante.
        ultima_vez = agora  # Atualiza o tempo.

        # Se o tempo acabar, mostra uma mensagem e para o jogo.
        if tempo_restante <= 0:
            exibir_texto("Tempo Esgotado", fonte_principal, VERMELHO, LARGURA // 2, ALTURA // 2)
            pygame.display.flip()
            pygame.time.delay(2000)  # Espera 2 segundos para o jogador ver.
            jogando = False
            salvar_pontuacao()  # Salva a pontuação.
            continue

        # Mostra o tempo que falta no canto da tela.
        exibir_texto(f"{int(tempo_restante)}s", fonte_secundaria, PRETO, 50, 30)
        # Mostra a pontuação atual no outro canto.
        exibir_texto(f"Pontuação: {PONTUACAO}", fonte_secundaria, PRETO, LARGURA - 80, 30)
        # Mostra a palavra que o jogador precisa traduzir.
        exibir_texto(f"Traduza: {palavra_portugues}", fonte_principal, PRETO, LARGURA // 2, 100)

        # Define cores para as 4 opções de resposta.
        cores = [AZUL, VERMELHO, AMARELO, BRANCO]
        # Desenha 4 retângulos coloridos, cada um com uma opção de resposta.
        for i in range(4):
            x = (i % 2) * (LARGURA // 2)  # Calcula a posição horizontal.
            y = 200 + (i // 2) * 100  # Calcula a posição vertical.
            pygame.draw.rect(tela, cores[i], (x, y, LARGURA // 2, 100))  # Desenha o retângulo.
            exibir_texto(opcoes[i], fonte_principal, PRETO, x + (LARGURA // 4), y + 50)  # Coloca o texto dentro.

        # Olha o que o jogador faz.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fecha o jogo se a janela for fechada.
                salvar_pontuacao()
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONUP:  # Se o jogador clicar...
                x, y = pygame.mouse.get_pos()  # Pega onde clicou.
                for i in range(4):  # Vê qual retângulo foi clicado.
                    rect_x = (i % 2) * (LARGURA // 2)
                    rect_y = 200 + (i // 2) * 100
                    if rect_x <= x < rect_x + LARGURA // 2 and rect_y <= y < rect_y + 100:
                        resposta_selecionada = opcoes[i]  # Pega a resposta que o jogador escolheu.
                        if resposta_selecionada == resposta_correta:  # Se for a certa...
                            PONTUACAO += 1  # Aumenta a pontuação.
                            exibir_texto("Correta", fonte_principal, AZUL, LARGURA // 2, ALTURA - 50)
                            pygame.display.flip()
                            pygame.time.delay(1000)  # Mostra "Correta" por 1 segundo.
                            palavra_portugues, opcoes = nova_pergunta()  # Dá uma nova pergunta.
                            tempo_restante = TEMPO_INICIAL  # Reseta o tempo.
                        else:  # Se for errada...
                            exibir_texto("Errada", fonte_principal, VERMELHO, LARGURA // 2, ALTURA - 50)
                            pygame.display.flip()
                            pygame.time.delay(2000)  # Mostra "Errada" por 2 segundos.
                            jogando = False  # Para o jogo.
                            salvar_pontuacao()  # Salva a pontuação.

        # Atualiza a tela para mostrar tudo que desenhamos.
        pygame.display.flip()

# Esse é o coração do jogo: um loop (repetição) que mantém o jogo rodando.
while True:
    menu_inicial()  # Mostra o menu inicial.
    menu_categorias()  # Deixa o jogador escolher a categoria.
    jogo()  # Roda o jogo.