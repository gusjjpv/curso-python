"""
            (parametro)
def quadrado(num):
    return num ** 2

print(quadrado(2)) 

# funções podem ter n paramentros, separados por virgula


def soma(a,b):
    return a + b

print(soma(1,2))

# OBS: se a gente informar um numero errado de parametros ou argumentos, teremos TypeError

# Nomeando parametros
def nome_completo(string1, string2):
    return f'seu nome completo é {string1} {string2}'


#print(nome_completo('Joao', "Gus"))
#seria melhor colocar como nome dos parametros 'nome' 'sobrenome', fica melhor de let o codigo

def nome_completo(nome, sobrenome):
    return f'seu nome completo é {nome} {sobrenome}'

# a ordem dos parametros importa
# se inverter pode gerar erro

# Agumentos nomeados (Keyword Arguments)
# Caso utilizamos nomes dos parametros nos argumentos par informa-los, podemos utilizar qualquer ordem.
print(nome_completo(nome='gus',sobrenome='souza'))
print(nome_completo(sobrenome='souza', nome='gus'))
"""

