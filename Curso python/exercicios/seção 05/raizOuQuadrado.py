"""
    leia um numero real. se o numero for positivo imprima a raiz quadrada. do contrario, imprima o numero ao quadrado.
"""

numero = float(input("informe um numero: \n"))
if numero > 0:
    raiz_quadrada = numero ** 0.5
    
    print(f"A raiz de {numero} é {raiz_quadrada:.2f}")
else:
    num_quadrado = numero ** 2
    print(f'O {numero} ao quadrado é {num_quadrado:.2f}')

