def Josephus(lista_pessoas, k, index, case):
    while True:
        if len(lista_pessoas) == 1:
            print(f'Case {case}: {lista_pessoas[0]}')
            return

        index = ((index + k) % len(lista_pessoas))

        lista_pessoas.pop(index)


index = 0


num_cases = int(input())

for case in range(num_cases):
    n, k = map(int, input().split())
    k = k - 1

    pessoas = []
    for i in range(1, n+1):
        pessoas.append(i)

    Josephus(pessoas, k, index, case + 1)
