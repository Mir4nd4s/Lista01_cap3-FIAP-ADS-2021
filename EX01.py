opcao = ""
total = 0
i = 0

while opcao != "0":
    print("(1) - Informar consumo de alimentos ingeridos")
    print("(0) - Encerrar o programa")
    opcao = input("\nDigite o número da opção desejada: ")

    if opcao == "1":
        x = ""
        qnt = int(input("Informe a quantidade de alimentos que você ingeriu: "))
        for cal in range(qnt):
            i = i + 1
            cal = float(input("Valor das calorias do alimento {}: ".format(i)))
            total = total + cal
        print("\nO valor total consumido foi de {} calorias\n".format(total))
    elif opcao > "1" or opcao < "0":
        print("\n *** Opção inválida... Tente novamente! ***\n")

print("\n ***** Programa encerrado! *****")