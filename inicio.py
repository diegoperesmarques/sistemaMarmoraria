import os
import cadastroArea
import formatacoes
import validacoes
import piaCozinha


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    formatacoes.titulo('PAGINA INICIAL')
    print('Escolha o que você deseja fazer')
    print('1 - Calcular áreas')
    print('2 - Pia (Cozinha) - Reta')
    print('999 - Sair')
    opcao = validacoes.numeroMenuPrincipal()

    #Calculo da área
    if opcao == 1:
        cadastroArea.cadastro()

    if opcao == 2:
        piaCozinha.piaReta()

    if opcao == 999:
        break

formatacoes.titulo('Programa finalizado')
