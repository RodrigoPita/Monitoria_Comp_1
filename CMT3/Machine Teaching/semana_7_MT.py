#-------------------------------------------------------------------------------------------------------------------------#
## =============================================================================================================
## S E M A N A  7  -  E S T R U T U R A  D E  R E P E T I Ç Ã O  C O M  T E S T E  D E  P A R A D A :  W H I L E
## =============================================================================================================

## ===========================
## Questão 1: Filtra múltiplos
## ===========================

## Faça uma função chamada **filtraMultiplos** para filtrar os múltiplos de um número n. Sua função deve receber como entrada uma lista de números e um número,
## e retornar outra lista contendo todos os elementos da lista original que forem divisíveis por n.

def filtraMultiplos(lista:list, n:int)->list:
    '''Função que dada uma lista (lista) de números e um número (n), retorna uma nova lista contendo todos os termos da lista original que são divisíveis por n'''
    count = 0
    L = []
    while count < len(lista):
        if lista[count] % n == 0:
            L.append(lista[count])
        count += 1
    return L

## ===================================
## Questão 2: Consoantes em maiúsculas
## ===================================

## Faça uma função chamada **uppCons** que receba como entrada uma frase e retorne a frase com todas as suas consoantes em maiúsculas
## (e os demais caracteres exatamente como estavam na frase original).

def uppCons(frase:str)->str:
    '''Função que dada uma string (frase), retorna a mesma frase, só que com todas as consoantes maiúsculas'''
    count = 0
    aux = []
    while count < len(frase):
        if frase[count] in 'bcçdfghjklmnpqrstvwxyz':
            aux.append(frase[count].upper())
        else:
            aux.append(frase[count])
        count += 1
    return ''.join(aux)

## ===========================
## Questão 3: Posição da Letra
## ===========================

## Faça uma função chamada **posLetra** que recebe como entrada uma string, uma letra,
## e um número que indica a ocorrência desejada da letra (1 para primeira ocorrência, 2 para segunda, etc).
## Sua função deve retornar em que posição da string aquela ocorrência da letra está.
## Caso exista menos ocorrências da letra do que a ocorrência pedida, a função deveretornar -1.
##
## Exemplo:
##
## >>> posLetra("mariana come banana", 'a', 3)
##
## 6
##
## (posição da terceira ocorrência da letra 'a' na string dada)

def posLetra(string:str, letra:str, numero:int)->int:
    '''Função que dada uma string (string), um caractere (letra) e um número (numero), retorna a posição da ocorrência numero do caractere letra na string'''
    posicao = -1
    while numero > 0:
        posicao += 1
        if posicao == len(string):
            return -1
        elif string[posicao] == letra:
            numero -= 1
    return posicao

## ====================
## Questão 4: Repetidos
## ====================

## Faça uma função chamada **repetidos** que receba como entrada uma lista de números,
## e retorne o número de vezes que um elemento da lista é igual ao elemento anterior.
## Exemplo: repetidos([1,4,3,3,2,3,3,3,3,5,4,6,6,7,6,8,8,7])
## Resposta: 6.

def repetidos(lista:list)->int:
    '''Função que dada uma lista (lista), retorna a quantidade de vezes que um elemento da lista é igual ao seu anterior'''
    vezes = 0
    count = 1
    while count < len(lista):
        if lista[count] == lista[count-1]:
            vezes += 1
        count += 1
    return vezes

## ===================
## Questão 5: Fatorial
## ===================

## Faça uma função chamada **fatorial** que dado um número, calcule o fatorial deste número. (Não usar a função factorial do módulo math)

def fatorial(numero:int)->int:
    '''Função que dado um número (numero), calcula seu faltorial'''
    count = 1
    aux = numero
    while count < aux:
        numero*= count
        count += 1
    return numero

## =======================
## Questão 6: Peça Perdida
## =======================

## *Questão OBI (Olimpíada Brasileira de Informática - OBI2007, Fase 1, Nível 1) - (Peça Perdida)*
##
## Joãozinho adora quebra-cabeças, essa é sua brincadeira favorita. O grande problema, porém, é que às vezes o jogo vem com uma peça faltando.
## Isso irrita bastante o pobre menino, que tem de descobrir qual peça está faltando e solicitar uma peça de reposição ao fabricante do jogo.
## Sabendo que o quebra-cabeças tem N peças, numeradas de 1 a N e que exatamente uma está faltando, ajude Joãozinho a saber qual peça ele tem de pedir.
##
## Escreva uma função chamada **faltante** que, dada uma lista com N − 1 inteiros numerados de 1 a N,
## descubra qual número inteiro deste intervalo está faltando.
##
## - **Entrada:** O parâmetro de entrada é uma lista L de tamanho N − 1 contendo números inteiros (não repetidos) de 1 a N.
## - **Saída:** A sua função deve retornar o número inteiro x que pertence ao intervalo [1, N] mas que não pertence a lista de entrada L.
##
## Exemplos:
##
## - Entrada: [3,1];
## Saída: 2
## - Entrada: [1,2,3,5] ;
##
## Saída: 4
## - Entrada: [2,4,3] ;
## Saída: 1

def faltante(L:list)->int:
    '''Função que dada uma lista (L) inteiros numerados (1 - N), retorna o termo que pertence ao intervado da lista, mas não está presente na lisa'''
    L.sort()
    x = 0
    while x < len(L):
        if L[x] != x+1:
            break
        x += 1
    return x+1

#-------------------------------------------------------------------------------------------------------------------------#
