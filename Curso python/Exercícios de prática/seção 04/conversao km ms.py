"""
Leia uma velocidade em km/h(quilometro por hora) e apresente-a
em m/s(metro por segundo). A formula de conversao é: M = K/3.6
sendo K a velocidade em km/h e M em m/s
"""

veloKm = float(input('informe a velocidade: '))
veloMs = veloKm/3.6
print(f'A velocidade {veloKm} Km/h em M/s é {veloMs}')
