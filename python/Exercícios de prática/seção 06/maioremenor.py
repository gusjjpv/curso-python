maior = 0
menor = int(input('Informe o numero:'))
for x in range(1, 10):
    num = int(input('Informe o numero:'))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print('Maior: ', maior)
print('Menor: ', menor)
