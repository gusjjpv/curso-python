conjuntoReais = [float(input('Informe os Valores: ')) for _ in range(10)]
conjuntoQuadrados = []
for quadrado in conjuntoReais:
    conjuntoQuadrados.append([quadrado ** 2])
print(conjuntoReais)
print('Agora Seus quadrados')
print(conjuntoQuadrados)
