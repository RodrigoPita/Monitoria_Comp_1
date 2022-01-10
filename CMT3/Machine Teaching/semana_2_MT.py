#-------------------------------------------------------------------------------------------------------------------------#
## ===============================================================
## S E M A N A  2  -  F U N Ç Õ E S  E   T I P O S  D E  D A D O S
## ===============================================================

## =================
## Questão 1: Bombom
## =================

## Pedrinho quer comprar o maior número de bombons possível com o dinheiro que tem.
## Faça uma função chamada **num_bombons** para calcular quantos bombons ele consegue comprar,
## dados o dinheiro e o preço do bombom para realização da compra.

def num_bombons(dinheiro:float, preco:float)->float:
    '''Função que calcula quantos bomboms podem ser comprados
    de acordo com o dinheiro e preço (>0) dados'''
    return dinheiro//preco

## =========================
## Questão 2: Quantos carros
## =========================

## Um grupo de amigos deseja fazer uma viagem e decidiram ir de carro.
## Pelas regras rodoviárias um veículo convencional tem a capacidade de transportar até 5 passageiros,
## porém há veículos com outras capacidades. Construa uma função em Python chamada **carros**
## para calcular e retornar o número exato de carros necessários para esta viagem,
## considerando que seja dado como entrada o número de pessoas.
## Caso os veículos considerados sejam de capacidades não convencionais,
## será dado também como entrada a capacidade dos veículos, considerando que todos os veículos são iguais.

import math
def carros(pessoas:int, capacidade:int=5)->int:
    '''Função que calcula quantos carros serão necessários, dado o número de pessoas e a capacidade dos carros'''
    return math.ceil(pessoas/capacidade)

## ================
## Questão 3: Bolos
## ================

## *Questão OBI (Olimpíada Brasileira de Informática - OBI2012, Fase 2, Nível Júnior) - (Receita de Bolo)*
##
## João deseja fazer bolos para seus amigos, usando uma receita que indica que devem ser usadas 2 xícaras de farinha de trigo, 3 ovos e 5 colheres de sopa de leite.
## Em casa ele tem **A** xícaras de farinha de trigo, **B** ovos e **C** colheres de sopa de leite. João não tem muita prática com a cozinha, e portanto ele só se arriscará a
## fazer medidas exatas da receita de bolo (por exemplo, se ele tiver material suficiente para fazer mais do que 2 e menos do que 3 bolos, ele fará somente 2 bolos).
## Sabendo disto, ajude João escrevendo uma função chamada **bolos** que determine qual a quantidade máxima de bolos que ele consegue fazer.
##
## - **Entrada:** Os parâmetros de entrada da função são três números inteiros A, B e C,
##   indicando respectivamente o número de xícaras de farinha de trigo, o número de ovos e o número de colheres de sopa de leite que João tem em casa.
##
## - **Saída:** Sua função deve retornar a quantidade máxima de bolos que João consegue fazer.
##
## Exemplos:
##
## - Entrada: 4, 6, 10;
## Saída: 2
## - Entrada: 4, 6, 9 ;
## Saída: 1

def bolos(A:int, B:int, C:int)->int:
    '''Função que calculao máximo de bolos possíveis de fazer, dadas as quantidades de cada ingrediente (A, B, C)'''
    return min(A//2, B//3, C//5)

#-------------------------------------------------------------------------------------------------------------------------#
