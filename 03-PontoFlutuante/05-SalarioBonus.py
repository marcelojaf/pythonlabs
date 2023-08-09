nomeVendedor = input()
salarioFixo = float(input())
totalVendas = float(input())

totalAReceber = salarioFixo + (totalVendas * 0.15)

print("TOTAL = R$ {:.2f}".format(round(totalAReceber, 2)))
