"""
    Loop for
loop -> Estrutura de repetição
for -> uma dessas estruturas

Python
for item in interavel:
    //execução do loop
    
    utilizamos loops para interar sobre sequencias ou sobre valores iteraveis
    
    Exemplo de iteraveis:
        - String
            nome = 'Gus'
        - Lista
            lista = [1,2,3,4,5,6]
        - Ranger
            numeros = ranger(1, 10)
            
# Exemplo de for 1(inteirando em uma string)

for letra in nome:
    print(letra)    #vai imprimir as letras
    
# exemplo de for 2(inteirando sobre uma lista)
for numero in lista:
    print(numero)
    
# exemplo de for 3(inteirando sobre um range)

range(valor_inicial, valor_final)

OBS: o valor final não é incluido
    range(1, 10) vai do 1 ate o 9, o 10 nao é incluido

for numero in range(1, 6):
    print(numero)
    

 Enumerate:
 
 ((0,'g'), (1,'u'), (2,'s')...)
 for valor in enumerate(nome):
    print(valor)
    
 for indice, letra in enumerate(nome):
    print(nome[indice])
OBS: quando n precisamos de um valor, podemos descartar usando o ' _ ', vai descartar um dos valores:
    for _, letra in enumerate(nome):
        print(letra)
    no exemplo anterior, havia a variavel indice, mas como o enumerate ja retorna dois valores, incluindo o indice, n ha necessidade incluir ele
nome = 'gus'
lista = [1,2,3,4,5]
numeros = range(1, 10) # temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)


qtd = int(input('deseja que eu conte ate que numero?'))

for n in range(1, qtd+1):
    print(f'{n}')

# soma
soma = 0.0
qtd = int(input('Quantos numeros deseja somar?\n'))
for n in range(1, qtd+1):
    num = float(input(f'informe o{n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma:.2f}')

A função print ja vem com o \n por padrão, ent no loop sempre vai pular uma linha, para escrever o nome sem pular linha:
    for n in nome:
        print(letra, ent='')

nome = joao
nome * 10
vai colocar 10 joao
"joaojoaojoaojoaojoaojoaojoaojoaojoaojoao"

para mostra emoji podemos fazer:

# code original: U+1F60D
# Modificado: U0001F60D

for num in range(1, 11):
    print('\U0001F60D' * num)

"""
