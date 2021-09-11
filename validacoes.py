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
            if (numeroDigitado == 1) or (numeroDigitado == 999):
                break
            formatacoes.titulo('INVÁLIDO!')
            print('Você digitou uma opção inválida. Tente novamente!')

        except Exception as erro:
            formatacoes.titulo('INVÁLIDO!')
            print('Você digitou uma opção inválida. Tente novamente!')
    
    return numeroDigitado
