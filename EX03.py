opcao = ""
while opcao != "0":
    print("(1) - Verificar valor na tabela de Fibonnaci\n(0) - Encerrar programa\n")
    opcao = (input("Escolha uma opção: "))

    if opcao == "1":
        num = int(input("\nDigite um número inteiro: "))
        i = ""
        n1 = 0
        n2 = 1
        cont = 0
        while cont <= num:
            n3 = n1 + n2
            print(n3 , end=" ")
            n1 = n2
            n2 = n3
            cont = cont + 1
            if num == n3:
                i = "sim"
                break
        if i == "sim":
            print("\nAção bem sucedida!\n")
        else:
            print("\nA Ação falhou!\n")

    elif opcao > "1" or opcao < "0":
        print("\n *** Opção inválida... Tente novamente! ***\n")

print("\n ***** Programa encerrado! *****")

