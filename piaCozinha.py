import os
import validacoes
import formatacoes

def piaReta():
    os.system('cls' if os.name == 'nt' else 'clear')
    formatacoes.titulo('Calculando pia de cozinha (Reta)')
    largura = validacoes.numeroReal('Digite a largura (m): ')
    profundidade = validacoes.numeroReal('Digite a profundidade (m): ')
    ladosParede = validacoes.numeroLadosParede('Quantos lados tocam a parede? ')
    quantidadeGuanicao = 4 - ladosParede 
    numeroEspelhos = validacoes.numeroEspelhos('Quantos espelhos? ', ladosParede)

    perguntaTamEspelho = validacoes.validacaoSN('Espelho terá tamanho padrão [S/N]? ')
    if perguntaTamEspelho == 'N':
        tamanhoEspelho = validacoes.numeroInteiro('Qual será o tamanho do espelho (cm)? ')
    else:
        tamanhoEspelho = 8

    tipoApoioPia = input('A pia é CHUMBADA ou APOIADA? ').upper().strip()
    if tipoApoioPia == "CHUMBADA":
        tamanhoApoioPia = 2
        tamanhoPadrao = input(f'A pia vai entrar {tamanhoApoioPia} cm ou será outro valor [S/N]? ').upper().strip()[0]
        if tamanhoPadrao == "N":
            tamanhoApoioPia = validacoes.numeroInteiro('Qual o tamanho da entrada da pia na parede? ')
    else:
        tamanhoApoioPia = 0

    print('')
    valorCubaPadrao = 300
    temCuba = input('Tem cuba [S/N]? ').upper().strip()
    if temCuba == 'S':
        print('Informar ao cliente que tem que trazer a cuba para medição')
    else:
        compraCuba = input(f'Gostaria de comprar nossa cuba, custa R$ {valorCubaPadrao} [S/N]? ').upper().strip()
        listaCubas = ['', 'Pequena', 'Média', 'Grande']
        if compraCuba == 'S':
            print(f''' 
                Escolha o tipo de cuba abaixo:
                1 - Pequena
                2 - Média
                3 - Grande
            ''')
            tipoDeCuba = listaCubas[validacoes.numeroInteiro('Digite o tipo: ')]
        else:
            print('Informar ao cliente que tem que trazer a cuba para medição')

    area = float(largura) * float(profundidade)

    formatacoes.titulo('Resultado')
    print(f'Largura: {largura}')
    print(f'Profundidade: {profundidade}')
    print(f'Área: {area}')
    print(f'Lados parede: {ladosParede}')

    print('')
    print(f'Número de espelhos: {numeroEspelhos}')
    print(f'Tamanho do espelho: {tamanhoEspelho}')
    print(f'Quantidade de guanições: {quantidadeGuanicao}')

    print('')
    print(f'Espaçamento pia da parede: {tamanhoApoioPia}')


    if temCuba == 'S':
        print('O clinte tem cuba')
    elif temCuba == 'N':
        if compraCuba == 'S':
            print(f'O cliente vai comprar a cuba {tipoDeCuba}')
        else:
            print('O cliente ainda vai realizar a compra da cuba')

    input('Pressione enter para voltar ao Menu anterior')