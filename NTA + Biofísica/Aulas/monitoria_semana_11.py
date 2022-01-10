# Questão 1
def notas(s):
    '''A partir de uma string com notas (A, B, C, D, E, F, G)
    seguidas de suas posições (1, 2, 3, 4, 5),
    encontra as frequências relativas à cada nota na posição dada 
    str --> list'''
    freq_retorno = []
    D = {}
    frequencias_centrais = [440, 494, 262, 294, 330, 349, 392]

    #range para abranger todas as notas musicais
    for i in range(7):
        #range para abranger as posições posiveis
        for j in range(5):
            # chr(65) -> 'A' na tabela ASCII
            D[chr(65+i)+f'{j+1}'] = frequencias_centrais[i]*2**(j-2)
    #range para acessar a string s de dois em dois caracteres
    for i in range(0, len(s), 2):
        freq_retorno.append(D[s[i:i+2]])
    return freq_retorno
        
# Questão 2
def n_elementos(entrada):
    '''Calcula o número de elementos distintos de uma dada entrada
    str/list/tuple --> int'''
    return len(set(entrada))

# Questão 3
def redes(users_f, users_i, users_w):
    '''A partir de 3 conjuntos de usuários de diferentes redes sociais, calcula:
    o número total de habitantes usuários de alguma dessas redes;
    a porcentagem de usuários em relação ao total de habitantes;
    o número de usuários comuns entre as três redes;
    o número de usuários comuns entre a rede f e i, mas que não pertencem a rede w
    set, set, set --> tuple'''
    tot_hab = 30000
    n_users = len(users_f | users_i | users_w)
    porcent_users = ((len(users_f) +
                      len(users_i) +
                      len(users_w)) * 100)/tot_hab
    n_users_fiw = len(users_f & users_i & users_w)
    n_users_fi = len((users_f & users_i) - users_w)
    return (n_users,
            porcent_users,
            n_users_fiw,
            n_users_fi)

# Questão 4
def cursos(cod_civil, cod_eletro):
    '''A partir das listas de códigos das disciplinas do cursos de civil e eletrônica,
    calcula a porcentagem de disciplinas em comum aos dois cursos,
    em relação ao total de disciplinas em eletrônica e também,
    o total de disciplinas distintas entre os dois cursos
    list, list --> tuple'''
    civil, eletro = set(cod_civil), set(cod_eletro)
    disciplinas = civil | eletro
    porcentagem = (len(civil & eletro)*100)/len(cod_eletro)
    total = len(disciplinas)
    return porcentagem, total

# Questão 5
def resist(cor1, cor2, cor3):
    '''Recebe 3 cores, cada referente a uma faixa presente num resistor
    e calcula o valor da resistência de acordo com as cores
    str, str, str --> int'''
    D = {'Preto': 0,
         'Marrom': 1,
         'Vermelho': 2,
         'Laranja': 3,
         'Amarelo': 4}
    if cor1 not in D or cor2 not in D or cor3 not in D:
        print('Código não encontrado')
        R = 0
    else:
        R = ((D[cor1])*10 + (D[cor2]))*(10**(D[cor3]))
    return R
