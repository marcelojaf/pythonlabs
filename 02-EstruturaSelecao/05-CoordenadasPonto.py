import sys

valorX, valorY = map(float, sys.stdin.readline().split())

if (valorX > 0) and (valorY > 0):
    print("Q1")
elif (valorX > 0) and (valorY < 0):
    print("Q4")
elif (valorX < 0) and (valorY > 0):
    print("Q2")
elif (valorX < 0) and (valorY < 0):
    print("Q3")
elif (valorX == 0) and ((valorY > 0) or (valorY < 0)):
    print("Eixo Y")
elif ((valorX > 0) or (valorX < 0)) and (valorY == 0):
    print("Eixo X")
elif (valorX == 0) and (valorY == 0):
    print("Origem")
