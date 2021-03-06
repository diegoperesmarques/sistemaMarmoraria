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

    tipoApoioPia = validacoes.apoiadaChumbada('A pia é CHUMBADA ou APOIADA? ')
    if tipoApoioPia == "CHUMBADA":
        tamanhoApoioPia = 2
        tamanhoPadrao = validacoes.validacaoSN(f'A pia vai entrar {tamanhoApoioPia} cm ou será outro valor [S/N]? ')
        if tamanhoPadrao == "N":
            tamanhoApoioPia = validacoes.numeroInteiro('Qual o tamanho da entrada da pia na parede? ')
    else:
        tamanhoApoioPia = 0

    print('')
    valorCubaPadrao = 300
    temCuba = validacoes.validacaoSN('Tem cuba [S/N]? ')
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


    temPontoAgua = validacoes.validacaoSN('Já tem ponto de água [S/N]? ')
    pontoAguaCentralizado = distanciaPontoAgua = distanciaCuba = 0
    if temPontoAgua == 'S':
        pontoAguaCentralizado = validacoes.validacaoSN('Cuba pode ser centralizada com o ponto de água? [S/N] ')
        if pontoAguaCentralizado == 'S':
            distanciaPontoAgua = validacoes.numeroInteiro('Qual a distância da extremidade até o ponto? ')
            distanciaCuba = distanciaPontoAgua
        else:
            distanciaPontoAgua = validacoes.numeroInteiro('Qual a distância da extermidade até o ponto de água? ')
            distanciaCuba = validacoes.numeroInteiro('Qual a distância da extermidade até a cuba? ')
    else: 
        print('Informar que é necessário saber a distância do ponto de água para o orçamento')








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

    print('')
    if temPontoAgua == 'S':
        if pontoAguaCentralizado == 'S':
            print('O ponto de águe é centralizado com a cuba')
            print(f'Na distância de {distanciaPontoAgua} cm')
        else:
            print('O ponto de água não é centralizado com a cuba!')
            print(f'Ponto de água: {distanciaPontoAgua} cm')
            print(f'Cuba: {distanciaCuba} cm')
    else:
        print('O cliente não tem ponto de água')


    input('Pressione enter para voltar ao Menu anterior')