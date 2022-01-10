# Questão 1 - MT
def eh_quadrada(matriz):
    '''Verifica se a matriz dada é quadrada, ou seja,
    se tem o mesmo número de linhas e colunas
    list --> bool'''
    for i in matriz:
        if len(matriz) != len(i):
            return False
    return True

# Questão 2 - MT
def conta_numero(matriz, n):
    '''Conta a frequência de um número n numa matriz
    list, int --> int'''
    contador = 0
    for i in matriz:
        contador += i.count(n)
    return contador

# Questão 3 - MT
def media_matriz(matriz):
    '''Calcula a média aritmética entre todos os elementos de uma matriz
    list --> float'''
    soma = 0
    total = 0
    for i in matriz:
        for j in i:
            soma += j
        total += len(i)
    return round(soma/total, 2)

# Questão 4 - MT
def melhor_volta(matriz):
    '''A partir de uma matriz 6x10 com números, retorna o menor número,
    a linha e a coluna em que ele está
    list --> tuple'''
    melhor_volta = 0
    tempo = 100000
    corredor = 0
    indice = 1
##    for i in range(len(matriz)):
##        for j in range(len(matriz[i])):
##            elemento = matriz[i][j]
##            if tempo > elemento:
##                tempo = elemento
##                melhor_volta = matriz[i].index(elemento)+1
##                corredor = i+1
    for i in matriz:
        if min(i) < tempo:
            tempo = min(i)
            corredor = indice
            melhor_volta = i.index(tempo) + 1
        indice += 1
    return(corredor, tempo, melhor_volta)

# Questão 5 - MT
def buscaSetor(setor, P):
    '''Busca as informações dos funcionários de um determinado setor de uma empresa
    str, list --> list'''
    lista_retorno = []
    for i in P:
        if i[2] == setor:
            lista_retorno.append(i[0:2] + i[3:])
    return lista_retorno

# Questão 6 - MT
def ordena_por_insercao(lista):
    '''Ordena uma lista pelo algoritmo Insertion sort
    list --> list'''
    for i in range(1, len(lista)):
        if lista[i] < lista[i-1]:
            for j in range(i, 0, -1):
                if lista[j] < lista[j-1]:
                    aux = lista[j-1]
                    lista[j-1] = lista[j]
                    lista[j] = aux
    return lista

# Questão 1 - IDLE
def multiplica_matriz(matriz, n):
    '''Fas o produto de uma matriz por um escalar n
    list, int --> list'''
    matriz_retorno = []
    for i in range(len(matriz)):
        matriz_retorno += [matriz[i][:]]
        for j in range(len(matriz[i])):
            matriz_retorno[i][j] *= n
    return matriz_retorno

# Questão 2 - IDLE
def quem_ligou(lista_contatos, numero):
    '''Dado um número de telefone e a lista de contatos,
    encontra os dados de quem o número pertence
    list, str --> list'''
    lista_retorno = []
    for i in lista_contatos:
        if numero in i[1]:
            lista_retorno += i
    return lista_retorno
