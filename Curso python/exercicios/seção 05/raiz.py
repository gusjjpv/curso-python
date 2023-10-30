"""
Leia um numero fornecido pelo usuario. se o numero for positivo, clacule a raiz quadrada do numero. se o numero for negativo, mostre uma mensagem dizendo que  o numero é invalido
"""

numero = int(input("informe o numero: \n"))
if numero > 0:
    # Calcula a raiz quadrada de um número
    raiz_quadrada = numero ** 0.5
    # Imprime o resultado
    print("A raiz quadrada de", numero, "é", raiz_quadrada)
else:
    print("numero invalido")
