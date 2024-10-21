"""
Em Python, *args e **kwargs são usados em funções para permitir que você passe um número variável de argumentos para a função. Vou explicar cada um deles separadamente e fornecer exemplos para ajudar a entender melhor.

*args

*args permite que você passe um número variável de argumentos posicionais para uma função. Quando você usa *args na definição de uma função, você pode passar qualquer quantidade de argumentos e eles serão armazenados em uma tupla.

exemplo:

def soma_todos(*args):
    return sum(args)

# Chamando a função com diferentes quantidades de argumentos
print(soma_todos(1, 2, 3))        # Saída: 6
print(soma_todos(10, 20))         # Saída: 30
print(soma_todos(4, 5, 6, 7, 8))  # Saída: 30

No exemplo acima, a função soma_todos pode receber qualquer quantidade de números e somá-los.

**kwargs

**kwargs permite que você passe um número variável de argumentos nomeados (ou seja, argumentos no formato chave=valor) para uma função. Quando você usa **kwargs, os argumentos passados são armazenados em um dicionário, onde as chaves são os nomes dos argumentos e os valores são os valores passados para eles.

exemplo:

def exibir_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Chamando a função com diferentes argumentos nomeados
exibir_informacoes(nome="João", idade=30, cidade="São Paulo")

# Saída:
# nome: João
# idade: 30
# cidade: São Paulo

No exemplo acima, a função exibir_informacoes pode receber qualquer quantidade de argumentos nomeados, e ela imprime cada um dos pares chave-valor.

Combinando *args e **kwargs
Você também pode combinar *args e **kwargs em uma mesma função para aceitar tanto argumentos posicionais quanto nomeados.
"""

def funcao_exemplo(*args, **kwargs):
    print("Argumentos posicionais:", args)
    print("Argumentos nomeados:", kwargs)
    print(sum(args))

# Chamando a função com diferentes tipos de argumentos
funcao_exemplo(1, 2, 3, nome="Maria", idade=25)

# Saída:
# Argumentos posicionais: (1, 2, 3)
# Argumentos nomeados: {'nome': 'Maria', 'idade': 25}

"""
Aqui, funcao_exemplo pode lidar com ambos os tipos de argumentos, mostrando como eles são armazenados dentro da função.

Resumo
*args é usado para passar uma lista de argumentos posicionais variáveis para uma função.
**kwargs é usado para passar um dicionário de argumentos nomeados variáveis para uma função.
Esses recursos tornam as funções mais flexíveis, permitindo que lidem com diferentes números de argumentos de maneira elegante. Se você tiver mais perguntas ou quiser mais exemplos, estou à disposição!
"""
