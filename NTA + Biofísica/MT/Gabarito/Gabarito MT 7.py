# -------------
# Gabarito MT 7
# -------------

# Questão 1 - MT
def filtra_multiplos(lista_numeros, n):
    '''Filtra uma lista de numeros, retornando apenas os ques são múltiplos de n
    list, int --> list'''
    i = 0
    lista = []
    while i < len(lista_numeros):
        if lista_numeros[i] % n == 0:
            lista.append(lista_numeros[i])
        i += 1
    return lista

# Questão 2 - MT
def consoantes(frase):
    '''Altera uma frase dada para que todas as consoantes fiquem maiúsculas
    str --> str'''
    i = 0
    aux = ''
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyzç':
            aux += frase[i].upper()
        else:
            aux += frase[i]
        i += 1
    return aux
        
# Questão 3 - MT
def posLetra(frase, letra, n):
    '''Encontra a posição da n-ésima ocorrência da letra dada na frase dada
    str, str, int --> int'''
    i = 0
    contador = 0
    while i < len(frase):
        if letra == frase[i]:
            contador += 1
        if contador == n:
            return i
        i += 1
    # caso o while rode a lista toda sem retornar, o número de ocorrências é menor que n
    return -1

# Questão 4 - MT
def repetidos(lista):
    '''Verifica quantos termos de uma lista são iguais ao termo imediatamente anterior e retorna esse valor
    str --> int'''
    i = 1
    contador = 0
    while i < len(lista):
        if lista[i-1] == lista[i]:
            contador += 1
        i += 1
    return contador

# Questão 5 - MT
def fatorial(n):
    '''Calcula o fatorial de n
    int --> int'''
    i = n-1
    while i > 0:
        n *= i
        i -= 1
    return n

# Questão 6 - MT
def faltante(lista):
    '''Verifica qual o número faltante numa lista de 1 até N com N-1 termos
    str --> int'''
    i = 0
    lista.sort()
    while i < len(lista):
        if lista[i]-1 not in lista and lista[i]-1 != 0:
            return lista[i]-1
        i += 1
    # caso o while rode a lista toda sem retornar, o elemento faltante do intervalo [1, N] será N
    return lista[-1]+1
