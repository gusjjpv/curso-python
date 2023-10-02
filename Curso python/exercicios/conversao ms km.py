"""
Leia uma velocidade em m/s (metro por segundo) e apresente-a convertida em km/h(quilometros por hora).
A formula de conversão é: K= M * 3.6, sendo K a velocidade em km/h e M em m/s
"""

veloMs = float(input('informe a velocidade: '))
veloKm = veloMs/3.6
print(f'A velocidade {veloMs} M/s em Km/h é {veloKm}')
