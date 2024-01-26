# Podemos acessar strings como listas, mas strings são imutaveis se tentarmos alterar ela como uma lista:
#acessando o primeiro elemento da strings
S= "Hello world"
print(S[0])
# alterando o valor de um indice
#S=[0] = 'X' # typeError

#se quisermos trabalhar caractere a caractere com uma string, alterando seu valor, teremos que primeiro transformar ela em uma lista
#   tranformando a string em uma lista
L = list(S)
L[0] = "X"
print(L)
# transformando a lista em uma string novamente com o join
s="".join(L)
print(s)

#7.1 verificação parcial de strings

#quando precisa verificar se uam string começa ou termina com alguns caracteres, podemos usar o startswith e endswith
#startswith retorna true se a string começar com o valor passado
#endswith retorna true se a string terminar com o valor passado

nome = "João Gustavo"
print(nome.startswith("João"))
print(nome.startswith("joao"))
print(nome.endswith("Souza"))

# essas funções consideram letras maiusculas e minusculas como letras diferentes
# podemos resolver esse tipo de problema convertendo a para maiusculo ou minusculo
# lower("Retornar minuscuo") e upper("Retorna maiusculo")

s = "O Rato roeu a roupa do Rei de Roma"
print(s.lower())
print(s.upper())

print(s.lower().startswith("o rato"))
print(s.upper().endswith("O RATO"))

# outra forma de verificar
# utilizando in

s = "Andrei Vieira"
print("verificação com in:")
print("Andrei" in s)
print("A" in s)

# 
