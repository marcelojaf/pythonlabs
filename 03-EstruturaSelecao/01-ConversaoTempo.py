duracao = int(input())

horas = duracao // 3600
minutos = (duracao % 3600) // 60
segundos = (duracao % 3600) % 60

print(f"{horas}:{minutos}:{segundos}")
