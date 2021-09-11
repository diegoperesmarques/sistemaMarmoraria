import os
import formatacoes
import validacoes

def cadastro():
    os.system('cls' if os.name == 'nt' else 'clear')
    formatacoes.titulo('Cadastrando área')

    quantidade = int(input('Quantas áreas quer calcular? '))
    listaInfo = list()
    infoLAA = dict()
    totalArea = 0
    tamanhoChapa = 5.04

    if quantidade <= 0:
        input('Pressiona enter voltar ao menu anterior')
    else:
        for i in range(0, quantidade):
            print('')
            print(f'Área número {i+1}')
            infoLAA['largura'] = float(validacoes.numeroReal('Largura (m): '))
            infoLAA['altura'] = float(validacoes.numeroReal('Altura (m): '))
            infoLAA['area'] = infoLAA['largura'] * infoLAA['altura']
            listaInfo.append(infoLAA.copy())
    
        #Exibição do resultado das áreas
        formatacoes.titulo('Lisagem das áreas')

        #Lista das áreas com largura e altura
        for i in range(0, len(listaInfo)):
            ordemArea = i + 1
            print(f'#00{ordemArea}')
            print(f'Área: {listaInfo[i]["area"]:.3f} || ', end='')
            print(f'L: {listaInfo[i]["largura"]} x ', end='')
            print(f'A: {listaInfo[i]["altura"]}')
            print('')

        #Soma com total da área
        for i in range(0, len(listaInfo)):
            totalArea = totalArea + listaInfo[i]['area']

        formatacoes.titulo('Totalizador')
        print(f'Total da área: {totalArea:.2f}')
        print(f'Total de chapas: {totalArea / tamanhoChapa}')

        input('Pressione enter para continuar')
