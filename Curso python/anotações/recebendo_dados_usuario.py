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
"""
# pequeno calculo para saber o ano que a pessoa nasceu// detro das chaves podemos faze calculos(processamentos)
print(f'A {nome} nasceu em{2023 - int(idade)}')
