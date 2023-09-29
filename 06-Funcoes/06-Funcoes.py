num_testes = int(input())
for index in range(num_testes):
    x, y = input().split()
    x = int(x)
    y = int(y)
    rafael = 9 * x * x + y * y
    beto = 2 * x * x + 25 * y * y
    carlos = -100 * x + y * y * y
    if rafael > beto and rafael > carlos:
        print("Rafael ganhou")
    elif beto > rafael and beto > carlos:
        print("Beto ganhou")
    else:
        print("Carlos ganhou")
