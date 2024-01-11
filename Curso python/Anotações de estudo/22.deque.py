"""
Modulo Collections - Deque

podemos dizer que o deque é uma lista de alta performace.

"""

# import

from collections import deque

# criando deques

deq = deque('geek')

print(deq)

#adiionando elementos no deque

deq.append('y') # adiciona no final, igual em listas
print(deq)

deq.appendleft('k') # adiciona no começo 
print(deq)

# remover elementos

print(deq.pop()) # remove e retorna o ultimo elemento
print(deq)

print(deq.popleft()) #remove e retorna o primeiro elemento

print(deq)
