lista_quantidade_lesmas = []
velocidades_lesmas = []
lista_velocidades_lesmas = []
while True:
    try:
        # ler quantidade de lesmas do grupo
        quantidade_lesmas = int(input())
        if (quantidade_lesmas >= 1 and quantidade_lesmas <= 500):
            # se a quantidade é valida, inclui na lista de quantidades
            lista_quantidade_lesmas.append(quantidade_lesmas)

            # ler as velocidades de cada lesma em string
            velocidades_str = input().split(" ", quantidade_lesmas)

            # converter as velocidades em inteiro
            velocidades_lesmas = [int(x) for x in velocidades_str]
            lista_velocidades_lesmas.append(velocidades_lesmas)
        else:
            break
    except:
        break


for grupo_lesmas in lista_velocidades_lesmas:
    velocidade_lesma_mais_veloz = 0
    index = len(lista_velocidades_lesmas)

    for velocidade in grupo_lesmas:
        if (velocidade > velocidade_lesma_mais_veloz):
            velocidade_lesma_mais_veloz = velocidade

    if (velocidade_lesma_mais_veloz < 10):
        print(1)
    elif (velocidade_lesma_mais_veloz >= 10 and velocidade_lesma_mais_veloz < 20):
        print(2)
    else:
        print(3)
