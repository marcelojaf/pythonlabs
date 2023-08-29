

while True:
    num_case = int(input())

    if (num_case < 1 or num_case > 100):
        print(
            'Número inválido. Informe um número maior ou igual a 1 e menor ou igual a 100')
    else:
        for case in range(num_case):
            num_casas_tabuleiro = int(input())
            qtde_graos_trigo = 1
            for casa in range(num_casas_tabuleiro):
                qtde_graos_trigo = qtde_graos_trigo * 2

            total_trigo_kg = (qtde_graos_trigo / 12) // 1000

            print(f'{int(total_trigo_kg)} kg')
        break
