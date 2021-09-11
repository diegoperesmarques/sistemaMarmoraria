import os
import cadastroArea
import formatacoes


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    formatacoes.titulo('PAGINA INICIAL')
    print('Escolha o que você deseja fazer')
    print('1 - Cadastrar area')
    print('2 - Pia (Cozinha)')
    print('999 - Sair')
    opcao = ' '

    #Validação da opção digitada
    while True:
        try:
            opcao = int(input('Digite a opção válida: '))
            if (opcao == 1) or (opcao == 999):
                break
            formatacoes.titulo('INVÁLIDO!')
            print('Você digitou uma opção inválida. Tente novamente!')

        except Exception as erro:
            formatacoes.titulo('INVÁLIDO!')
            print('Você digitou uma opção inválida. Tente novamente!')

    #Cadastro da cotacao
    if opcao == 1:
        cadastroArea.cadastro()

    if opcao == 999:
        break

formatacoes.titulo('Programa finalizado')
