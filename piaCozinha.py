import os
import validacoes
import formatacoes

def piaReta():
    os.system('cls' if os.name == 'nt' else 'clear')
    formatacoes.titulo('Calculando pia de cozinha (Reta)')
    largura = validacoes.numeroReal('Digite a largura (m): ')
    profundidade = validacoes.numeroReal('Digite a profundidade (m): ')
    area = float(largura) * float(profundidade)

    formatacoes.titulo('Resultado')
    print(f'Largura: {largura}')
    print(f'Profundidade: {profundidade}')

    input('Pressione enter para voltar ao Menu anterio')