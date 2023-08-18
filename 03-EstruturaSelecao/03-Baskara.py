import math
import sys

valorA, valorB, valorC = map(float, sys.stdin.readline().split())

delta = (valorB ** 2) - (4 * valorA * valorC)

if delta < 0 or valorA == 0:
    print("Impossivel calcular")
else:
    resultado = (-valorB + math.sqrt(delta)) / (2 * valorA)
    print(f"R1 = {resultado:.5f}")
    resultado = (-valorB - math.sqrt(delta)) / (2 * valorA)
    print(f"R2 = {resultado:.5f}")
