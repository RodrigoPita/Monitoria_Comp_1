#Machine Teaching 3

#q1
def avalia(c, ce, cs, fv, fe, fs):
    '''Função que recebe número de vitórias,emaptes e saldo de gols
    de dois times e retorna qual deles está melhor colocado no campeonato.
    Se houver empate em ambos os paramêtros, retorna essa informação.
    int,int,int,int,int,int -> string'''
    #Verificamos qual time possui maior pontuação
    if c*3 + ce > 3*fv + fe:
        return 'Cormengo'
    elif c*3 + ce < 3*fv + fe:
        return 'Flaminthians'
    #Caso as pontuações sejam iguais, analisamos o saldo de gols
    else:
        if cs > fs:
            return 'Cormengo'
        elif cs < fs:
            return 'Flaminthians'
        #Caso os pontos e saldo de gols sejam iguais, então estão empatados
        else:
            return 'Empate'
    #return 'Empate'

#q2
def verificar(competidores,quantidade_papel,quantidade_folhas):
    '''Função que recebe três o número de competidores, a quantidade de
    papel total e a quantas folhas cada competidor terá direito.
    Retorna uma string que informa se a quantidade de papel é suficiente.
    int,int,int -> string'''
    #Calculamos a quantidade total necessária e comparamos com
    #a quantidade disponível
    if quantidade_papel >= competidores*quantidade_folhas:
        return 'Suficiente'
    else:
        return 'Insuficiente'
    
    