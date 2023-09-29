num_idiomas = int(input())

idiomas = []
mensagens = []
for i in range(num_idiomas):
    idiomas.append(input())
    mensagens.append(input())

num_criancas = int(input())

criancas = []
idiomas_criancas = []
for i in range(num_criancas):
    criancas.append(input())
    idiomas_criancas.append(input())

for i in range(num_criancas):
    for j in range(num_idiomas):
        if idiomas_criancas[i] == idiomas[j]:
            print(criancas[i])
            print(mensagens[j])
            print()
            break
