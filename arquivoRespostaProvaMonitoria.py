# =====================================
# EDITE SOMENTE OS PARÂMETROS DO FORMAT
# =====================================
__doc__ = """
====================
Prova de Seleção
 Monitoria 2021.1
====================
--------------
Indentificação
--------------
 Nome: {nome}
 DRE: {dre}
 Curso de Origem: {curso}
---------
Pontuação
---------
 Questão | 1 | 2 | 3 | 4 | 5 | Total
 ---------------------------------------------
 Valor | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 10.0
 ---------------------------------------------
 Nota | | | | | |

""".format( # AQUI EMBAIXO

 nome="Rodrigo Côrtes Nogueira da Rocha Pita",

 dre="118187443",

 curso="Bacharelado em Ciência da Computação"
 )
# ===========
# OBSERVAÇÕES
# ===========
# > Dê nomes elucidativos, ou seja, que se auto explique, a suasfunções/métodos
# e variáveis/atributos;
#
# > Insira um comentário antes de cada linha de código descrevendosua funcio-
# nalidade de forma clara e sucinta;
#
# > Documente suas classes, funções e parâmetros.
#
# =========
# Questão 1
# =========
# Preencha as linhas de comentário em branco, descrevendo,
# de forma clara e resumida, a linha de código que a sucede
# dentro de seu contexto.
def ordenaPorInsercao(numeros: list[int, float]) -> list[int, float]:
    '''Ordena a lista numerica de forma crescente
    seguindo o método da inserção'''
    # Iniciando um indice
    indice = 1
    # Loop no "indice" até alcançar o último indice
    # da lista "numeros"
    while indice < len(numeros):
        # Verifica se o termo da lista numeros na posição indice é menor que seu antecessor
        if numeros[indice] < numeros[indice-1]:
            # Removendo número da respectiva posicao
            # e colocando o mesmo na variável pivo
            pivo = numeros.pop(indice)

            # Colocando o pivo (inicializado acima) na posição anterior a indice
            numeros.insert(indice-1, pivo)

            # Armazenando indice anterior
            indiceAnterior = indice - 1

            # Loop enquanto a variável indiceAnterior for maior que zero
            while indiceAnterior > 0:
                # Verifica se o termo da lista numeros na posição indiceAnterior e menor que seu antecessor
                if numeros[indiceAnterior] < numeros[indiceAnterior-1]:
                    # Removendo numero da posição indiceAnterior
                    # e colocando o mesmo na variável pivo
                    pivo = numeros.pop(indiceAnterior)
                    # Colocando o pivo (inicializado acima) na posição anterior a indiceAnterior
                    numeros.insert(indiceAnterior-1, pivo)

                # Atualizando indice anterior
                indiceAnterior -= 1

            # Incrementa o indice para dar continuidade ao loop
            indice = indice + 1

    return numeros

# =========
# Questão 2
# =========

# Referente a calculos matriciais, implemente as seguintes
# FUNÇÕES:
#
# a) somaMatrizes:
# Que, dadas DUAS matrizes, retorne a matriz resultan-
# te da soma entre elas;
#
# b) produtoMatrizes:
# Que, dadas DUAS matrizes, retorne a matriz resultan-
# te do produto entre elas;
#
# c) determinante:
# Que, dada UMA matriz tridiagonal, retorne o determi-
# nante dela.
#
# OBS: Utilize ESTRUTURAS CONDICIONAIS para contornar, onde
# for necessário, os seguintes casos:
#
# > Matrizes Desalinhadas:
# Numero de linhas e colunas não compatíveis;
#
# > Matriz fora do formato esperado:
# A matriz não está de acordo com o previamente espera-
# do.

# RESPOSTA...

# Importa numpy com o "apelido" np
import numpy as np

