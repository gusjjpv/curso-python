"""
Leia uma distancia em quilometros e apresente-a convertida em quilometros.
A formula é: M=k/1..61, sendo K a distancia em quilometros e M em milhas
"""

km = float(input('Informe a Distancia: '))
milhas = km/1.61
print(f'A distancia {km} km em milhas é {milhas:.2f}')
# o ':.2f' é para formatar o numero float para mostras duas casas decimais.
