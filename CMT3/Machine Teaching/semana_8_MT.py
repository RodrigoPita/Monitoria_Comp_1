#-------------------------------------------------------------------------------------------------------------------------#
## ========================================================================================
## S E M A N A  8  -  E S T R U T U R A  D E  R E P E T I Ç Ã O  I T E R A D O R A :  F O R
## ========================================================================================

## =================================
## Questão 1: Frequência de palavras
## =================================

## Construa uma função chamada **freq_palavras(frases)** que receba uma string e retorne um dicionário
## onde cada palavra dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece. Por exemplo:
##
## - freq_palavras("dinheiro é dinheiro e vice versa")
##
## Retorna o dicionário: { "dinheiro":2, "é": 1, "e": 1, "vice": 1, "versa":1}

def freq_palavras(frases:str)->dict:
    '''Função que dada uma string (frases), retorna um dicionário com cada palavra presente na string e sua frequência relativa'''
    D = {}
    frases = frases.split()
    for i in frases:
        if i in D:
            D[i] += 1
        else:
            D[i] = 1
    return D

## ==================
## Questão 2: Compras
## ==================

## Escreva uma função chamada **total** que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja,
## e retorna o valor total dos itens da lista que estejam disponíveis nesta loja. Por exemplo, para os dados:
## - lista de compras = [’biscoito’, ’chocolate’, ’farinha’]
## - produtos = { ’amaciante’:4.99, ’arroz’:10.90, ’biscoito’:1.69, ’cafe’:6.98, ’chocolate’:3.79, ’farinha’:2.99 }
##
## O valor retornado pela função será 8.47.

def total(lista_compras:list, preco_produto:dict)->int:
    '''Função que dados uma lista (lista_compras) e um dicionário (preco_produto), retorna a soma dos valores dos produtos da lista'''  
    preco = 0
    for i in lista_compras:
        if i in preco_produto:
            preco += preco_produto[i]
	return round(preco, 2)

## ======================
## Questão 3: Língua do P
## ======================

## Faça uma função chamada **lingua_p** que receba como parâmetro uma palavra (em português) e retorne esta mesma palavra traduzida para a língua do P.
## Uma palavra foi traduzida para a língua do P quando, após cada vogal da palavra original, é inserida a sequência de letras 'p' mais a vogal original.
## A resposta deve ignorar a diferença entre minúsculas e maiúsculas e retornar a palavra traduzida toda em minúsculas.
##
## Por exemplo:
## 
## exemplo → epexepemplopo
##
## entao → epentapaopo
##
## Caderno → capadepernopo

def lingua_p(palavra:str)->str:
    '''Função que a partir da string (palavra), retorna uma string modificada para que a palavra atenda os requisitos da língua do P'''
    palavra = palavra.lower()
    aux = ''
    for i in palavra:
        if i in 'aáàâãeéiíoóôõuú':
            aux += i + 'p' + i
        else:
            aux += i
	return aux

## ====================
## Questão 4: Divisores
## ====================

## Faça uma função chamada **qtd_divisores** que conte quantos divisores um número tem. Este número será passado como entrada.
##
## Exemplo: Se o número for 10, os divisores são: 1, 2, 5 e 10; total de 4 divisores.

def qtd_divisores(numero:int)->int:
    '''Função que recebe um inteiro (numero) e retorna quantos divisores ele tem'''
    divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
	return divisores

## =========================
## Questão 5: Números primos
## =========================

## Faça uma função chamada **primo** que dado um número inteiro positivo, verifique se este número é primo ou não. Retorne um valor booleano.
## Dica: uma estratégia simples para identificar a primalidade de um número é verificar se não existe nenhum número menor que ele próprio (e maior ou igual a 2) que o divida.
## Dica 2: O número de divisões indicado na dica anterior é maior que o necessário. Você consegue reduzi-lo?

def primo(numero:int)->bool:
    '''Função que verifica se um inteiro (numero) é primo'''
    teto = round(numero**(1/2))
    for i in range(2, teto + 1):
        if numero % i == 0:
            return False
	return True

## =================
## Questão 6: Soma H
## =================

## Sendo
##
## H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N
##
## Faça uma função chamada **soma_h** para calcular e retornar o valor H com N termos onde N é inteiro e dado com entrada.
## **Retorne seu resultado somente com 2 casas decimais, utilizando a função \`round(número, 2)\`.**

def soma_h(N:int)->int:
    '''Função que dado um inteiro (N), calcula H, para
    H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N'''
    H = 0
    for i in range(1, N+1):
        H += 1/i
	return round(H, 2)

#-------------------------------------------------------------------------------------------------------------------------#
