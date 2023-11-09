numeros = [float(input('Informe os Valores: ')) for _ in range(8)]
print(numeros)


x = int(input('Informe a posição do primeiro numero da soma: '))
y = int(input('Informe a posição do segundo numero da soma: '))


soma = numeros[y] + numeros[x]

print(soma)
