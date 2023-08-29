codigo, quantidade = input().split()
codigo = int(codigo)
quantidade = int(quantidade)

codigos = [1, 2, 3, 4, 5]
especificacoes = ["Cachorro Quente", "X-Salada",
                  "X-Bacon", "Torrada simples", "Refrigerante"]
preco = [4.00, 4.50, 5.00, 2.00, 1.50]

if codigo in codigos:
    indice = codigos.index(codigo)
    total = quantidade * preco[indice]
    print(f"Total: R$ {total:.2f}")