# a)
# Define a função para calcular a soma entre duas matrizes
def somaMatrizes(matriz1:list, matriz2:list)->list:
    # Verifica se a matriz1 tem número de linhas e colunas compatível
    if(!verifica(matriz1):
       # Imprime mensagem de erro
       print("Tamanho de matriz errado")

    # Verifica se a matriz2 tem número de linhas e colunas compatível
    if(!verifica(matriz2):
       # Imprime mensagem de erro
       print("Tamanho de matriz errado")
    
    # Cria m1 como a matriz1 para numpy
    m1 = np.matrix(matriz1)

    # Cria m2 como a matriz2 para numpy
    m2 = np.matrix(matriz2)

    # Retorna a matriz resultado da soma das matrizes de entrada
    return m1 + m2

# b)
# Define a função para calcular o produto entre duas matrizes
def produtoMatrizes(matriz1:list, matriz2:list)->list:
    # Verifica se a matriz1 tem número de linhas e colunas compatível
    if(!verifica(matriz1):
       # Imprime mensagem de erro
       print("Tamanho de matriz errado")

    # Verifica se a matriz2 tem número de linhas e colunas compatível
    if(!verifica(matriz2):
       # Imprime mensagem de erro
       print("Tamanho de matriz errado")
       
    # Cria m1 como a matriz1 para numpy
    m1 = np.matrix(matriz1)

    # Cria m2 como a matriz2 para numpy
    m2 = np.matrix(matriz2)

    # Retorna a matriz resultado do produto das matrizes de entrada
    return m1 * m2

# c)
#
def determinante(matriz:list[list])->int:
    # Verifica se a matriz tem número de linhas e colunas compatível
    if(!verifica(matriz)):
        # Imprime mensagem de erro
        print("Tamanho de matriz errado")
        
    # Verifica se a matriz está no formato certo
    if(!ehTriDiag(matriz)):
        # Imprime mensagem de erro
        print("Formato de matriz errado")
        
    # Retorna o determinante da matriz
    return np.linalg.det(triDiag)

def verifica(matriz:list)->bool:
    if len(matriz[0][:]) != len(matriz[:][0]):
        return False
    else:
        return True
def ehTriDiag(matriz:list)->bool:
    # Salva o tamanho da matriz original em uma variável
    tamanhoMatriz = len(matriz)

    # Cria o corpo da matriz tridiagonal
    triDiag = [[0 for j in range(tamanhoMatriz)]
                for i in range(tamanhoMatriz)]

    # Itera pelo tamanho da matriz
    for i in range(0, tamanhoMatriz):
        # Verifica se está na última iteração
        if i == tamanhoMatriz-1:
            triDiag[i][i] = matriz[i][i]
            continue

        # Adiciona a diagonal principal a nova matriz
        triDiag[i][i] = matriz[i][i]

        # Adiciona a diagonal acima da principal a nova matriz
        triDiag[i][i+1] = matriz[i][i+1]

        # Adiciona a diagonal abaixo da principal a nova matriz
        triDiag[i+1][i] = matriz[i+1][i]
    if matriz == triDiag:
        return True
    else:
        return False
    
# =========
# Questão 3
# =========
# Escreva um código fazendo o devido TRATAMENTO DE EXCEÇÕES
# da seguinte interação com o usuário:
# Recebendo a posicao do usuario
posicao = input("\n> Digite a posicao [x,y]: ")
# Avaliando a posicao
posicao = eval(posicao)
# OBS:
# > Implemente seu código resposta ao redor do comando
# já digitado acima.
#
# > O "devido" tratamento, consiste em imprimir:
# >> uma mensagem notificando o erro;
# >> uma solução.
#
# > Contorne, pelo menos, 3 tipos de erro!
# =========
# Questão 4
# =========
# Considerando as funções abaixo
def imprime(matriz: list[list[int]]):
 return print(*matriz, sep='\n', end='\n\n')
def adicionaParametro(f: "function", param: str):
 # Obtendo os parâmetros da função f
 vars = f.__code__.co_varnames
 # Colocando as variáveis lado a lado
 vars = (len(vars)*"{}, ").format(*vars)

 return eval(f"lambda {vars}{param}: f({vars})")
def adiconaValor(lista: list, valor: "Any"):
 lista.append(valor)
# Analise as seguintes setenças a respeito do conteúdo destas
# funções:
#
# I. O tipo do valor de retorno da função "imprime" é "str";
#
# II. O tipo do valor de retorno da função "imprime" é None;
#
# III. Ao executar a função "adicionaParametro", CERTAMENTE
# ocorrerá um erro, mesmo que os parâmetros sejam
# os esperados;
#
# IV. O tipo do valor de retorno da função "adicionaValor"
# é "list";
#
# V. O tipo do valor de retorno da função "adicionaParametro"
# é "lambda";
#
# É correto afirmar que:
# a) As alternativas I e IV estão certas!
#
# b) Apenas a alternativa II está certa!
#
# c) As alternativas II e V estão certas!
#
# d) Apenas a alternativa I está errada!
#
# e) Nenhuma alternativa está certa!
# Responda aqui a alternativa!
OBJETIVA = "x"
# Justifique os itens falsos considerando a alternativa
# escolhida!
JUSTIFICATIVA = "..."
# =========
# Questão 5
# =========
# Crie uma CLASSE "Prova" que receba:
#
# > o nome da instituição: str *
# > o nome da disciplina: str *
# > o nome do professor: str *
# > o nome do aluno: str *
# > o numero do dre: int *
# > o numero de questoes: int
#
# para instanciar objetos capazes de estruturar e preencher
# avaliações acadêmicas.
#
# Abaixo constam mais informações sobre esta classe:
#
# > O MÉTODO CONSTRUTOR deve criar atributos com as in-
# formações recebidas marcadas com "*" e um DICIONÁRIO
# com o par (numero da questão, enunciado), onde o con-
# údo incial do enunciado é uma STRING VAZIA.
#
# > Um MÉTODO para enunciar as questões, que recebendo:
#
# >> numero da questão: int
#
# >> enunciado: str
#
# atualiza o atributo do DICIONÁRIO.
#
# > Quando executado o comando "print(instanciaProva)",
# sejá exibida uma string minimamente formatada, se-
# guindo a estrutura:#
#
# CABEÇALHO
#
# QUESTAO 1: Enunciado
#
# ...
#
# QUESTAO N: Enunciado
# RESPOSTA...
