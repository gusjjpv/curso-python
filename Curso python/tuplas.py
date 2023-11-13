"""
Tuplas

    Tuplas são bastante parecidas com as listas.
    
    Existem basicamente duas diferenças basicas:
    
    1 - As tuplas são representadas por parenteses ()
    
    2 - As tuplas são imutaveis: isso significa que ao se criar uma tuplas ela não muda. Toda operação em uma tupla gera uma nova tupla
    
# CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1,2,3,4,5,6)
print(type(tupla1))

tupla2 = 1,2,3,4,5,6
print(tupla2)

print(type(tupla2))

# Cuidado 2: tuplas com 1 elemento

tupla3 = (4) # isso não é uma tupla:
print(tupla3)

print(type(tupla3))

tupla4 = (4,) # isso é uma tupla, observe que existe uma virgula no final
print(tupla4)

print(type(tupla4))

# CONCLUSÃo: Podemos concluir que tuplas são definidas pela virgula e não pelo uso do parenteses

    (4) -> não é tupla
    (4,) -> é tupla
    4, -> é tupla

# Podemos gerar uma tupla dinamicamente com um range(inicio, fim, passo)

tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('geek university', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# OBS: Gera erro(ValueError) se colocarmos um numero diferente de elementos para desenpacotar.
# Metodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutaveis

# Soma*, valor maximo*, valor minimo* e tamanho

# * se os valores forem todos inteiros ou reais

tupla = (1,2,3,4,5,6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tuplas1 = (1,2,3)
print(tuplas1)

tupla2 = (4,5,6)
print(tupla2)

print(tuplas1 + tupla2) #tuplas são imutaveis

print(tuplas1)
print(tupla2)

tupla3 = tuplas1 + tupla2

print(tupla3)
print(tupla2)
print(tuplas1)

tuplas1 = tuplas1 + tupla2 # tuplas são imutaveis, mas podemos sobrescrever seus valores
print(tuplas1)

# Verificar se determinado elemento esta contido na tupla

tupla = (1,2,3)

print(3 in tupla)
# iterando sobre uma tupla

tupla = (1,2,3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b','c', 'c', 'e','a', 'b','a', 'b',)

print(tupla.count('b'))    

escola = tupla(" Geek University")
print(escola)

print(escola.count('e'))

# Dicas na utilzação de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

# o acesso a elementos de uma tupla tambem é semelhante a de uma lista

print(meses[5])

# iterar com while

i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# verificamos em qual indice um elemento esta na tupla

print(meses.index('playstation'))

# OBS: Caso o elemento não exista, sera gerado ValueError
    
# slicing

# tupla[inicio:fim:passo]

print(meses[5:9])


# Por que utilizar tuplas?

# tuplas são mais rapidas do que listas
# tuplas deixam seu codigo mais seguro*

# isso porque trabalhar com elementos imutaveis traz segurança para o codigo

# copiando uma tupla para outra

tupla = (1,2,3)
print(tupla)

nova = tupla # na tupla não temos o problema de shallow copy

print(nova)
print(tupla)

outra = (4,5,6)

nova = nova + outra

print(nova)
print(tupla)

"""

