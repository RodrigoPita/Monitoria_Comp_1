#MT 4

#Q1
def concatenacao(a,b):
    '''Recebe duas strings, a e b, retornando a string abba.
    str -> str'''
    return a + b*2 + a

#Q2
def substitui(s, x, i):
    '''Recebe uma string s, um caractere x e um inteiro i entre 0
    e o tamanho de s. Retorna a string s, com o caractere da posição i
    substituído por x.
    str, str, int -> str'''
    #Caso você interprete que um caractere pode ser algo além de um string,
    #então deve utilizar str(x)
    return s[:i] + x + s[i+1:]

#Q3
def recursiva(string):
    '''Recebe um string e retorna a própria string no meio dela mesma.
    str -> str'''
    tam = len(string) #Primeiro criamos uma var com o tamanho da string
    #Agora, fatiamos a string até a metade, ou seja, tam//2
    #Usamos divisão inteira para cuidar do caso de número ímpares
    #Concatenamos isso com a string inicial, e depois com a string inicial
    #da metade para o final
    return string[:tam//2] + string + string[tam//2:]

#OBS: De forma geral, tendo uma string s, podemos reescrevê-la da seguinte
#forma: s[:len(s)//2] + s[len(s)//2:]. Tente demonstrar isso.

#Q4
def hashtag(string):
    '''Recebe uma string e insira o caractere "#" no início, no meio
    e no final dela.
    str -> str'''
    tam = len(string)
    #Mesmo raciocínio da questão anterior
    return '#' + string[:tam//2] + '#' + string[tam//2:] + '#'

#Q5
def diff_datas(dat1,dat2):
    '''Recebe duas datas no formato "DD/MM/AAAA", sendo a segunda maior
    que a primeira e retorna o total de dias passados entre as datas.
    A função considera que todos os meses tem 30 dias e o ano tem 365.
    str,str -> int'''
    #Vamos criar variáveis com a diferença entre os valores de dia,mês e ano
    ano = int(dat2[-4:]) - int(dat1[-4:])  
    mes = int(dat2[-7:-5]) - int(dat1[-7:-5])
    dia = int(dat2[:2]) - int(dat1[:2])
    #Agora basta somar tudo, transformando para dias, ou seja,
    #temos que multiplicar o valor de ano por 365 e o de mês por 30.
    #Observe que a condição do enunciado de que dat2 > dat1 nos garante
    #que o resultado abaixo será positivo.
    return 365*ano + 30*mes + dia

#OBS: Se não houvesse a restrição que dat2 > dat1, algo teria que mudar
#na nossa função? Se sim, o quê? 

#Q6
def filtra_pares(tupla):
    '''Recebe uma tupla com quatro elementos inteiros, e retorna
    uma nova tupla contendo apenas os elementos pares da original,
    na mesma ordem em que se encontravam.
    tuple -> tuple'''
    #Criamos uma tupla vazia para a resposta
    final = ()
     #Verificamos se o valor em cada posição é par, e caso seja,
     #concatenamos a tupla unitária composta por ele com a nossa vazia.
     #Fazemos isso para todas os valores da tupla recebida.
    if tupla[0] % 2 == 0:
        final += (tupla[0],)  
    if tupla[1] % 2 == 0:
        final += (tupla[1],)
    if tupla[2] % 2 == 0:
        final += (tupla[2],)
    if tupla[3] % 2 == 0:
        final += (tupla[3],)
     #Agora, basta retornar a tupla que concatenamos.
    return final

#Q6 - Extra
def filtra_pares1(tup):
    '''Recebe uma tupla com quatro elementos inteiros, e retorna
    uma nova tupla contendo apenas os elementos pares da original,
    na mesma ordem em que se encontravam.
    tuple -> tuple'''
    #Criamos uma função que avalia se um número é par ou não, retornando
    #True e False respectivamente.
    def par(x):
        '''Recebe um número e retorna True caso seja par, False caso não.
        float -> bool'''
        return x % 2 == 0
    #Desafio
    return tuple(filter(par,tup))

#OBS: É um desafio bem difícil, então não se preocupe em entender 100%
#esse código agora, está aqui apenas para instigar curiosidade e mostrar
#algo novo. Se ficar interessado, tente investigar a função filter e pense
#porque essa abordagem funciona. Não hesite em contactar o monitor caso
#queira perguntar mais sobre.

#Q7
def colisao(tup1,tup2):
    '''Recebe duas tuplas com quatro valores inteiros cada uma,
    representando as coordenadas do primeiro retângulo e do segundo.
    Retorna se os retângulos colidem ou não.
    tuple,tuple -> bool'''
    #A melhor forma de entender essa questão é fazer um desenho
    #e investigar os casos em que NÃO ocorre uma colisão.
    #Filtrados esses, todos os outros são colisões.
    if tup2[0] > tup1[2] or tup2[2] < tup1[0] or tup1[3] < tup2[1] or tup1[1] > tup2[3]:
        return False
    else:
        return True

#Pense nos seguinte casos:
    #Um retângulo à direita do outro, independente da altura
    #Um retângulo acima do outro, independente da posição horizontal

#Para cada um desses casos, há um caso análogo (esquerda e abaixo), tente
#pensar em como os vértices devem estar posicionados para que isso ocorra.
    