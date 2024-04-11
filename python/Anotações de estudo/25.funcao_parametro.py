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

# parametros especiais 

Em Python, existem três tipos de parâmetros que você pode usar ao definir uma função: positional-only, keyword-only e uma combinação dos dois.

Positional-only parameters: São parâmetros que só podem ser passados para uma função na ordem correta. Eles são definidos na função sem um valor padrão ou antes de um / na lista de parâmetros.
def func(a, b, /):
    return a + b

# a e b são positional-only parameters
print(func(1, 2))  # Isso funciona
print(func(a=1, b=2))  # Isso gera um erro

Keyword-only parameters: São parâmetros que só podem ser passados para uma função como argumentos nomeados. Eles são definidos na função após um * ou *args na lista de parâmetros.

def func(*, a, b):
    return a + b

# a e b são keyword-only parameters
print(func(a=1, b=2))  # Isso funciona
print(func(1, 2))  # Isso gera um erro

Combinação de positional e keyword parameters: Você pode definir uma função que aceita ambos os tipos de parâmetros. Os parâmetros posicionais devem vir primeiro, seguidos por * ou *args, e então os parâmetros keyword-only.

def func(a, b, *, c, d):
    return a + b + c + d

# a e b são positional parameters, c e d são keyword-only parameters
print(func(1, 2, c=3, d=4))  # Isso funciona
print(func(1, 2, 3, 4))  # Isso gera um erro


 
"""
