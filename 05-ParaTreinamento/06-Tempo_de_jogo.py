hora_inicial, hora_final = map(int, input().split())

if hora_final - hora_inicial > 0:
    tempo_de_jogo = hora_final - hora_inicial
else:
    tempo_dia_anterior = 24 - hora_inicial
    tempo_de_jogo = tempo_dia_anterior + hora_final

print(f'O JOGO DUROU {tempo_de_jogo} HORA(S)')
