lista_numeros = []
temp = 0
casos_teste = int(input())

for i in range(0, casos_teste):
    lista_numeros.append(int(input()))

for numero in lista_numeros:
    for i in range(1, numero):
        if numero % i == 0:
            temp += i
    if temp == numero:
        print(f"{numero} eh perfeito")
    else:
        print(f"{numero} nao eh perfeito")
    temp = 0
