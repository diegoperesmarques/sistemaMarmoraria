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

    perguntaTamEspelho = input('Espelho terá tamanho padrão [S/N]? ').strip().upper()[0]
    if perguntaTamEspelho == 'N':
        tamanhoEspelho = validacoes.numeroInteiro('Qual será o tamanho do espelho (cm)? ')
    else:
        tamanhoEspelho = 8

    tipoApoioPia = input('A pia é CHUMBADA ou APOIADA? ').upper().strip()
    if tipoApoioPia == "CHUMBADA":
        tamanhoApoioPia = 2
        tamanhoPadrao = input(f'Vai deixar com {tamanhoApoioPia} cm ou será outro valor [S/N]? ').upper().strip()[0]
        if tamanhoPadrao == "N":
            tamanhoApoioPia = validacoes.numeroInteiro('Qual o espaçamento da pia com a parede? ')
    else:
        tamanhoApoioPia = 0

    area = float(largura) * float(profundidade)

    formatacoes.titulo('Resultado')
    print(f'Largura: {largura}')
    print(f'Profundidade: {profundidade}')
    print(f'Área: {area}')
    print(f'Lados parede: {ladosParede}')
    print(f'Número de espelhos: {numeroEspelhos}')
    print(f'Tamanho do espalho: {tamanhoEspelho}')
    print(f'Quantidade de guanições: {quantidadeGuanicao}')
    print(f'Espaçamento pia da parede: {tamanhoApoioPia}')

    input('Pressione enter para voltar ao Menu anterior')