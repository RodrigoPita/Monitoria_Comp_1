# Questão 1

from random import randint

def freq_serie(n):
    '''
    int --> int'''

    lista_resultados = []
    contador = 0
    n_atual = 0
    for i in range(n):
        lista_resultados.append(randint(1, 6))
        if i == 0:
            continue
        if n_atual != lista_resultados[i]:
            n_atual = lista_resultados[i-1]
            if lista_resultados[i] == lista_resultados[i-1]:
                contador += 1
    return contador

def sequenciasRepetidas():
    '''Retorna quantas sequências de repetições existem na sequência que será inserida
none -> int'''
    sequencia=input('Insira sua sequência, separando os elementos apenas por espaço: ')
    listaNumeros=[]
    for i in range(len(str.split(sequencia,' '))):
        numero=int(str.split(sequencia,' ')[i])
        list.append(listaNumeros,numero)
    novaLista=[]
    j=1
    while j<len(listaNumeros):
        lista1=[]
        if listaNumeros[j]==listaNumeros[j-1]:
            while listaNumeros[j]==listaNumeros[j-1]:
                list.append(lista1,listaNumeros[j])
                j=j+1
            list.append(lista1,listaNumeros[j-1])
            list.append(novaLista,lista1)
        j=j+1
    print(len(novaLista))

#sequenciasRepetidas()


# Questão 2
def i1(a, b, c):
    return ((a + b)*c)/2
def i2(a, b, c):
    return a*a, b*b, c*c
def i3(a, b, c):
    return (a + b + c)/3
def i4(a, b, c):
    return sum(range(a, b+1, c))

def func():
    '''
    None --> None'''
    i = int(input('Digite o código i de 1 a 4: '))
    while 1 > i or i > 4:
        i = int(input('Digite o código i de 1 a 4: '))
        
    a = int(input('Insira um valor inteiro a: '))
    b = int(input('Insira um valor inteiro b maior o anterior: '))
    c = int(input('Insira um valor inteiro c: '))

    resultado = 0
    if i == 1:
        resultado = i1(a, b, c)
    elif i == 2:
        resultado = i2(a, b, c)
    elif i == 3:
        resultado = i3(a, b, c)
    else:
        resultado = i4(a, b, c)

    print(
        f'Considerando os valores {a}, {b}, {c}',
        f'O resultado foi {resultado}',
        sep = '\n'
        )

# Questão 3

def buscaSetor(setor, P):
    '''Busca as informações dos funcionários de um determinado setor de uma empresa
    str, list --> list'''
    lista_retorno = []
    for i in P:
        if i[2] == setor:
            lista_retorno.append(i[0:2] + i[3:])
    return lista_retorno

def main():
    n = int(input('Digite o número de funcionários da sua empresa: '))
    P = []
    for i in range(n):
        linhaI = input('Digite o nome, registro, setor e telefone do funcionário separado de um espaço: ')
        P.append(linhaI.split())
    setor = input('Insira um setor: ')
    matriz = buscaSetor(setor, P)
    for i in matriz:
        print(i)
