num_candidatos = int(input())

votacao = sorted(list(map(int, input().split())))

votacao.reverse()
total_votos = sum(votacao)

percentual = [votacao[i] / total_votos for i in range(num_candidatos)]

if percentual[0] >= 0.45:
    print(1)
elif percentual[0] >= 0.40:
    percentual_maior_que_dez_porcento = False
    for i in range(1, num_candidatos):
        if percentual[0] - percentual[i] > 0.10:
            percentual_maior_que_dez_porcento = True
        else:
            percentual_maior_que_dez_porcento = False
            break
    if percentual_maior_que_dez_porcento:
        print(1)
    else:
        print(2)
else:
    print(2)
