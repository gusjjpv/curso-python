"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia a teoria dos conjuntos da matematica.

- Aqui no python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matematica:

- Sets(Conjuntos) não possuem valores duplicados;
- Sets(Conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles. quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (Sets) são referenciados em Python com chaves {}

Difereça entre conjuntos (Sets) e Mapas(Dicionarios) em Python:
    - Um dicionario tem chave/vlaor:
    - Um Conjunto tem apenas valor;


# Definindo um conjunto:

# Forma 1

s = set({1,2,3,4,5,5,6,7,2,3}) #repare que temos valores repetidos

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor ja existente, o msm sera ignorado sem gerar error e não fara parte do conjunto

# Forma 2 - mais comum

s = {1,2,3,4,5,5}

print(s)
print(type(s))

# outra forma usando set(), podemos converter uma lista ou tupla para um set

lista = [1,2,3,4,5,5,7,7]
print(set(lista))
tupla = 1,1,1
print(set(tupla))

# Podemos verificar se um determinado elemento esta contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('não tem o 3')
    
# Importante lembrar que, alem de não termos valores duplicados, não temos ordem

# listas aceitam valores duplicados entao temos 10 elementos

lista = [99,2,34,2,23,12,1,44,5,34]
print(f'lista:{lista} com {len(lista)} elementos')

# tuplas aceitam valores duplicados, entao temos 10 elementos

tupla = 99,2,34,2,23,12,1,44,5,34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# dicionarios nao aceitam chaves duplicadas, entao temos 8 elementos

dicionario = {}.fromkeys([99,2,34,2,23,12,1,44,5,34], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjuntos nao aceitam valores duplicados, entao temos 8 elementos

conjunto = {99,2,34,2,23,12,1,44,5,34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# assim como todo outro conjunto python podemos colocar tipos de dados misturados em sets

s = {1,'b', True, 34.22, 44}
print(s)
print(type(s))

#podemos iterar em um set normalmente

for valor in s:
    print(valor)

# Usos interessantes com sets

# imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu e os visitantes
#informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista python, ja que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo horizonte', 'São paulo', 'Campo grande', 'Cuiaba', 'Campo grande', 'São paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, unicas, temos.

# podemos utilizar o set para isso:

print(len(set(cidades)))

# adicionando elementos em um conjunto

s = {1,2,3}

s.add(4)
s.add(4) # duplicidade nao gera erro. simplismente é ignorado e não é adicionado.
print(s)

# remover elementos em um conjunto

s = {1,2,3}
print(s)

# forma 1

s.remove(2) # NÂO é indice!! informamos o valor a ser removido

print(s)

# OBS: Caso o valor não seja encontrado sera ferado o erro KeyError, nenhum valor é retornado

# forma 2

s.discard(3)

print(s)

# OBS: se o valor n for encontrado nenhum erro é gerado

# copiando um conjunto para outro

s = {1,2,3}
print(s)

# forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy

novo = s

novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)


# Metodos matematicos de Conjunto

# Imagine que temos dois conjuntos: um contendo estudantes do curso python e um contendo estudantes do curso de java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}

estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# veja que alguns alunos que estudam python tambem estudam java

# precisamos gerar um conjunto com nomes de estudantes unicos

# forma 1 - utilizamos union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - utilizando o caractere pipe |

unicos2 = estudantes_python | estudantes_java

print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - utilizando intersection

ambos1 = estudantes_java.intersection(estudantes_python)
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que nao estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)


# Soma*, valor maximo*, valor minimo*, tamanho

# * se os valores forem todos inteiros ou reais

s = {1,2,3,4,5,6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

"""

