(print("* Utilize apenas valores numéricos *\n"))

qnt = int(input("Quantas transações financeiras você realizou: "))
total = 0
i = 0

while qnt == 0 or qnt < 0:
    print("**** Quantidade inválida! ****")
    qnt = int(input("Quantas transações financeiras você realizou: "))

for valor in range(qnt):
    i = i + 1
    valor = float(input("Valor da transação {}: ".format(i)))
    total = total + valor
media = total / qnt
print("\nO valor total das transações foi de {} R$".format(total))
print("Uma média de R$ {} por transação".format(media))



