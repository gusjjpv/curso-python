notas = [float(input('Informe suas notas: ')) for _ in range(2)]
if notas[0] and notas[1] > 0.0 and notas[0] and notas[1] < 10.0:
    media = (sum(notas))/len(notas)
    print(media)
else:
    print('Notas invalidas!!\nNotas Validas devem ser maior que 0.0 e menor que 10.0')
