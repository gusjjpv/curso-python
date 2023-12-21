"""
leia um numero inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro
"""

num = int(input('informe o numero: '))
numTriplo = num * 3
sucessorTriplo = numTriplo + 1
numDobro = num * 2
antecessorDobro = numDobro - 1

soma = antecessorDobro + sucessorTriplo
print(soma)
