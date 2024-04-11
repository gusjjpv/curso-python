def maiorMenor(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um numero: "))

print(f'{maiorMenor(num1,num2)}')