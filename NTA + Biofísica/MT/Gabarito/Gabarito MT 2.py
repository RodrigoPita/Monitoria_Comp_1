#1
def num_bombons(dinheiro,valor_unid):
    '''Calcula a quantidade de bombons no valor 'valor_unid' que pode ser comprada com
    dinheiro.
    float,float -> int'''
    return dinheiro // valor_unid
#2
from math import ceil
def carros(pessoas,capacidade=5):
    '''Calcula a quantidade de carros de capacidade X para transportar
    um número Y de pessoas.
    int,int -> int'''
    #Encontramos o número de carros necessários fazendo 'pessoas/capacidade'
    #Depois pegamos o maior inteiro mais próximo
    return ceil(pessoas / capacidade)

#2.1 solução alternativa(sem importar bibliotecas)
def carros2(pessoas,capacidade=5):
    carros_int = pessoas // capacidade
    resto = pessoas % capacidade
    #Se o valor de resto for 0, então bool(resto) retornará False, que na adição
    #é interpretado como 0. Caso contrário, retornará True, que é interpretado como 1
    #na adição.
    return carros_int + bool(resto)

#2.2 outra solução só com aritmética e arredondamento
def carros3(pessoas,capacidade=5):
    carros_int = pessoas // capacidade
    #Aqui vamos verificar se nosso número de pessoas é múltiplo da capacidade dos carros
    carros_frac = (pessoas/capacidade) - carros_int
    #Caso carros_frac seja 0, então teremos round(0.5) que é zero.("pessoas" é múltiplo de "capacidade")
    #Para qualquer outro valor de carros_frac(note que é limitado a [0,1[),
    #round(carros_frac + 0.5) será igual a 1(pois 0.5 < x < 1.5),
    #identificando que precisamos de mais um carro.
    return carros_int + round(carros_frac + 0.5)

#3
def bolos(a,b,c):
    '''Calcula a quantidade de bolos máxima de bolos que pode ser feita
    usando quantidades a,b,c dos ingredientes.
    int,int,int -> int'''
    #Verificar quantos bolos podemos fazer com cada ingrediente separadamente
    trigo, ovo, leite = a // 2 , b // 3, c // 5
    #Retornamos a quantidade de bolos do ingrediente limitante 
    return min(trigo,ovo,leite)
    