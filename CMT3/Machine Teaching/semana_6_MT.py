#-------------------------------------------------------------------------------------------------------------------------#
## ==================================================================================
## S E M A N A  6  -  F A T I A M E N T O  E  M A N I P U L A Ç Ã O  D E  L I S T A S
## ==================================================================================

## =======================
## Questão 1: Altera frase
## =======================

## Faça uma função chamada **altera_frase** que receba uma frase, uma palavra e uma posição.
## - Caso a palavra já exista na frase, transforme a primeira ocorrência da palavra na frase para maiúscula.
## - Caso a palavra não exista, insira a palavra na frase na posição dada. Assuma que a primeira palavra está na posição 0.
## Retorne a nova frase.
##
## Exemplo1:
## - Frase: "Meu nome é ana"
## - Palavra: "ana"
## - Retorno": Meu nome é ANA"
##
## Exemplo 2:
## - Frase: "Meu nome é ana"
## - Palavra: "primeiro"
## - Posição: 1
## - Retorno: "Meu primeiro nome é ana"

def altera_frase(frase:str, palavra:str, posicao:int)->str:
    '''Função que dadas duas strings (frase, palavra) e um número (posicao),
    retorna a mesma frase com a palavra toda maiúscula se ela já estava na frase, caso contrário,
    insere a palavra na frase e retorna a frase nova'''
    frase = frase.split()
    if palavra in frase:
        aux = frase.index(palavra)
        frase[aux] = frase[aux].upper()
    else:
        frase[posicao:posicao] = [palavra]
    return ' '.join(frase)

## ===============================
## Questão 2: Faltas no campeonato
## ===============================

## Faça uma função chamada **faltas** que receba uma lista no seguinte formato:
## [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]
##
## Esta lista indica o número de faltas que cada time fez em cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9.
## Dada essa lista, a função deve retornar o total de faltas do campeonato.

def faltas(lista:list)->int:
    '''Função que dada uma lista (lista) com o número de faltas de cada time relativo a cada jogo, retorna o somatório de todas as faltas'''
    return sum(lista[0][2]) + sum(lista[1][2]) + sum(lista[2][2])

## ==========================
## Questão 3: Insere ordenado
## ==========================

## Faça uma função definida por **insere(lista_numero, n)** que dada uma lista ordenada (crescente) de números inteiros
## e um número inteiro n, inclua n na posição correta, ou seja, de tal maneira que a lista continue ordenada.
##
## **DICA**: Provavelmente, a primeira idéia que vem à cabeça é inserir diretamente na posição correta,
## verificando os elementos da lista até achar a posição onde o n deve ser inserido. Mas nós ainda não sabemos fazer isso (veremos nas próximas aulas).
## Pense em outra estratégia de resolução deste problema, usando a função **list.sort(lista)**.

def insere(lista_numero:list, n:int)->list:
    '''Função que dada uma lista (lista_numero) e um número (n), insere n na lista e devolve a mesma ordenada'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero

## ==================
## Questão 4: Maiores
## ==================

## Faça uma função chamada **maiores** que dada uma lista de números inteiros e um número inteiro n, retorna outra lista,
## que contenha todos os números da lista original maiores que n, ordenados em ordem crescente.

def maiores(lista:list, n:int)->list:
    '''Função que dada uma lista (lista) e um número (n), retorna uma nova lista com apenas os números maiores que n'''
    if n not in lista:
    	lista.append(n)
    lista.sort()
    aux = lista.index(n)
    return lista[aux+1:]

## =========================
## Questão 5: Acima da média
## =========================

## Faça uma função chamada **acima_da_media** que dada uma lista com as notas dos alunos de uma turma,
## retorne uma lista ordenada com as notas que ficaram acima da média.
##
## **DICA 1**: Python provê uma função sum(lista).
##
## **DICA 2:** Aproveite a função desenvolvida no exercício **maiores**. Para reaproveitar uma função feita no Machine Teaching,
## copie o código completo da função e cole na caixa de resposta do exercício onde quer utilizá-la.
## Faça então a função pedida no exercício, embaixo da que você colou, e dentro dela você irá chamar a que está reutilizando.

def maioresX(lista:list, n:int)->list:
    if n not in lista:
    	lista.append(n)
    lista.sort()
    aux = lista.index(n)
    return lista[aux+1:]

from math import ceil
def acima_da_media(lista:list)->list:
    '''Função que dada uma lista (lista), calcula a média aritmética entre seus termos
    e retorna uma nova lista com apenas os termos maiores que a média'''
    n = sum(lista)/len(lista)
    return maioresX(lista, n)

## ====================
## Questão 6: Ordenada?
## ====================

## Defina uma função chamada **eh_ordenada** que dada uma lista não vazia contendo uma quantidade qualquer de valores numéricos,
## diga se a lista está ordenada em ordem crescente, decrescente ou não ordenada.
## A retorno da função deve ser uma tupla cujo primeiro elemento é **True**, caso a lista esteja ordenada, e **False**,
## caso contrário e cujo segundo elemento seja "crescente", "decrescente" ou "desordenada", indicando se a lista está ordenada em ordem crescente,
## decrescente ou não está ordenada, respectivamente.
##
## **DICA**: Atenção! Lembre-se que algumas operações sobre listas alteram o valor da lista original ao invés de retornar uma nova lista com as alterações.
## Esse é o caso da função list.sort(lista), por exemplo. Então, se você precisar preservar o valor da lista original, faça uma cópia antes de alterá-la.

def eh_ordenada(lista:list)->tuple:
    '''Função que dada uma lista (lista) não vazia com valores numéricos,
    retorne uma tupla, onde seu primeiro termo é um booleano para classificar a lista como ordenada (True) ou não (False)
    e o segundo termo uma string ('crescente', 'decrescente', 'desordenada')'''
    aux = [] + lista
    aux.sort()
    if lista == aux:
        return (True, "crescente")
    aux.sort(reverse = True)
    if lista == aux:
        return(True, "decrescente")
    return (False, "desordenada")

#-------------------------------------------------------------------------------------------------------------------------#
