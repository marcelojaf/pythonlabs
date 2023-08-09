import sys

valorA, valorB, valorC, valorD = map(int, sys.stdin.readline().split())

if (valorB > valorC) and (valorD > valorA) and (valorC + valorD) > (valorA + valorB) and (valorC > 0) and (valorD > 0) and (valorA % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
