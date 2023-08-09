import sys

codigoPeca1str, numPeca1str, valorPeca1str = input().split()
codigoPeca2str, numPeca2str, valorPeca2str = input().split()

codigoPeca1 = int(codigoPeca1str)
numPeca1 = int(numPeca1str)
valorPeca1 = float(valorPeca1str)
codigoPeca2 = int(codigoPeca2str)
numPeca2 = int(numPeca2str)
valorPeca2 = float(valorPeca2str)

totalAPagar = (numPeca1*valorPeca1) + (numPeca2*valorPeca2)

print("VALOR A PAGAR: R$ {:.2f}".format(round(totalAPagar, 2)))
