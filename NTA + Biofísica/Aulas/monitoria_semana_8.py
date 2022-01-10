# Questão 1

# a)
def soma_serie(n):
    '''Dado n, calcula a soma da série
    1 - 1/3 + 1/5 - 1/7 + ... + ((-1)**n)/(2*n + 1)
    int --> float'''
    
    # variável para guardar o valor da soma
    soma = 0
    
    # usamos o ponto de parada (n+1) para que n seja o último valor de i
    for i in range(n+1):
        # incrementamos a soma com o próximo valor da série
        soma += ((-1)**i)/(2*i + 1)
    return soma

# b)
from math import fabs, pi
def erro_serie():
    '''Calcula a soma da série 
    1 - 1/3 + 1/5 - 1/7 + ... + ((-1)**n)/(2*n + 1)
    com erro (serie - pi/4 < 0.01)
    --> tuple'''

    # variáveis para guardar o valor da soma e do iterador
    soma, i = 0, 0

    # enquanto o erro não for menor que 0.01, seguimos com a soma da série
    while fabs(soma - pi/4) >= 0.01:
        #chamada para a função definida no item a
        soma = soma_serie(i)
        #incrementamos o iterador
        i += 1
    return (soma, i)

# Questão 2
def contatos(lista_contatos, nome):
    '''Busca os dados de um contato numa lista, através do nome dado
    list, str --> list'''
    lista_retorno = []

    # itera pela lista com o i uma sublista a cada iteração
    for i in lista_contatos:
        # verifica se a string nome pertence a string da primeira posição na sublista i
        if nome.lower() in i[0].lower():
            # adiciona as informações da pessoa com o nome procurado na lista de retorno
            lista_retorno.append(i)
    return lista_retorno

# Questão 1 - MT
from math import factorial
def soma_fatorial(n):
    '''Calcula a soma dos fatoriais de 1 até n
    int --> int'''

    # variável para guardar o valor da soma
    soma = 0

    # itera no intervalo de n até 1 com passo -1
    for i in range(n, 0, -1):
        # incrementamos a soma com o fatorial seguinte
        soma += factorial(i)
    return soma
    
# Questão 2 - MT
def qtd_divisores(n):
    '''Calcula a quantidade de divisores de n
    int --> int'''

    # variável para guardar o total de divisores de n
    total = 0

    # itera no intervalo de 1 até n
    for i in range(1, n+1):
        # verifica se i é divisor de n
        if n % i == 0:
            # incrementa o total em uma unidade
            total += 1
    return total

# Questão 3 - MT
def primo(n):
    '''Verifica se n é primo
    int --> bool'''

    # Para identificar a primalidade de um número,
    # basta verificar se existe um número
    # menor ou igual à raiz quadrada dele que o divida
    ponto_parada = round(n**(1/2)) + 1

    # itera pelo intervalo de 2 a 1 mais a raiz quadrada de n
    for i in range(2, ponto_parada):
        # verifica se i é divisor de n
        if n % i == 0:
            # n não é primo
            return False
    # n é primo
    return True

# Questão 4 - MT
def soma_h(n):
    '''Calcula o valor da soma
    H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
    int --> float'''

    # variável para guardar o valor da soma
    soma = 0

    # itera pelo intervalo de 1 até n
    for i in range(1, n+1):
        # incrementa o próximo termo de H à variável soma
        soma += 1/i
    return soma

# Questão 5 - MT
def soma():
    '''Calcula o valor da soma
    S = 10/1! - 9/2! + 8/3! - 7/4! + ... - 1/10!
    --> float'''

    # variáveis para guardar o valor da soma e de parada
    s, parada = 0, 11

    # itera no intervalo de 1 a 10
    for i in range(1, parada):
        # variável auxiliar para altenar o sinal da soma em cada iteração
        aux = (-1)**(i-1)
        # incrementa o próximo termo da soma à variável s
        s += ((parada - i)/factorial(i)) * aux
    return s
    
# Questão 6 - MT
def lingua_p(palavra):
    '''Traduz uma palavra em português para uma na língua do P
    exemplo --> epexepemplopo
    str --> str'''

    # variável para guardar a palavra traduzida
    palavra_p = ''

    # itera pela palavra
    for i in palavra.lower():
        # verifica se o caractere em i é uma vogal
        if i in 'aáàâãeéèêiíìîoóôõuúùû':
            # adiciona p entre a vogal em i à palavra traduzida
            palavra_p += i + 'p' + i
        else:
            # adiciona a consoante em i à palavra traduzida
            palavra_p += i
    return palavra_p

# Questão 7 - MT
def freq_palavras(frases):
    '''Calcula a frequência de cada palavra em uma string
    retornando um dicionário com as palavras e suas respectivas frequências
    str --> dict'''

    # dicionário para guardar as palavras e suas frequências
    freq_por_palavra = {}
    # transforma frases numa lista com cada termo sendo uma palavra
    frases = frases.split()

    # itera pela lista frases
    for i in frases:
        # verifica se a palavra em i já está no dicionário
        if i in freq_por_palavra:
            # incrementa em uma unidade a frequência da palavra em i 
            freq_por_palavra[i] += 1
        else:
            # adiciona a palavra em i no dicionário com frequência igual a 1
            freq_por_palavra[i] = 1
    return freq_por_palavra

# Questão 8 - MT
def total(lista_compras, preco_por_produto):
    '''Calcula o valor total dos produtos na lista de compras,
    a partir dos preços no dicionário
    list, dict --> float'''

    # variável para guardar o valor total do preço
    preco = 0

    # itera pela lista de compras
    for i in lista_compras:
        # verifica se o produto em i está no dicionário
        if i in preco_por_produto:
            # incrementa o preço referente ao produto em i à variável preco
            preco += preco_por_produto[i]
    return round(preco, 2)
