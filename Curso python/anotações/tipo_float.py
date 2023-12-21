"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: o separador de casas decimmais na programação é o ponto '.' não a virgula.

"""

# Errado do ponto de vista do float, mas gera uma tupla
valor = 1, 55
print(valor)



# Certo no ponto de vista float

valor = 1.55
print(valor)
print(type(valor))

# É possivel
valor1, valor2 = 1, 44
# esta atribuindo um valor a variavel, na ordem que é declarada.
# valor1 = 1 ; valor2 = 44

print(valor1)
print(valor2)

# podemos converter um float para um int
"""
OBS: ao converter valores float para inteiros, nos perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))

# podemos trabalhar com numeros complexos:
# os numeros complexos são representados pelo 'j' = '5j'

variavel = 5j
print(variavel)
print(type(variavel))
