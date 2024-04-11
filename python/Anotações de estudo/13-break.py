"""
Saindo do loop com break

Funciona da msm forma que o C
Ultilizamos o break para sair de loops de maneira projetaa
"""

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('sai do loop')

#Exemplo 2

while True:
    comando = input("Digite 'sair' para sair\n")
    if comando == 'sair':
        break
print('sai do loop')
