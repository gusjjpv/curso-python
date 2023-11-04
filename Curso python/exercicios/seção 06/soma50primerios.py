soma = 0
pares = 0
i = 0
while pares != 51:
    if i%2 ==0:
        pares = pares + 1
        soma = soma + i
    i = i + 1
"""
for x in range(1, 51):
    if x%2 == 0:
        soma = soma + x
"""
print(soma)
