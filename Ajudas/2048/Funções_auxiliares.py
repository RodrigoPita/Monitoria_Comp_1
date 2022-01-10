# Trabalho final - 2048
# Arquivo de funçoes auxiliares
# Gabriel Pacheco do Nasciento
# 116091468

#Parte 1
#Item (1)
def numeros_adj(lista):
    """ Função recebe uma lista númerica e soma os números adjacentes que
    são iguais, a soma é feita da esquerda para direita. list -> bool"""
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1] and lista[i] != 0:
            lista[i+1] = lista[i] + lista[i+1]
            lista[i] = 0
            return True

#Item (2)
def move(lista, direcao):
    """ Função que designa a direção da soma, guiando para esquerda ou direita
    list, str -> bool."""
    copy = lista.copy()
    if direcao == 'esq':
        for i in range(0, len(lista)-1):
            if lista[i] == lista[i+1] and lista[i] != 0 and lista[i] == copy[i]:
                lista[i+1] = lista[i]+lista[i+1]
                lista[i] = 0
    elif direcao == 'dir':
        for i in range(len(lista)-1, 0, -1):
            if lista[i] == lista[i-1] and lista[i] != 0 and lista[i] == copy[i]:
                lista[i-1] = lista[i]+lista[i-1]
                lista[i] = 0
    return lista

#Item (3)
def organiza(lista):
    """Função conta os zeros e põe a esquerda da lista, os outros valores
    ficam a direita. list -> list"""
    total_zeros = lista.count(0)
    for i in range(total_zeros):
        lista.remove(0)
        for i in range(total_zeros):
            lista.insert(0,0)
            return lista
#Item (4)
def organiza(lista, direcao):
    """Função conta os zeros e põe a esquerda da lista, os outros valores
    ficam a direita. list -> list"""
    if direcao == 'dir':
        total_zeros = lista.count(0)
        for i in range(total_zeros):
            lista.remove(0)
        for i in range(total_zeros):
            lista.insert(0,0)
    elif direcao == 'esq':
        total_zeros = lista.count(0)
        for i in range(total_zeros):
            lista.remove(0)
        for i in range(total_zeros):
            lista.append(0)
    return lista
#Parte 2
#Item (5)
def eh_igual(matriz_1, matriz_2):
    """Função verifica se as matrizes são iguais, retornado True caso sejam iguais
    e False caso não sejam iguais, os valores de entrada são as matrizes e de saída o booleano
    list, list -> bool"""
    if len(matriz_1) != len(matriz_2):
        return False
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[i])):
            if matriz_1[i][j] != matriz_2[i][j]:
                return False
    return True

#Item (6)
from random import randint
def cria_tabuleiro(n: int=4):
    """Função cria um tabuleiro de zeros n por n, com exeção de duas posições aleatorias que contem
    o número 2; int -> list"""
    matriz_retorno = []
    aux1, aux2 = 0, 0
    for i in range(n):
        matriz_retorno += [[0]]
        for j in range(1, n):
            matriz_retorno[i] += [0]
    for k in range(2):
        i, j = randint(0, n-1), randint(0, n-1)
        if i == aux1 and j == aux2:
            i, j = randint(0, n-1), randint(0, n-1)
        aux1, aux2 = i, j
        matriz_retorno[i][j] = 2
    return matriz_retorno

#Item (7)
def substitui(M):
    """Função que cria uma matriz e substitui de forma aleatoria os números zeros por
    depois ou quatro. Se  a inserção não puder ser feitaretorna False, caso contrario True
    list -> bool."""
    n = len(M)
    contador = 0
    lista = [2, 2, 2, 4]
    for i in M:
        for j in i:
            if j == 0:
                contador += 1
                if contador == 2:
                    break
    if contador < 2:
        return False
    else:
        contador = 0
    while contador < 2:
        i, j, pos = randint(0, n-1), randint(0, n-1), randint(0, len(lista)-1)
        if M[i][j] == 0:
            M[i][j] = lista[pos]
            contador += 1
    return True

#Item (8)
def transposta(M_t):
    """Função retorna a transposta da matriz list -> list"""
    T = []
    parada = len(M_t)
    for i in range(parada):
        T += [[M_t[0][i]]]
        for j in range(1, parada):
            T[i] += [M_t[j][i]]
    return T

