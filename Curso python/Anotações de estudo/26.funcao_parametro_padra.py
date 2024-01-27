"""
    Funções com parametro padrão (Default paramters)

#colocando um valor ao parametro, torna o parametro opcional
# mas se coloca um parametro, o valor substituira(no exemplo vai substituir o 2)
def exponencial(numero, potencia=2):
    return numero ** potencia

#OBS: se o usuario passar somente um parametro, este sera atribuido ao parametro numero
#sera calculado o quadrado deste numero
#se passar 2 parametros, a função vai funcionar normalmente como seria

OBS:
    Em funções python, os parametros com valores default (padrão) DEVEM sempre estar ao final da declração.

# ERRO !
def teste(num=2, potencia):
    return num ** potencia

Todos os tipos de dados podem ser usados como default para parametros

# exemplo 

def soma(num1,num2):
    return num1 + num2

def mat(num1,num2,fun=soma):
    return fun(num1,num2)

def subtracao(num1,num2):
    return num1 - num2

print(mat(2,6))
print(mat(4,7,subtracao))

# ATENÇÃO com variaveis globais(se possivel evitar)

total = 0
def incremento():
    global total # avisando que queremos utilizar a variavel global
# se n utiliza o global, ira dar erro, pos isso na função é bom evitar o uso de variaveis globais    
    total = total + 1
    return total

# Podemos ter funções que são declaradas dentro de funções, e tambem tem uma forma especial de escopo de variavel

def fora():
    contador = 0
    #para usar uma variavel de uma função em uma função que esta dentro usamos o nonlocal para indicar 
    def dentro():
       nonlocal contador
       contador = contador + 1
       return contador
    return dentro()
#só podemos usar a função dentro() chamando a função fora()
"""
