"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a' 'True', '42.5'
- Estiver entre aspas duplas -> "uma string", "234", "a"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a'''
- Estiver entre aspas duplas triplas

Se voce abrir as aspas com uma simples, voce tem que finalizar com uma simples e assim por diante
"""

nome = 'gus'
frase = "gus joga demais ta maluco"
print(nome)
print(type(nome))
print(frase)
print(type(frase))

# O mais comum é o aspas simples
# Para usar uma aspas simples em uma string, usa uma aspas duplas, se for usar uma
# aspas duplas, usa aspas simples/duplas triplas

bar = "Gina's Bar"
print(bar)
print(type(bar))

# Para pular linhas
# \n funciona
pularLinha = 'pule uma linha \n linha pulada'
print(pularLinha)
print(type(pularLinha))

nome = """ joao
gus"""
print(nome)

"""Funções legais para String"""

# Colocar tudo em maiusculo

nome = 'João Gustavo'
print(nome.upper())

# Colocar tudo em minusculo

nome = 'JOÃO GUSTAVO'
print(nome.lower())

# Colocar a primeira letra em maiusculo

nome = 'joão gustavo'
print(nome.title())

# eliminando espaços em branco

curso = '   Curso de Python   '
print(curso.strip())
print(curso.lstrip())  # elimina os espaços a esquerda
print(curso.rstrip())  # elimina os espaços a direita

# junçoes e centralização

print(",".join(curso))
# junta cada letra da string com uma virgula

# centraliza a palavra 'Curso de Python' em 20 caracteres, preenchendo com '*'
print(curso.center(20, '*'))


# Colocar em um lista/array

sp = 'São Paulo o maior do Brasil'
print(sp.split())

# Para imprimir uma parte da frase, vamos usar 'arrays', chamamos isso de SLICE DE STRING
# Nesse exemplos vamos do indice 0(primeira letra), ate o indice 9
print(sp[0:9])

# Imprime 'O maior do Brasil', esta começando do indice 10 e vai ate o 27
print(sp[10:27])


# Podemos usar o split para tranformar em uma lista e usar o slice de string

sp = 'São Paulo'
print(sp.split()[1])


"""
# Para inverter a string 
[::-1] -> comece do primeiro elemento, va ate o ultimo elemento e inverta
"""
nome = 'sao paulo'

print(nome.upper()[::-1])
print('tes: 1', sp[2::-1])

# trocar letras
# onde tiver 's' vai ser substituido por 'j'
print(nome.replace('s', 'j'))
# em sao paulo temos dois 'a', se substituimos o 'a' por outra letra, vai ser trocada todas as letras 'a'
