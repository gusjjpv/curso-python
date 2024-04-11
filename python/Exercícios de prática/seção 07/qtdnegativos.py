numeros = []
numNegativos = 0
soma = 0
for _ in range(10):
    num = float(input('informe o numero: '))
    numeros.append(num)
    if num < 0:
        numNegativos = numNegativos + 1
    elif num > 0:
        soma = soma + num
print(numeros)
print(numNegativos)
print(soma)
