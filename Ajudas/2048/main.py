from Funções_auxiliares import *

def main():
    print(
        f'Ao final de cada rodada, pressione:',
        f'- "Enter" para continuar a jogar;',
        f'- "1" para ver o menu;',
        f'- "2" para reiniciar;',
        f'- "3" para sair;',
        sep='\n'
        )
    tamanho_tabuleiro = int(input('Insira o tamanho do tabuleiro: '))
    valor_max = int(input('Insira o valor máximo (sendo uma potência de 2): '))
    A = cria_tabuleiro(tamanho_tabuleiro)
    visualiza(A)
    condicao = True
    ganhou = False
    while condicao:
        jogada = pega_jogada()
        A = move_tabuleiro(A, jogada)
        substitui(A)
        visualiza(A)
        teste = input('')
        S = status(A, valor_max)
        if S == 1 and ganhou == False:
            ganhou = True
            print('Parabéns, você ganhou!!!')
            continua = input('Insira S/N caso queira ou não continuar a jogar: ')
            if continua.upper() == 'N':
                break
        if teste == '1':
            menu()
        elif teste == '2':
            tamanho_tabuleiro = int(input('Insira o tamanho do tabuleiro: '))
            valor_max = int(input('Insira o valor máximo (sendo uma potência de 2): '))
            A = cria_tabuleiro(tamanho_tabuleiro)
            visualiza(A)
        elif teste == '3':
            break
main()
            
