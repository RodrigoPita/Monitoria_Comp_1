#-------------------------------------------------------------------------------------------------------------------------#
## ===========================================================================================
## S E M A N A  5  -  M A N I P U L A Ç Ã O  D E  S T R I N G S ,  T U P L A S  E  L I S T A S
## ===========================================================================================

## =================================
## Questão 1: Quantidade de palavras
## =================================

## Faça uma função definida por **quant_palavras(frase)** que dada uma frase, retorne o número de palavras da frase.
## Considere que a frase pode ter espaços no início e no final.
##
## **Dica: veja a função split()**

def quant_palavras(frase:str)->int:
    '''Função que dada uma string (frase), calcula a quantidade de palavras nela'''
    return len(frase.split(' '))

## =======================
## Questão 2: Conta frases
## =======================

## Dado um texto armazenado em uma string, faça a função **conta_frases** que conte o número de frases que aparecem neste texto.
## Cada frase no texto é terminada com um ponto final, um ponto de exclamação, um ponto de interrogação ou três pontos em sequência (reticências).
## Pontos de exclamação ou de interrogação não aparecerão repetidos em sequência no texto e esses símbolos só aparecem no texto terminando uma frase.
## No exemplo a seguir, são contadas 4 frases: “Preciso tirar um cochilo. Meus Deus! Que horas são? Vou perder a minha aula...”

def conta_frases(texto:str)->int:
    '''Função que dada uma string (texto), calcula a quantidade de frases nela'''
    texto = (((texto.replace('...', '.')).replace('?', '.')).replace('!', '.'))
    return len(texto.split('.'))-1

## ==============================
## Questão 3: Intercalando listas
## ==============================

## Faça uma função chamada definida por **\`intercala(lista1, lista2)\`** que dadas duas listas L1 e L2 de tamanho 3,
## gera uma lista L3 que é formada intercalando os elementos de L1 e L2.
##
## Exemplo:
## L1 = [1, 3, 5] e L2 = [2, 4, 6] gera L3 = [1, 2, 3, 4, 5, 6].

def intercala(lista1:list, lista2:list)->list:
    '''Função que dadas duas listas (lista1, lista2), intercala os termos de ambas em uma nova lista'''
    return [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]

## ===========================
## Questão 4: Retira pontuação
## ===========================

## Faça uma função **retira_pontuacao** que, dada uma frase, retorne a frase onde todos os caracteres de pontuação (incluindo travessão,
## vírgula, dois pontos, ponto e vírgula, além da pontuação de encerramento de frase) tenham sido substituídos por espaço.

def retira_pontuacao(frase:str)->str:
    '''Função que dada uma string (frase), retorna uma string sem as pontuações'''
    return frase.replace('-', ' ').replace(',', ' ').replace(':', ' ').replace(';', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace('...', ' ')

## =============================
## Questão 5: De trás pra frente
## =============================

## Faça uma função chamada **inverte** que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa,
## sem letras maiúsculas, e sem a pontuação. Dica: remova a pontuação da frase, usando a função que você fez pro exercício anterior.
## Exemplo:
##
## frase lida: “Nossa, como eu gosto de chocolate.”
##
## frase alterada: “chocolate de gosto eu como nossa”
##
## DICA: remova a pontuação da frase, usando a função que você fez pro exercício anterior. Para reaproveitar uma função feita no Machine Teaching,
## copie o código completo da função e cole na caixa de resposta do exercício onde quer utilizá-la. Faça então a função pedida no exercício,
## embaixo da que você colou, e dentro dela você irá chamar a que está reutilizando.

def retira_pontuacaoX(frase:str)->str:
    return frase.replace('-', ' ').replace(',', '').replace(':', '').replace(';', '').replace('.', '').replace('!', '').replace('?', '').replace('...', '')

def inverte(frase:str)->str:
    '''Função que dada uma string (frase), retorne a mesma string, só que invertida,
    sem pontuações e com tudo minúsculo'''
    frase = retira_pontuacaoX(frase).lower().split(' ')
    frase.reverse()
    return ' '.join(frase)

## ==============================
## Questão 6: Pirâmide de números
## ==============================

## Faça uma função **piramide_num** que construa uma pirâmide de números inteiros, dados dois números.
## Uma pirâmide de números é na verdade uma sequência de números com as seguintes características:
##
## 1. o primeiro valor passado como parâmetro deverá ser o primeiro e o último elemento da sequência, marcando o início e fim da sequência;
## 2. cada valor dentro da sequência não pode ter uma diferença absoluta maior que um de seu vizinho à direita ou à esquerda.
## 3. o segundo número dado como entrad, estará no meio dela.
## 4. todos os números na pirâmide aparecem duas vezes na sequência com exceção daquele que está no meio.
##
## Sua função receberá como entrada dois números inteiros, e deve retornar uma lista com a sequência correspondente à pirâmide.
##
## Exemplos:
##
## >>> piramide(3,6)
## [3,4,5,6,5,4,3]
## >>> piramide(9,6)
## [9,8,7,6,7,8,9]
## >>> piramide(6,6)
## [6]

def piramide_num(numero1:int, numero2:int)->list:
    '''Função que dados dois números (numero1, numero2), cria uma lista começando o numero1,
    indo até o numero2 e voltando ao numero1, em forma de pirâmide'''
    if numero2 < numero1:
        return list(range(numero1, numero2, -1))+list(range(numero2, numero1+1))
    return list(range(numero1, numero2))+list(range(numero2, numero1-1, -1))

## ==================
## Questão 7: Colchão
## ==================

## *Questão OBI (Olimpíada Brasileira de Informática - OBI2012, Fase 1, Nível 2) - (Colchão)*
##
## João está comprando móveis novos para sua casa. Agora é a vez de comprar um colchão novo, de molas, para substituir o colchão velho.
## As portas de sua casa têm **altura H** e **largura L** e existe um colchão que está em promoção com dimensões A × B × C.
## O colchão tem a forma de um paralelepípedo reto retângulo e João só consegue arrastá-lo através de uma porta com uma de suas faces paralelas ao chão,
## mas consegue virar e rotacionar o colchão antes de passar pela porta. Entretanto, de nada adianta ele comprar o colchão se ele não passar através das portas de sua casa.
## Portanto ele quer saber se consegue passar o colchão pelas portas e para isso precisa de sua ajuda.
## Faça uma função definida por **colchao(medidas,H,L)** para resolver esse problema,
## onde medidas é uma lista com os tamanhos inteiros A, B e C, e H e L são os tamanhos inteiros da altura e largura da porta, respectivamente.
##
## - **Entrada:** Os parâmetros de entrada são uma lista com as dimensões do colchão em centímetros, ordenadas da menor para a maior, e dois inteiros H e L,
## correspondentes respectivamente a altura e a largura das portas em centímetros.
## - **Saída:** A sua função deve retornar True se o colchão passa pelas portas e False caso contrário.
##
## Exemplos:
##
## - Entrada: [25,120,220], 200, 100 ;
## Saída: True
## - Entrada: [25,205,220], 200, 100 ;
## Saída: False
## - Entrada: [25,200,220], 200, 100 ;
## Saída: True

def colchao(medidas:list, H:int, L:int)->bool:
    '''Função que dada uma lista (medidas) com as dimensões de um colchão, a altura (H) e largura (L) de uma porta,
    diz se é possível passar o colchão pela porta'''
    if (medidas[0] <= H and medidas[1] <= L) or (medidas[0] <= L and medidas[1] <= H):
        return True
    return False

#-------------------------------------------------------------------------------------------------------------------------#
