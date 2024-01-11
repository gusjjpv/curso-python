"""
Modulo Collections - named Tuple

# Recap tupla

print(tupla(1))

Named Tuple -> São tupla, diferenciadas, onde, especificamos um nome para a mesma e tambem parametros.
"""

#import

from collections import namedtuple

#precisamos definir o nome e parametros.

# forma 1 - declaração named tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# forma 2 - declaração named tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# forma 3 - declaração named tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# usando

ray = cachorro(idade=2, raca='caramelo', nome='bidu')

print(ray)

# acessando os dados

# forma 1

print(ray[0]) #idade
print(ray[1]) # raça
print(ray[2]) # nome

# forma 2

print(ray.idade) # idade
print(ray.raca) # caça
print(ray.nome) # nome