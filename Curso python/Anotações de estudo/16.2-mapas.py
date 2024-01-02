"""
Mapas -> conhecidos em Python como Dicionarios

Dicionarios em python são representados por chaves {}

#inteirar sobre dicionarios

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R${receita[chave]}')

# Acessando as chaves

print(receita.keys())

# Modo pythonico
for chave in receita.keys():
    print(receita[chave])

# Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionarios

print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

"""

receita = {'jan': 100, 'fev': 90, 'mar':300}

print(receita)

# Soma*, Valor Maximo*, valor Minimo*, Tamanho
# Para usar os metodos que tem '*', os valores devem ser inteiros ou reais

print(sum(receita.values())) #soma
print(max(receita.values())) #valor maximo
print(min(receita.values())) #valor minimo
print(len(receita)) #tamanho
