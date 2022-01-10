#-------------------------------------------------------------------------------------------------------------------------#
## =========================================================================================================
## S E M A N A  3  -  T I P O S  D E  D A D O S ,  S T R I N G S ,  E S T R U T U R A  C O N D I C I O N A L
## =========================================================================================================

## =====================================
## Questão 1: Positivo, Negativo ou Zero
## =====================================

## Faça uma função chamada **PosNegZero** que determina se um número inteiro X passado como parâmetro é positivo, negativo ou zero.
## O valor de retorno da função deve ser uma dentre as strings “X e positivo”, “X e negativo” ou “X e zero”.

def PosNegZero(x:int)->str:
    '''Função que classifica um número (x) como sendo negativo, positivo ou zero'''
    if x > 0:
        return str(x) + ' e positivo'
    elif x < 0:
        return str(x) + ' e negativo'
    return str(x) + ' e zero'

## ==================
## Questão 2: Futebol
## ==================

## Questão OBI (Olimpíada Brasileira de Informática - 2012, Fase 1, Nível Júnior) - (Campeonato)
##
## Dois times, Cormengo e Flaminthians, participam de um campeonato de futebol, juntamente com outros times.
## Cada vitória conta três pontos, cada empate um ponto. Fica melhor classificado no campeonato um time que tenha mais pontos.
## Em caso de empate no número de pontos, fica melhor classificado o time que tiver maior saldo de gols.
## Se o número de pontos e o saldo de gols forem os mesmos para os dois times então os dois times estão empatados no campeonato.
## Faça uma função definida por classificacao(Cv, Ce, Cs, Fv, Fe, Fs). Dados os números de vitórias e empates, e os saldos de gols dos dois times,
## sua tarefa é determinar qual dos dois está melhor classificado, ou se eles estão empatados no campeonato.
##
## Entrada: Os parâmetros de entrada da função são seis números inteiros C, Ce, Cs, F v, F e e F s, que são, respectivamente,
## o número de vitórias do Cormengo, o número de empates do Cormengo, o saldo de gols do Cormengo, o número de vitórias do Flaminthians,
## o número de empates do Flaminthians e o saldo de gols do Flaminthians.
##
## Saída: A sua fun¸ção deve retornar a string 'Cormengo', se Cormengo estiver melhor classificado que Flaminthians ou a string 'Flaminthians',
## se Flaminthians estiver melhor classificado que Cormengo; e se os dois times estão empatados a função deve retornar 'Empate'.
##
## Exemplos:
## Entrada: 10,5,18,11,2,18
## Saída: ’Empate’
##
## Entrada: 10,5,18,11,1,18 ;
## Sapida: ’Cormengo’
##
## Entrada: 9,5,-1,10,2,10
## Saída: ’Flaminthians’

def classificacao(cv:int, ce:int, cs:int, fv:int, fe:int, fs:int)->str:
    '''Função que determinao qual time foi melhor posicionado de acordo com os números de vitórias (cv, fv),
    empates (ce, fe) e saldo de gol (cs, fs)'''
    if 3*cv + ce > 3*fv + fe:
        return 'Cormengo'
    elif 3*cv + ce < 3*fv + fe:
        return 'Flaminthians'
    else:
        if cs > fs:
            return 'Cormengo'
        elif cs < fs:
            return 'Flaminthians'
    return 'Empate'

## ==========================
## Questão 3: Aviões de Papel
## ==========================

## Questão OBI (Olimpíada Brasileira de Informática - 2009, Fase 1, Nível Júnior) - (Aviões de Papel)
##
## Para descontrair os alunos após as provas da OBI, a Diretora da escola organizou um campeonato de aviões de papel.
## Cada aluno participante receberá uma certa quantidade de folhas de um papel especial para fazer os seus modelos de aviões.
## A quantidade de folhas que cada aluno deverá receber ainda não foi determinada: ela será decidida pelos juízes do campeonato.
##
## A diretora convidou, para atuarem como juízes, engenheiros da Embraer, uma das mais bem sucedidas empresas brasileiras,
## que vende aviões com tecnologia brasileira no mundo todo. O campeonato está programado para começar logo após a prova da OBI,
## mas os juízes ainda não chegaram à escola. A diretora está aflita, pois comprou uma boa quantidade de folhas de papel especial,
## mas não sabe se a quantidade comprada vai ser suficiente. Considere, por exemplo, que a Diretora comprou 100 folhas de papel especial,
## e que há 33 competidores. Se os juízes decidirem que cada competidor tem direito a três folhas de papel,
## a quantidade comprada pela diretora é suficiente. Mas se os juízes decidirem que cada competidor tem direito a quatro folhas,
## a quantidade comprada pela diretora não seria suficiente. Você deve escrever uma função definida por avioes(competidores, papel_comprado, papel_competidor)
## que, dados o número de competidores, o número de folhas de papel especial compradas pela Diretora e o número de folhas que cada competidor deve receber,
## determine se o número de folhas comprado pela Diretora é suficiente.
##
## Entrada: Os parâmetros de entrada da função são três números inteiros representando respectivamente o número de competidores,
## a quantidade de folhas de papel especial compradas pela Diretora e a quantidade de folhas de papel especial que cada competidor deve receber.
##
## Saída: A sua função deve retornar 'Suficiente' se a quantidade de folhas compradas pela Diretora for suficiente, ou 'Insuficiente' caso contrário.
##
## Exemplos:
## Entrada: 10,100,10
## Saída: 'Suficiente'
##
## Entrada: 10,90,10
## Saída: 'Insuficiente'
##
## Entrada: 5,40,2
## Saída: 'Suficiente'

def avioes(c:int, p_compr:int, p_compet:int)->str:
    '''Função que dados o número dos competidores (c), a quantidade de folhas de papel compradas (p_compr)
    e a quantidade de folhas de papel por competidor (p_compet), calcula se o material é suficiente ou não'''
    if p_compr//c >= p_compet:
        return 'Suficiente'
    return 'Insuficiente'

#-------------------------------------------------------------------------------------------------------------------------#
