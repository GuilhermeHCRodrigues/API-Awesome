import utils

moedaDolar = "USDBRL"
moedaEuro = "EURBRL"
moedaBitcoin = "BTCBRL"


# Menu principal
menu = """
=========================================
    Bem-vindo ao conversor de moedas!
=========================================

1 - Conversor de Dolar
2 - Conversor de Euro
3 - Conversor de Bitcoin
4 - Verificar cotação do Dólar, Euro e Bitcoin
0 - Sair

"""

escolha = int(input(menu + "Escolha uma das opções: "))


while escolha != 0:

    # =========================================
    # CONVERSOR DE DÓLAR
    # =========================================
    if escolha == 1:

        while True:

            print("Você deseja converter de:\n1) Dólar para Real\n2) Real para Dólar\n0) Voltar")

            opcao = int(input("Escolha uma das opções: "))

            if opcao == 1:
                valorDolar = float(
                    input("Informe o valor em dólar que deseja converter para Real: ")
                )

                utils.conversorMoeda(valorDolar, opcao, moedaDolar)

            elif opcao == 2:
                valorReal = float(
                    input("Informe o valor em real que deseja converter para Dólar: ")
                )

                utils.conversorMoeda(valorReal, opcao, moedaDolar)

            elif opcao == 0:
                break

            else:
                print("Opção inválida!")


    # =========================================
    # CONVERSOR DE EURO
    # =========================================
    elif escolha == 2:

        while True:

            print("Você deseja converter de:\n1) Euro para Real\n2) Real para Euro\n0) Voltar")

            opcao = int(input("Escolha uma das opções: "))

            if opcao == 1:
                valorEuro = float(
                    input("Informe o valor em Euro que deseja converter para Real: ")
                )

                utils.conversorMoeda(valorEuro, opcao,moedaEuro)

            elif opcao == 2:
                valorReal = float(
                    input("Informe o valor em real que deseja converter para Euro: ")
                )

                utils.conversorMoeda(valorReal, opcao, moedaEuro)

            elif opcao == 0:
                break

            else:
                print("Opção inválida!")


    # =========================================
    # CONVERSOR DE BITCOIN
    # =========================================
    elif escolha == 3:

        while True:

            print("Você deseja converter de:\n1) Bitcoin para Real\n2) Real para Bitcoin\n0) Voltar")

            opcao = int(input("Escolha uma das opções: "))

            if opcao == 1:
                valorBitcoin = float(
                    input("Informe o valor em Bitcoin que deseja converter para Real: ")
                )

                utils.conversorMoeda(valorBitcoin, opcao, moedaBitcoin)

            elif opcao == 2:
                valorReal = float(
                    input("Informe o valor em real que deseja converter para Bitcoin: ")
                )

                utils.conversorMoeda(valorReal, opcao, moedaBitcoin)

            elif opcao == 0:
                break

            else:
                print("Opção inválida!")


    # =========================================
    # COTAÇÕES
    # =========================================
    elif escolha == 4:

        utils.verificarCotacaoDinheiro()


    # =========================================
    # OPÇÃO INVÁLIDA
    # =========================================
    else:

        print("Opção inválida!")


    # =========================================
    # VOLTA PARA O MENU PRINCIPAL
    # =========================================

    escolha = int(input(menu + "Escolha uma das opções: "))


print("Encerrando o Sistema...")
