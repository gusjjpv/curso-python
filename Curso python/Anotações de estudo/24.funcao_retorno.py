"""
Funções com retorno

numeros = [1,2,3]

ret_pop = numeros.pop()

ret_pr = print(f'retorno de pop: {ret_pop}')

print(f'Retorno de print: {ret_pr}')

OBS: Em python, quando uma função não retornoa nenhum valor, o retorno é None

OBS: Funções python que retornam valores, devem retornar estes valores com a palavra reservada return

OBS: não precisamos necessariamente criar uma variavel para receber o retorno de uma função. Podemos passar a execução da função para outras funções

def quadrado_de_7():
    return 7*7

# essa variavel recebe o retorno da função
ret = quadrado_de_7()

print(f'retorno: {ret}')

# chamando a função em outra função

print(f'retorno: {quadrado_de_7()}')

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes return;
3 - Podemos, em uma função, retornar qualquer tipo de dado e ate mesmo multiplos valores;

# exemplo

def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'a'

print(nova_funcao())

# Exemplo 2

def outra_funcao():
    return 1,2,3,4

num1, num2, num3, num4 = outra_funcao()

print(num1,num2,num3,num4)
"""


