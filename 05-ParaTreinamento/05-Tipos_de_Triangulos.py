lados = list(map(float, input().split()))

lados.sort(reverse=True)
ladoA, ladoB, ladoC = lados

if ladoA >= ladoB+ladoC:
    print('NAO FORMA TRIANGULO')
else:
    quadrado_catetos = ladoB ** 2 + ladoC ** 2
    quadrado_maior = ladoA ** 2

    if quadrado_maior == quadrado_catetos:
        print('TRIANGULO RETANGULO')
    elif quadrado_maior > quadrado_catetos:
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')

    if ladoA == ladoB == ladoC:
        print('TRIANGULO EQUILATERO')
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print('TRIANGULO ISOSCELES')
