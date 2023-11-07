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
"""

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

"""
    Para adicionar elementos em lista utilizamos a função append ele vai adicionar no final 
    
    OBS: com append, nós só conseguimos adicionar 1 elemento por vez
    lista1.append(12, 34, 56) # Erro
"""

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
print(curso)
curso = curso.split()
print(curso)

#OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.
