numero = int(input())

for i in range(1, numero//2 + 1):
    if numero % i == 0:
        print(i)
print(numero)
