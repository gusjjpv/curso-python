"""
Leia uma distancia em milhas e apresente-a convertida em quilometros. A formula de conversão é:
K = 1.61 * M, sendo K a distancia em quilometros e M em milhas.
"""
distMilhas = float(input('Informe a Distancia: '))
distKm = 1.61 * distMilhas
print(f'A distancia {distMilhas} m em Quilometros é {distKm}')
