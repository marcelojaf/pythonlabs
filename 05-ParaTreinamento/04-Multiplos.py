valorA, valorB = map(int, input().split())

if (valorA >= valorB):
    modulo = valorA % valorB
else:
    modulo = valorB % valorA

if modulo == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