#Parte 3
#Item (9)
def visualiza(M): 
    """Função para ver melhor a disposição do tabuleiro. list -> list"""
    for i in range(len(M)): 
        for j in range(len(M)): 
            if M[i][j] == 0: 
                print('-', end = '  ') 
            else: 
                print(M[i][j], end = '  ') 
        print() 
    return

#Item (10)
from math import log2, ceil, floor 
def pega_n():
    """Funç̃ao que pega um numero do usúario, confere se é uma potencia de 2, e entao retorne o ńumero inteiro. float -> int"""
    n = input('Insira uma potência de 2: ') 
    if ceil.log2(n) == floor.log2(n): 
        return n 

#Item (11)
def pega_jogada():
    """Funcao que ira pegar alguma jogada v́alida do usúario. No 2048, as
    jogadas v ́alidas serao a, s, d, w. str -> str"""
    jogada = input('Insira uma jogada válida ("a", "s", "d", "w"): ') 
    while jogada not in 'asdw': 
        jogada = input('Insira uma jogada válida "a", "s", "d", "w"): ') 
    return jogada

#Item (12)
def move_tabuleiro(tabuleiro, direcao): 
    parada = len(tabuleiro) 
    if direcao == 'a': 
        for i in range(parada): 
            tabuleiro[i] = organiza(tabuleiro[i], 'esq') 
            tabuleiro[i] = move(tabuleiro[i], 'esq')
            tabuleiro[i] = organiza(tabuleiro[i], 'esq')
    elif direcao == 'd': 
        for i in range(parada): 
            tabuleiro[i] = organiza(tabuleiro[i], 'dir') 
            tabuleiro[i] = move(tabuleiro[i], 'dir')
            tabuleiro[i] = organiza(tabuleiro[i], 'dir')
    elif direcao == 'w': 
        aux = transposta(tabuleiro) 
        for i in range(parada): 
            aux[i] = organiza(aux[i], 'esq') 
            aux[i] = move(aux[i], 'esq')
            aux[i] = organiza(aux[i], 'esq') 
        tabuleiro = transposta(aux) 
    elif direcao == 's': 
        aux = transposta(tabuleiro) 
        for i in range(parada): 
            aux[i] = organiza(aux[i], 'dir') 
            aux[i] = move(aux[i], 'dir')
            aux[i] = organiza(aux[i], 'dir')
        tabuleiro = transposta(aux) 
    return tabuleiro

#Item (13)
def status(tabuleiro, n_max): 
    ''' 
    1 - Ganhou! 
    2 - Ainda tem 0s no tabuleiro 
    3 - Ainda tem jogadas possíveis 
    4 - Perdeu! 
    ''' 
    parada = len(tabuleiro) 
    t_tabuleiro = transposta(tabuleiro) 
    if n_max in tabuleiro[0] or n_max in tabuleiro[1] or n_max in tabuleiro[2] or n_max in tabuleiro[3]: 
        return 1 
    elif 0 in tabuleiro[0] or 0 in tabuleiro[1] or 0 in tabuleiro[2] or 0 in tabuleiro[3]: 
        return 2 
    for i in range(parada): 
        for j in range(1,parada): 
            if tabuleiro[j] == tabuleiro[j-1] or t_tabuleiro[j] == t_tabuleiro[j-1]: 
                return 3 
    return 4

#Item (14)
def menu(): 
    """Função explica como funciona o jogo. str -> str""" 
    print("2048 é um jogo de tabuleiro e raciocínio.\n") 
    print("Com peças numéricas que deslizam suavemente quando o jogador as move em um dos quatro sentidos disponíveis.\n") 
    print("Esses sentidos são: para cima, para baixo, à esquerda e à direita.\n") 
    print("As peças validas aqui são os botões a, w, s, d.\n") 
    print("Quando dois blocos de números iguais se chocam, eles viram um só com valor igual a soma dos dois") 
    print("A cada movimento é acrescentado um bloco com valor 2 ou com valor 4.\n") 
    print("Você vence quando conseguir um bloco no valor de 2048.")
