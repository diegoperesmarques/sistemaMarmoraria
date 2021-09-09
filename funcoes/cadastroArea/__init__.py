import os
from funcoes import formatacoes


def cadastro():
    os.system('cls' if os.name == 'nt' else 'clear')
    formatacoes.titulo('Cadastrando área')

    # Validação largura
    while True:
        largura = input('Largura (m): ').strip().replace(',','.')
        if (float(largura)):
            break
        else:
            formatacoes.titulo('AVISO!')
            print('Você digitou um número inválido. Tente novamente!')

    # Validação altura
    while True:
        altura = input('Altura (m): ').strip().replace(',', '.')
        if (float(altura)):
            break
        else:
            formatacoes.titulo('AVISO!')
            print('Você digitou um número inválido. Tente novamente!')


    area = float(largura) * float(altura)

    formatacoes.titulo('Ficha')
    print(f'Área: {area:.3f}')
    input('Pressione enter pr continur')
