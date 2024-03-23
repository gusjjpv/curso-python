"""
Recebendo do usuario

input() -> Todo dado recebido via input é do tipo String
Em Python, string é tudo que estiver entre:
- Aspas simples -> 'João'-
- Aspas duplas -> "João"
- Aspas simples triplas ->'''João'''
"""
# - Aspas duplas triplas -> """João"""

# entrada do usuario

# print("Qual seu nome? ")
# nome = input()  # input -> Entrada
# print('Qual sua idade? ')
# idade = input()
# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}' .format(nome))

# forma simplificada de um input e print
nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem vindo(a) {nome}')

# Processamento

# Saida de dados

# Exemplo de print 'antigo' 2.x
# print('A(o) %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('A(O) {0} tem {1} anos' .format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'A(O) {nome} tem {idade} anos')

"""
int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.

O cast pode ser feito na propria declaração da variavel
Exemplo:
int idade = input()

outra forma de conveter:
    idade = int(input('informe a sua idade: '))
"""
# pequeno calculo para saber o ano que a pessoa nasceu// detro das chaves podemos faze calculos(processamentos)
print(f'A {nome} nasceu em{2023 - int(idade)}')

# formatar a saida de dados

PI = 3.141592

print(f'O valor de PI é {PI:.2f}')  # :.2f -> duas casas decimais
print(f'O valor de PI é {PI:.4f}')  # :.4f -> quatro casas decimais
# :10.2f -> dez caracteres com duas casas decimais
print(f'O valor de PI é {PI:10.2f}')

# print tem argumentos que podem ser passados para ele
# sep -> separador / vai separar os argumentos
# end -> final / vai finalizar a linha com o que for passado
# print(nome, idade, sep='-', end='###') == "nome-idade###"
