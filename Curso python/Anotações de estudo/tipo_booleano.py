"""
Tipo booleano

2 constantes, verdadeiro ou falso
True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiuscula

Errado:

true, false

Certo:

True, False
"""
ativo = False

print(ativo)

"""
Operações básicas:
"""

# Negação (not):
"""
fazendo a negação, se o valor booleano for verdadeiro sera falso, se for falso o resultado
sera verdadeiro, ou seja, sempre o contrario.
"""
print(not ativo)
ativoTeste = not True
print(ativoTeste, 'a')
logado = False

# Ou (or)
"""
É uma operação binaria, ou seja, depende de dois valores, ou um ou outro deve ser versadeiro.
True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

# E (and)
"""
Tambem é uma operação binaria, ou seja, depende de dois valores. ambos os valores devem ser verdadeiro.
True and True -> True
True and False -> False
True and True -> False
False and False -> True
"""


