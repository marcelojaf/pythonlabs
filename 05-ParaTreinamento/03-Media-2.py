notas = input()
notas = list(map(float, notas.split()))
pesos = [2, 3, 4, 1]

notas_ponderadas = [nota*pesos[i] for i, nota in enumerate(notas)]
media = sum(notas_ponderadas)/sum(pesos)

print(f'Media: {media:.1f}')

if (media >= 7):
    print('Aluno aprovado.')
elif (media < 5):
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame:.1f}')
    media_final = (media + nota_exame) / 2
    if (media_final >= 5):
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media_final:.1f}')
