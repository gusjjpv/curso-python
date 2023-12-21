"""
Ranges
- Precisamos conhecer o loop for para usar os rangers.
- Precisamos conhecer o range par trabalhar melhor com loops

Rangers são utilizados para gerar sequencias numericas, não de forma aleatoria, mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão é 0, e passo da de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num) 

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive(inicio especificado pelo usuario, e passo de 1 em 1)

# Exemplo Forma 2

for num in range(4, 11):
    print(num)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive(inicio especificado pelo usuario, e passo especificado pelo usuario)

# Exemplo Forma 3

for num in range(5,55,5):
    print(num)
    
# Forma 4(inverso)

range(valor_de_inicio, valor de parada, passo)

OBS: valor_de_parada não inclusive(inicio especificado pelo usuario, e passo especificado pelo usuario)

#Exemplo Forma 4:
for num in range(20, -1, -1):
    print(num)

# Array usando range
    Podemos criar um array usando o range
    nome_da_lista = list(range(valor))
    
"""
