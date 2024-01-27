def converterF(tempC):
    tempF = tempC*(9.0/5.0)+32.0
    return tempF

tempC = float(input("Informe a temperatura em celsius:"))

print(f'{tempC} graus celsius em fahrenheit:{converterF(tempC)}')
