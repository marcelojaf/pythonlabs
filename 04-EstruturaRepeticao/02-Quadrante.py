import sys

while True:
    valorX, valorY = map(int, sys.stdin.readline().split())

    if (valorX == 0) or (valorY == 0):
        break
    else:
        if (valorX > 0) and (valorY > 0):
            print("primeiro")
        elif (valorX > 0) and (valorY < 0):
            print("quarto")
        elif (valorX < 0) and (valorY > 0):
            print("segundo")
        elif (valorX < 0) and (valorY < 0):
            print("terceiro")
