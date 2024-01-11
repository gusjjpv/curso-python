"""
Modulo Collections: Ordered Dict

# Em um dicionario, a ordem de inserção dos elementos não é garantida.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave ={chave}:valor={valor}')
    
OrderedDict -> é um dicionario, que nos garante a ordem de inserção dos elementos.

#Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor{valor}')
"""

# Fazendo o import
from collections import OrderedDict

# Entendendo a diferença  entre Dict e Ordered Dict

# dicionarios comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)
# True -> Ja que a ordem dos elementos não importa para o dicionario, ele vai verificar se as chaves e os valores são iguais

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2,'a': 1})

print(odict1 == odict2) # False -> ja que a ordem dos elementos importa para o OrderedDict 
