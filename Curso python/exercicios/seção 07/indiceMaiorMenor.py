numeros = [float(input('Informe os valores: ')) for _ in range(5)]
menor = numeros.index(min(numeros), 0)
maior = numeros.index(max(numeros), 0)

print(max(numeros))
print(maior)
print(min(numeros))
print(menor)
