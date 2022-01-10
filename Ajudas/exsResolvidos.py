'''
def tarefa(L, n):
    L1 = []
    if len(L1) < n:
        L1.append(L.pop(0))
        return tarefaX(L, n, L1)
    else:
        L2 = L1
        return L2, L

def tarefaX(L, n, L1):
    if len(L1) < n:
        L1.append(L.pop(0))
        return tarefaX(L, n, L1)
    else:
        L2 = L1
        L1 = []
        return L2, L

def listas(lista, numero):
    inicio = lista[0:numero]
    final = lista[numero:-1]
    list.append(final, lista[-1])
    return inicio, final

def tarefa(x:str, y:str):
    L = [] ##lista para retorno
    k = 0  ##variavel para contador
    while k < len(x):
        candidato = x[k:k+len(y)] ##string a ser comparada com y
        if y == candidato:
            L.append(k)
            k += len(y) ##impedindo a sobreposicao
            continue
        k+=1
    return L

a = tarefa('1;2;3;4;5', ';')
b = tarefa('ABC,ABC', 'AB')
c = tarefa('BAAAC', 'AA')

print(a, b, c)


def tarefa(x:tuple, y:tuple, z:tuple):
    w = [] ##lista auxiliar para criar a tupla para retorno
    k = 0 ##variavel para contador
    while k < len(x):
        w.append(x[k])
        w.append(y[k])
        w.append(z[k])
        k+=1
    return tuple(w)

tarefa(("A Origem", "Laranja Mecanica", "Bastardos Inglorios"),
       ("Christopher Nolan", "Stanley Kubrick", "Quentin Tarantino"),
       (2010, 1971, 2009))

def tarefa(x:str, y:tuple):
    L = [] ##lista para retorno
    k = 0 ##variavel para contador
    while k < len(y):
        if x.upper() == y[k][1].upper():
            L.append(y[k][0])
        k+=1
    return L


def tarefa(L:list):
    D = {} ##dicionario de retorno
    tarefaX(L, D) ##chama a funcao auxiliar para recursao
    return D

def tarefaX(L:list, D:dict):
    ##impede a tentativa de acessar algum elemento se a lista estiver vazia
    if len(L) > 0:
        ##adiciona o primeiro elemento da lista todo minúsculo para a chave
        ##e todo maiúsculo para o valor
        D[L[0].lower()] = L[0].upper()
        L.remove(L[0]) ##remove o primeiro elemento da lista
        tarefaX(L, D) ##da continuidade a recursao
    return D


def tarefa(L:list):
    D = {} ##dicionario para guardas as frequencias
    tarefaX(L, D) ##chama a funcao auxiliar para recursao
    return D

def tarefaX(L:list, D:dict):
    if len(L) > 0:
        if L[0] in D:
            D[L[0]] += 1 ##incrementa a frequencia do da chave L[0]
        else:
            D[L[0]] = 1 ##adiciona uma chave nova ao dicionario
        L.remove(L[0])
        tarefaX(L, D)
    return D


def tarefa(D:dict, x:str):
    Dx = {} ##dicionario para retorno
    tarefaX(D, x, Dx) ##chama a funcao auxiliar para recursao
    return Dx

def tarefaX(D:dict, x:str, Dx:dict):
    L = list(D) ##lista para acessar as chaves do dicionario em ordem
    if len(L) > 0:
        ##comapara se a primeira chave do dicionario tem classificacao x
        if D[L[0]] == x:
            Dx[L[0]] = x ##adiciona a chave com o valor no dicionario de retorno
        del D[L[0]] ##apaga a chave e o valor do dicionario original
        return tarefaX(D, x, Dx)
    return Dx


from random import randint
def tarefa(n:int):
    L = [4, 6, 8, 12, 20]
    dado1 = -1 ##inicializa o dado1 com um valor qualquer
    dado2 = -2 ##inicializa o dado2 com um valor qualquer diferente do dado1
    count = 1 ##contador de vezes que os dados foram jogados
    while dado1 != dado2:
        dado1, dado2 = randint(1, L[n-1]), randint(1, L[n-1])
        count += 1
    return("Os dados foram jogados {:d} vezes".format(count))


def tarefa(L:list):
    D = {} ##dicionario para guardas as frequencias
    while len(L) > 0:
        if L[0] in D:
            D[L[0]] += 1 ##incrementa a frequencia do da chave L[0]
        else:
            D[L[0]] = 1 ##adiciona uma chave nova ao dicionario
        L.remove(L[0])
    return D


def repetidos(L:list):
    k = 1 ##variavel para iterar pela lista
    count = 0 ##contador de repetidos
    while k < len(L):
        if L[k] == L[k-1]:
            count += 1
        k += 1
    return count



def faixa(s:str):
    s = s.replace(' ', '') ##tira os espacos em branco da string
    if s == '':
        ##caso de ser uma string de espacos em branco ou vazia
        return ''
    k = 0 ##variavel para iterar pela lista
    count = 0 ##contador de letras na faixa
    L = sorted(s) ##lista com caracteres em ordem alfabetica
    x = L[k] ##primeira letra da faixa atual
    result = '' ##string de retorno
    while k < len(s):
        if k+1 == len(s):
            if count > 0:
                ##se count for mair que 0, a letra final != letra inicial
                result = result + x + ':' + L[k]
            else:
                ##senao letra final == letra inicial
                result = result + L[k] + ':' + L[k]
            break
        if ord(L[k])+1 == ord(L[k+1]):
            ##se as letras L[k] e L[k+1] forem consecutivas, incrementamos count
            count += 1

        elif ord(L[k]) == ord(L[k+1]):
            ##se as letras L[k] e L[k+1] forem iguais, pulamos uma iteracao
            k += 1
            continue
        else:
            ##senao fechamos a faixa atual
            result = result + x + ':' + chr(ord(x)+count) + ', '
            count = 0 ##zeramos o count
            x = L[k+1] ##atualizamos a primeira letra da faixa
        k += 1                
    return result

print('1) ' + faixa('aha') + '\n' + '2) '
      + faixa('xyzzy') + '\n' + '3) '
      + faixa('quick brown fox jumps over the lazy dog') + '\n' + '4) '
      + faixa('fbxeac') + '\n' + '5) '
      + faixa(' x ') + '\n' + '6) '
      + faixa('b z a x c y') + '\n' + '7) '
      + faixa('bdfhjlnprtvxz') + '\n' + '8) '
      + faixa(' ') + '\n' + '9) '
      + faixa('az def'))


def itera(L:list):
    k = 0 ##variavel para iterar pela lista
    n = 0 ##variavel de retorno
    while k < len(L):
        if(L[k] & 1):
            ##se L[k] for impar
            n += 1
        else:
            ##se L[k] for par
            n -= 1
        k += 1
    return n


def rna(m:str):
    k = 0 ##variavel para iterar pela string
    nome = '' ##string de retorno
    ##dicionario com as trincas
    aminoacido = {'UUU': 'Phe', 'CUU':'Leu',
                  'UUA':'Leu', 'AAG':'Lisina',
                  'UCU':'Ser', 'UAU':'Tyr', 'CAA':'Gln'}
    while k < len(m):
        nome += aminoacido[m[k]+m[k+1]+m[k+2]]
        k += 3
        if k < len(m):
            nome += '-'
    return nome



def multiplos(num:int, tamanho:int):
    L = [] ##lista de retorno
    k = 0 ##variavel para iterar pela range
    while k in range(0, tamanho):
        L.append((k+1)*num)
        k += 1
    return L

def multiplosR(num:int, tamanho:int):
    L = [] ##lista de retorno
    k = 0 ##variavel para condicao da recursao
    if k in range(0, tamanho):
        multiplosX(num, tamanho, k, L)
    return L

def multiplosX(num:int, tamanho:int, k:int, L:list):
    if k not in range(0, tamanho):
        return L
    L.append((k+1)*num)
    k += 1
    return multiplosX(num, tamanho, k, L)



def fatorial(n:float):
    if n == 1.0:
        return 1.0
    return fatorial(n-1)*n

def seno(x:float, n:float):
    i = 0 ##variavel para iterar a soma
    soma = 0 ##variavel de retorno
    for i in range(0, n):
        soma += (((-1)**i)/fatorial(2*i+1))*x**(2*i+1)
    return soma

'''
