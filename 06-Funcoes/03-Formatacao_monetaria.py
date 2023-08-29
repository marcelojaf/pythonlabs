def Insere_Separacao_Milhar(numero_inteiro_string):
    tamanho_numero = len(numero_inteiro_string)

    qtde_milhar = tamanho_numero // 3
    numero_formatado_com_divisao_milhar = ''
    index = tamanho_numero

    for i in range(qtde_milhar + 1):
        # print(f'Inicio do FOR. Index: {index}')
        if (tamanho_numero == index):
            if (index >= 3):
                numero_formatado_com_divisao_milhar = numero_inteiro_string[index - 3: index]
            else:
                numero_formatado_com_divisao_milhar = numero_inteiro_string
        elif (index < 3):
            # print(f'Index é menor que 3: {index}')
            # print(f'Substring: {numero_inteiro_string[:index]}')
            numero_formatado_com_divisao_milhar = numero_inteiro_string[:index] + \
                ',' + numero_formatado_com_divisao_milhar
        else:
            numero_formatado_com_divisao_milhar = numero_inteiro_string[index -
                                                                        3: index] + ',' + numero_formatado_com_divisao_milhar
        # print(f'Numero formatado atual: {numero_formatado_com_divisao_milhar}')
        # print(f'Index atual: {index}')
        # print(f'Novo index: {index - 3}')
        # input()
        index = index - 3
        # print(f'INDEX ATUALIZADO: {index}')
        if index <= 0:
            break

    return (f'${numero_formatado_com_divisao_milhar}')


def Insere_centavos(total_centavos):
    if (total_centavos < 10):
        return (f'.0{total_centavos}')
    else:
        return (f'.{total_centavos}')


while True:
    try:
        num = int(input())
        if (num >= 0 and num <= 2 * 10 ** 9):
            numero_formatado = Insere_Separacao_Milhar(str(num))
        else:
            break
        centavos = int(input())
        if (centavos >= 0 and centavos <= 99):
            numero_formatado = numero_formatado + Insere_centavos(centavos)
        else:
            break
        print(numero_formatado)
    except:
        break
