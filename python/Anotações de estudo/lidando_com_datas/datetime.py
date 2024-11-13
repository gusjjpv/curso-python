from datetime import date, datetime, time

#vai retornar a data passada(no modelo ano/mes/dia)
d = date(2024, 11, 8)
print(d)

#vai retornar a data atual
d = date.today()
print(d)

#vai retornar a data, hora, minuto e segundo passado
d = datetime(2024, 11, 8, 5, 10, 6)
print(d)

#usando o today() ele vai pegar a data e hora atual
d = datetime.today()
print(d)
# faz a msm coisa
d = datetime.now()
print(d)

#TIME
#vai retornar a hora passada
h = time(10, 20, 12, 2)
print(h)

