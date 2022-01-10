#-------------------------------------------------------------------------------------------------------------------------#
## =============================================================================================
## S E M A N A  4  -  V A R I Á V E I S  E  A T R I B U I Ç Ã O ,  S T R I N G S  E  T U P L A S
## =============================================================================================

## =======================
## Questão 1: Concatenação
## =======================

## Considere que *a* e *b* são duas strings à escolha do usuário. Faça uma função, chamada **concatenacao**,
## que retorne a concatenação delas no formato *abba*.

def concatenacao(a:str, b:str)->str:
    '''Função que dadas duas strings (a e b), as une da forma abba'''
    return a+b+b+a

## =======================
## Questão 2: Substituição
## =======================

## Escreva uma função definida por **substitui(s, x, i)** que receba uma string *s*, um caractere *x* e um
## número inteiro *i* entre 0 e o comprimento da string, e retorne uma string igual a *s*,
## exceto que o elemento da posição *i* deve ser substituído pelo caractere *x*.

def substitui(s:str,x:str,i:int)->str:
    '''Função que dada uma string (s), um caractere (x) e um número (i), substitui o caractere na posição i de s pelo caractere x'''
    return s[:i] + x + s[i+1:]

## ==================
## Questão 3: Hashtag
## ==================

## Escreva uma função chamada **hashtag** que receba uma string e insira o caractere ”#” no início,
## no meio e no final dela. Por exemplo, se a entrada for ”abcd”, a saída deve ser ”#ab#cd#”.
## Outro exemplo: se receber ”abcde”, a função deve retornar ”#ab#cde#”.

def hashtag(s:str)->str:
    '''Função que dada uma string (s), insere um # no início, um no meio e um no final da string'''
    return '#'+s[:len(s)//2]+'#'+s[len(s)//2:]+'#'

## ====================
## Questão 4: Filtragem
## ====================

## Faça uma função chamada **filtra_pares** que receba uma tupla com quatro elementos inteiros como parâmetro,
## e retorne uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam.
## Esse tipo de operação onde se selecionam elementos de um conjunto inicial que satisfazem uma determinada propriedade é bastante comum em computação,
## e se chama **filtragem**.
##
## Dica: Verifique cada elemento da tupla de entrada um por um!

def filtra_pares(tupla:tuple)->tuple:
    '''Função que dada uma tupla com 4 elementos, retorna outra tupla com apenas os elementos pares da primeira'''
    aux = ()
    if tupla[0]&1 == 0:
        aux += tupla[0],
    if tupla[1]&1 == 0:
    	aux += tupla[1],
    if tupla[2]&1 == 0:
    	aux += tupla[2],
    if tupla[3]&1 == 0:
    	aux += tupla[3],
    return aux

## =========================================
## Questão 5: Detectando colisões com tuplas
## =========================================

## Questão OBI (Olimpíada Brasileira de Informática - 2007, Fase 1, Nível 1) - (http://olimpiada.ic.unicamp.br/pratique/programacao/nivel1/2007f1p1_colisoes)
##
## Detecção de colisão é uma das operações mais comuns (e importantes) em jogos eletrônicos. O objetivo, basicamente, é verificar se dois objetos quaisquer colidiram,
## ou seja, se a interseção entre eles é diferente de vazio. Isso pode ser usado para saber se duas naves colidiram, se um monstro bateu numa parede, se um personagem pegou um item, etc.
##
## Para facilitar as coisas, muitas vezes os objetos são aproximados por figuras geométricas simples (esferas, paralelepípedos, triângulos etc).
## Neste problema, os objetos são aproximados por retângulos num plano 2D.
##
## Escreva uma função chamada **colisao** que, dados dois retângulos, determine se eles se interceptam ou não.
## Cada retângulo é determinado pelas coordenadas x e y de dois de seus vértices diametralmente opostos, representando a diagonal que vai da esquerda para a direita e de baixo para cima.
## Os lados de cada retângulo são sempre paralelos aos eixos x e y.
##
## **Entrada:** Os parâmetros de entrada são duas tuplas com quatro valores inteiros cada uma, representando as coordenadas do primeiro retângulo e as coordenadas do segundo retângulo.
##
## **Saída:** A sua função deve retornar o valor booleano True caso haja interseção ou False, caso não haja.
##
## **Exemplos**
##
## Entrada: (0,0,1,1), (0,0,1,1) ; Saída: True
##
## Entrada: (0,0,2,2), (1,1,3,3) ; Saída: True
##
## Entrada: (0,0,1,1), (2,2,3,3) ; Saída: False

def colisao(ret1:tuple,ret2:tuple)->bool:
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.'''

    # primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

    # segunda etapa - calculo do resultado
    if x_inf_esq1 > x_sup_dir2 or x_inf_esq2 > x_sup_dir1:
        return False
    elif y_inf_esq1 > y_sup_dir2 or y_inf_esq2 > y_sup_dir2:
        return False
    return True

#-------------------------------------------------------------------------------------------------------------------------#
