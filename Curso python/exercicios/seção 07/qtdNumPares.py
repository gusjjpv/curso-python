numeros = [int(input('Informe os valores: ')) for _ in range(10)]
print(numeros)
pares = 0
for i in numeros:
    if i%2 == 0:
        pares = pares + 1

print(pares)
 