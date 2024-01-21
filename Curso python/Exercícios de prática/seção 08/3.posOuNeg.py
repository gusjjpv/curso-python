def verificar_posi_ou_nega(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    elif num == 0:
        return 0

num = float(input('Digite um numero:'))

print(verificar_posi_ou_nega(num))
