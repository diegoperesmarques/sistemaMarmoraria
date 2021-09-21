import formatacoes

def numeroReal(validando):
    while True:
        numeroResultado = input(f'{validando}').strip().replace(',','.')
        if (float(numeroResultado)):
            break
        else:
            formatacoes.titulo('AVISO!')
            print('Você digitou um número inválido. Tente novamente!')

    return numeroResultado


def numeroMenuPrincipal():
    while True:
        try:
            numeroDigitado = int(input('Digite a opção válida: '))
            if (numeroDigitado == 1) or (numeroDigitado == 2) or (numeroDigitado == 999):
                break
            formatacoes.titulo('AVISO!')
            print('Você digitou uma opção inválida. Tente novamente!')

        except Exception as erro:
            formatacoes.titulo('AVISO!')
            print('Você digitou uma opção inválida. Tente novamente!')
    
    return numeroDigitado


def numeroLadosParede(mensagem):
    while True:
        try:
            numeroDigitado = int(input(f'{mensagem}'))
            if (numeroDigitado == 1) or (numeroDigitado == 2) or (numeroDigitado == 3):
                break
            else:
                formatacoes.titulo(f'AVISO!')
                print('Somente são aceitos os valores 1, 2 ou 3') 
        except Exception as erro:
            formatacoes.titulo(f'AVISO!')
            print('Somente são aceitos os valores 1, 2 ou 3')
    
    return numeroDigitado


def numeroEspelhos(mensagem, ladosParede):
    while True:
        try:
            numeroDigitado = int(input(f'{mensagem}'))
            if (numeroDigitado <= ladosParede):
                break
            else:
                formatacoes.titulo(f'QUANTIDADE INVÁLIDA!')
                print(f'Deve ter {ladosParede} espelhos ou menos.')
        except Exception as erro:
            print(f'ERRO! Digite um númeor válido')
    
    return numeroDigitado


def numeroInteiro(mensagem):
    while True:
        try:
            numeroDigitado = int(input(f'{mensagem}'))
            if numeroDigitado > 0:
                break
        except Exception as erro:
            print(f'Digite um número inteiro válido! Tente novamente.')

    return numeroDigitado


def validacaoSN(mensagem):
    resultadoSN = input((f'{mensagem}')).upper().strip()[0]
    while resultadoSN not in 'SsNs':
        print('')
        formatacoes.titulo('AVISO!')
        print('Digite apenas S ou N')
        resultadoSN = input((f'{mensagem}')).upper().strip()[0]
    
    return resultadoSN


def apoiadaChumbada(mensagem):
    while True:
        valorDigitado = input(f'{mensagem}').upper().strip()
        if (valorDigitado == 'CHUMBADA') or (valorDigitado == 'APOIADA'):
            break
        else:
            formatacoes.titulo('AVISO!')
            print('Digite apenas CHUMBADA ou APOIADA')
        
    return valorDigitado
