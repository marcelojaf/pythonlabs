salario_pessoa = float(input())

indice_imposto = 0
imposto_a_pagar = 0

if (salario_pessoa > 2000 and salario_pessoa <= 3000):
    imposto_a_pagar = (salario_pessoa - 2000) * 0.08
elif (salario_pessoa > 3000 and salario_pessoa <= 4500):
    imposto_a_pagar = (salario_pessoa - 3000) * 0.18 + 1000 * 0.08
elif (salario_pessoa > 4500):
    imposto_a_pagar = (salario_pessoa - 4500) * \
        0.28 + 1500 * 0.18 + 1000 * 0.08

print(f"R$ {imposto_a_pagar:.2f}" if imposto_a_pagar > 0 else "Isento")
