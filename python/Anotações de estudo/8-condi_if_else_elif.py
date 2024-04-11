"""
    Estruturas Condicionais
    if(se), else, elif(se não)
"""

idade = int(input("diga sua idade"))
# identação de 4 espaços para ser considerado como o bloco do if
if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("tem 18 anos")
else:
    print("Maior de idade")

# if ternario
status = "Menor de idade" if idade < 18 else "Maior de idade"
# comparação mais simples
