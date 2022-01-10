#Gabarito MT 5

#Q1
def qtde_pal(frase):
    """Retorna o número de palavras da frase.
    str -> int"""
    #Tiramos espaços iniciais ou finais
    frase = frase.strip()
    #Contamos os espaços
    qtde = frase.count(' ')
    #O número de palavras será o número de espaços + 1
    return qtde + 1

#Q2
def qtde_frase(texto):
    """Conta o número de frases que aparecem no texto inserido.
    str -> int"""
    #Contamos todos as possíveis terminações de frases
    qtde = texto.count('!') + texto.count('?')
    ret = frase.count('...')
    #Temos que tirar os pontos a mais que serão considerados
    pontos = frase.count('.') - 3*ret
    return qtde + ret + pontos
#Q3
def inter(l1,l2):
    """Função que recebe duas listas de tamanho 3, e retorna uma lista que
    é formada intercalando os elementos das duas primeirasss.
    list,list -> list"""
    #Lista com zeros de tamanho 6
    fim = [0]*len(l1)*2
    #Inserimos os elementos de L1 nos índices pares
    fim[::2] = l1
    #Inserimos os elementos de L2 nos índices ímpares
    fim[1::2] = l2
    return fim

#Q4
def substitui(frase):
    """Retorne uma frase onde todos os caracteres de pontuação da frase
    inserida foram substituídos por espaços.
    str -> str""" 
    #Verificamos cada ocorrência e trocamos para espaço
    frase = frase.replace('...'," ")
    frase = frase.replace('-'," ")
    frase = frase.replace(','," ")
    frase = frase.replace(':'," ")
    frase = frase.replace(';'," ")
    frase = frase.replace('.'," ")
    frase = frase.replace('!'," ")
    frase = frase.replace('?'," ")
    return frase

#Q5
def contrario(frase):
    """Retorna a frase inserida, contendo as mesmas palavras, mas na
    ordem inversa, sem letras maiúsculas, e sem a pontuação.
    str -> str"""
    #Retiramos a pontuação e colocamos todas as letras minúsculas
    limpa = subs(frase).lower()
    #Criamos uma lista, usando como separação o espaço
    nova = limpa.split(" ")
    #Transformamos a lista em string, mas sendo percorrida de trás para frente
    return str.join(" ",nova[::-1])

#Q6
def piramide(n1,n2):
    """Função que constroi uma pirâmide de números inteiros,
    dados dois números inteiros como entrada.
    int,int -> list"""
    #Fazemos uma lista com os valores de n1 até n2
    lista = [numero for numero in range(n1,n2+1)]
    #Para a "segunda parte" da pirâmide, percorremos a nossa lista
    #ao contrário, excluindo o último termo
    #lista[-2::-1] --> percorrer os elementos de "lista" de trás para frente
    #começando com o penúltimo(-2) e indo até o primeiro
    lista_inverso = lista[-2::-1]
    #Depois basta concatenar as listas
    return lista + lista_inverso

#Q7
def colchao(lista,H,L):
    """Função que recebe A, B e C do colchão em centímetros,
    ordenadas da menor para a maior, e dois inteiros H e L, e retorna True
    se o colchão passa pelas portas e False em caso contrário.
    list,int,int -> bool"""
    maior = max(L,H)
    menor = min(L,H)
    #Ao menos duas dimensões do colchão devem ser menores que as da porta
    #Verificando o primeiro caso, no qual a segunda maior dimensão do
    #colchão é maior que a da porta
    if lista[1] > maior:
        return False
    else:
        #Temos que checar se ambas são menores
        if lista[0] > menor:
            return False
        else:
            return True
