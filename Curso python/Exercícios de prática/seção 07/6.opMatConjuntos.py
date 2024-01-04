numPares = set({})
numImpar = set({})


for elemento in range(1,11):
    if elemento%2 == 0:
        numPares.add(elemento)
    else:
        numImpar.add(elemento)

print(f'numeros pares: {numPares}')
print(f'numeros primos: {numImpar}')

