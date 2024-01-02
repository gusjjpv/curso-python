"""
Listas

Listas em python funciona como vetores/matrizes (arrays)  em outras linguagens, com a diferernça de serem DINAMICO e tambem de poderem colocar QUALQUER tipo de dado.

linguagens C/Java: arrays
    - possuem tamanho e tipo de dado fixo;
    ou seja, nestas linguagens se vc criar um array do tipo int e com tamanho 5, este array sera SEMPRE do tipo inteiro e podera ter SEMPRE no maximo 5 valores.

Ja em Python:
    - Dinamico: não possuem tamanho fixo; ou seja, podemos criar a lista e simplesmente ir adicionando elementos:
    - Qualquer tipo de dado: não possuem tipo de dado fixo; ou seja, podemos colocar qualquer tipo de dado;
    
As listas em Python são representadas por colchetes: []

lista1 = [1,33,3,55,5,9,7,1,67,1111]
lista2 = ['g', 'u', 's']
lista3 = []
lista4 = list(range(11)) # vai criar uma lista com 11 elementos [0,1,2,3,4,5,6,7,8,9,10]
lista5 = list(range(1,11,2))
lista6 = list('gus é muito bom') # vai tranformar em uma lista de caracteres

# podemos facilmente checar se determinado valor esta contido na lista
num = 3
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')
# funciona com string tbm
let = 'u'
if let in lista6:
    print('achei a letra')
else:
    print('noa encontrei a letra')

# Podemos facilmente ordernar uma lista
lista1.sort()
#print(lista1)

# Podemos facilmente contar o numero de ocorrencias de um valor em uma lista

#print(lista1.count(1))
#print(lista6. count('e'))

# Adicionar elementos em listas

    Para adicionar elementos em lista utilizamos a função append ele vai adicionar no final 
    
    OBS: com append, nós só conseguimos adicionar 1 elemento por vez
    lista1.append(12, 34, 56) # Erro

print(lista1)
lista1.append(4)
#print(lista1)

lista1.append([1,2,3])
#print(lista1)

if [1,2,3] in lista1:
    print('encontrei a lista')
else:
    print('nao encontrei a lista')

# 'extend' adiciona os elementos da lista, na outra lista(diferente do append que adiciona a lista na lista) no final da fila

lista1.extend([234,333,555])
#print(lista1)

# pode usar para adicionar strings na lista

# Podemos inserir um novo elemento na lista informando a posição do indice
# OBS: Isso não substitui o valor inicial, O mesmo sera deslocado para a direita da lista

lista6.insert(3, 'é lindo')
#print(lista6)

# Podemos facilmente juntar duas listas
lista7 = list('são paulo campeão')
lista8 = lista6 + lista7
#print(lista8)

# inverter a lista

lista7.reverse()
#print(lista7)

# copiar uma lista

lista9 = lista1.copy()
#print(lista9)

# Podemos contar quantos elementos existem dentro da lista
#print(len(lista9))

# Podemos remover facilmente o ultimo elemento de uma lista
# O pop alem de remover o ultimo elemento, ele o retorna o elemento
#print(lista9)
lista9.pop()
#print(lista9)

# Podemos remover o elemento pelo indice
# OBS: Os elementos a direita desde indice serão deslocados para a esquerda
lista9.pop(5)
#print(lista9)

# Podemos remover todos os elementos(zerar a lista)

#print(lista9)
lista9.clear()
#print(lista9)

# Podemos facilmente repetir elementos em uma lista
nova = [1,2,3]
#print(nova)
nova = nova * 3
#print(nova)

# Podemos facilmente converter uma string para uma lista

#exemplo 1

curso = 'Programação em  Python: Essencial'
#print(curso)
curso = curso.split()
#print(curso)

#OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2

curso = 'Programação em  Python: Essencial'
print(curso)
curso = curso.split(',')
#print(curso)

# Convertendo uma lista em uma string

listastring = ['Programação', 'em', 'Python']
#print(listastring)

# abaixo estamos falando: pega a listastring, coloca espaço entre cada elemento e tranforma em uma string
curso = ' '.join(listastring)
#print(curso)
# pode colocar qualquer caractere para forma a string

teste = ['oi', 'testando']
varteste = '#'.join(teste)
#print(varteste)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

listadados = [1,2,3, True, 'gus', False, [1,3,2], 40295406]

#print(type(listadados))

# Inteirando sobre listas

listanova = [1,2,3,4,5]

for elemento in listanova:
    print(elemento)

# usando while

carrinho = []
produto = ''

while produto != 'sair' and produto != 'SAIR':
    produto = input("Informe o produto ou digite 'sair' para sair:\n")
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
  

# Ultilizando variaveis em listas

listanumeros = [1,2,3,4,5]
#podemos ultilizar variaveis e vai ser a msm coisa

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

listanumeros = [num1,num2,num3,num4,num5]
#print(listanumeros)

# Fazendo acesso aos elementos de forma indexada

#           0       1           2       3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) #branco

# fazer acesso aos elementos de forma indexada inversa

print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde
# print(cores[-5]) # Erro, não existe indice -5

for cor in cores:
    print(cor)


indice = 0

while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# gerar indice em um for

for indice, cor in enumerate(cores):
    print(indice, cor)

# listas aceitam valores repetidos

listas = []
listas.append(42)
listas.append(42)
listas.append(33)
listas.append(33)

print(listas)

# outros metodos não tão importantes mas tambem uteis

# encontrar o indice de um elemento na lista

numeros = [5,6,,5,7,8,9,10]

#em qual indice da lista esta o valor 6?
print(numeros.index(6))
#em qual indice da lista esta o valor 6?

# OBS: caso não tenha este elemento na lista, sera apresentado erro ValuerError

print(numeros.index(5)) # existem dois cincos, vai ser retornado o valor do primeiro elemento encontrado

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1)) # buscando a partir do indice 1
print(numeros.index(5, 2)) # buscando a partir do indice 2
print(numeros.index(5, 3)) # buscando a partir do indece 3
# print(numeros.index(5, 4)) # buscando a partir do indice 4
# OBS: caso não tenha este elemento na lista, sera apresentado erro ValueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6)) # busca o indice do valor 8, entre os indices 3 a 6


# Revisar de slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhamos com slice de lista com o parametro 'inicio'

lista = [1,2,3,4]

print(lista[1:]) # iniciando no indice 1 e pegando todos os elementos restantes

# trabalhando com slice de lista com o parametro 'fim'

print(lista[:2]) # começa em 0, pega ate o indice 2 - 1
print(lista[:4]) # começa em 0, pega ate o indice 4 - 1
print(lista[1:3]) # comeca em 1, pega ate o indice 3 - 1

# trabalhando com slice de lista com o parametro 'passo'

print(lista[1::2]) # Começa em 1, vai ate o final, de 2 em 2

print(lista[::2]) # começa em 0, vai ate o final, de 2 em 2

# invertendo valores em uma lista
nomes = ['Joao', 'gus']

nomes[0], nomes[1] = nomes[1], nome[0]

print(nomes)
nomes = ['geek', 'University']

# jeito mais pythonico
nomes.reverse()
print(nomes)

# Soma*, valor maximo, valor minimo, tamanho

lista=[1,2,3,4,5]

print(sum(lista)) # soma
print(max(lista)) # maximo valor
print(min(lista)) # minimo valor
print(len(lista)) # tamanho da lista

# Transformado uma lista em tupla

lista = [1,2,3,4,5,6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(lista))

# Desempacotamento de listas

lista = [1,2,3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um numero diferente de elementos na lista ou variaveis para receber os dados, temos ValueError

# IMPORTANTE!!!
# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy

lista = [1,2,3]
print(lista)

nova = lista.copy() # copia

print(nova)

print(lista)
print(nova)

# Veja que utilizarmos lista.copy()  copiamos os dados da lista para uma nova lista, mas elas ficam totalmente indepedentes, ou seja, modificando uma lista,  não afeta a outra. isso em Python é chamado de Deep Copy(copia profunda)

# Forma 2 - Shallow Copy

lista = [1,2,3]
print(lista)

nova = lista # copia

print(lista)
print(nova)

# veja que ultilizamos a copia via atribuição e copiamos os dados da lista para a nova lista, mas apos realizar modificação em uma das listas, essas modificações se reflete em ambas as listas, Isso em Python chamamos de Shallow Copy
"""
