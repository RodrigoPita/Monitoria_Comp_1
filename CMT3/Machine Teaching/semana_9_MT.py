#-------------------------------------------------------------------------------------------------------------------------#
## ===================================================================
## S E M A N A  9  -  L A Ç O S  A N I N H A D O S  E  M A T R I Z E S
## ===================================================================

## ==========================
## Questão 1: Matriz quadrada
## ==========================

## Faça uma função booleana chamada **eh_quadrada** para identificar se uma matriz é quadrada.
## Observação: uma matriz vazia (sem nenhuma linha nem coluna) é considerada quadrada.

def eh_quadrada(matriz:list[list])->bool:
    '''Função que verifica se uma matriz é quadrada (mesmo número de linhas e colunas)'''
    for i in matriz:
        if len(matriz) != len(i):
            return False
	return True

## ============================
## Questão 2: Buscando a matriz
## ============================

## Faça uma função definida por **conta_numero(numero, matriz)** que dado um número inteiro e uma matriz de inteiros de tamanho qualquer,
## conta e retorna quantas vezes aquele número aparece na matriz.

def conta_numero(numero:int, matriz:list[list])->int:
    '''Função que calcula a frequência de um número numa matriz'''
    contador = 0
    for i in matriz:
        for j in i:
            if j == numero:
                contador += 1
	return contador

## ==========================
## Questão 3: Média da matriz
## ==========================

## Faça uma função chamada **media_matriz** que dada uma matriz de inteiros não vazia,
## retorna a média de todos os números da matriz (com exatamente duas casas decimais de precisão).

def media_matriz(matriz:list[list])->float:
    '''Função que calcula a média aritmética entre todos os elementos de uma matriz'''
    soma = 0
    total = 0
    for i in matriz:
        soma += sum(i)
        total += len(i)
    return round(soma/total, 2)

## =======================
## Questão 4: Melhor volta
## =======================

## Uma pista de Kart permite 10 voltas para cada um dos 6 corredores.
## Faça uma função chamada **melhor_volta** que receba como entrada uma matriz 6 x 10 com os tempos em segundos dos corredores em cada volta.
## A função deve retornar uma **tupla** informando: De quem foi a melhor volta da prova, com qual tempo e em que volta.
## Assuma que os corredores tem tempos diferentes. (dica: use a função \`min\`).
##
## Obs: use números de 1 a 6 para os corredores e de 1 a 10 para as voltas (não esqueça que em Python os índices começam de 0)

def melhor_volta(matriz:list[list])->tuple:
    '''Função que a partir de uma matriz 6 x 10 com os tempos em segundos dos corredores em cada volta,
    retorna o corredor mais rápido, seu tempo e em qual volta atingiu esse tempo'''
    tempo, corredor, volta, indice = 1000, 0, 0, 1
    for i in matriz:
        if min(i) < tempo:
            corredor = indice
            tempo = min(i)
            volta = i.index(tempo)+1
        indice += 1
	return (corredor, tempo, volta)

## ================================
## Questão 5: Busca de funcionários
## ================================

## Suponha que os dados de funcionários de uma empresa sejam armazenados em uma matriz como a do exemplo a seguir:
##
## ( "AdalbertoFerreira"  "566"  "Contabilidade"  "(21)84564-5248" )
## ( "JulianaVasconcelos" "465"       "RH"         "(21)3555-4552" )
## (    "FlaviaAmorim"    "565"  "Contabilidade"   "(21)2134-4845" )
##
## Cada linha da matriz tem quatro entradas, representando as informações referentes a nome, registro,
## setor e telefone de um funcionário, nesta ordem. O número de linhas depende da quantidade de funcionários.
## Todas as entradas da matriz estão em formato string.
##
## Escreva uma função chamada **busca** que receba uma matriz como a do exemplo e faça uma busca por setor, ou seja,
## dado um nome de um setor da empresa, a função retorna os dados de todos os funcionários daquele setor. Por exemplo:
##
## >>> busca("Contabilidade", matriz)
##
## >>> [[‘Adalberto Ferreira’, ‘566’, ‘(21)84564-5248’],[‘Flavia Amorim’, ‘465’, ‘(21)2134-4845']]
##
## Se nenhum registro for encontrado, a função deverá retornar uma lista vazia.

def busca(setor:str, matriz:list[list])->list[list]:
    '''Função que busca na matriz dada as informações de um funcionário de uma empresa, de acordo com o setor dado'''
    resultado = []
    for i in matriz:
        if i[2] == setor:
            resultado.append(i[0:2] + i[3:])
	return resultado

#-------------------------------------------------------------------------------------------------------------------------#
