dias = int(input())

qtde_dias_por_ano = 365
qtde_dias_por_mes = 30

anos = dias // qtde_dias_por_ano
meses = (dias % qtde_dias_por_ano) // qtde_dias_por_mes
dias = (dias % qtde_dias_por_ano) % qtde_dias_por_mes

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
