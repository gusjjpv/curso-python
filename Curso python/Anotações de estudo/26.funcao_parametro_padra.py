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


"""
