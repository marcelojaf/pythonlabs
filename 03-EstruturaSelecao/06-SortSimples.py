import sys

valorLidoA, valorLidoB, valorLidoC = map(int, sys.stdin.readline().split())

if (valorLidoA < valorLidoB) and (valorLidoA < valorLidoC) and (valorLidoB < valorLidoC):
    print(valorLidoA)
    print(valorLidoB)
    print(valorLidoC)
elif (valorLidoA < valorLidoB) and (valorLidoA < valorLidoC) and (valorLidoC < valorLidoB):
    print(valorLidoA)
    print(valorLidoC)
    print(valorLidoB)
elif (valorLidoB < valorLidoA) and (valorLidoB < valorLidoC) and (valorLidoA < valorLidoC):
    print(valorLidoB)
    print(valorLidoA)
    print(valorLidoC)
elif (valorLidoB < valorLidoA) and (valorLidoB < valorLidoC) and (valorLidoC < valorLidoA):
    print(valorLidoB)
    print(valorLidoC)
    print(valorLidoA)
elif (valorLidoC < valorLidoA) and (valorLidoC < valorLidoB) and (valorLidoA < valorLidoB):
    print(valorLidoC)
    print(valorLidoA)
    print(valorLidoB)
elif (valorLidoC < valorLidoA) and (valorLidoC < valorLidoB) and (valorLidoB < valorLidoA):
    print(valorLidoC)
    print(valorLidoB)
    print(valorLidoA)

print()
print(valorLidoA)
print(valorLidoB)
print(valorLidoC)
