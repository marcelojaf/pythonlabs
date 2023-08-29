nota1, nota2, nota3, nota4 = input().split()
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

peso1 = 2
peso2 = 3
peso3 = 4
peso4 = 1

soma_das_medias = nota1*peso1 + nota2*peso2 + nota3*peso3 + nota4*peso4
soma_dos_pesos = peso1 + peso2 + peso3 + peso4

media = soma_das_medias / soma_dos_pesos

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
