"""
Tipo Númerico

para receber um resultado inteiro em uma divisao que seria um resultado real(float), pode usar o '//'
5//2 = 2
5/2 = 2.5
ou tbm
int(5 / 2) = 2


para usar potencia, em python usamos '**'
3 ** 3 = 27
2 ** 8 = 256

em python, o limite do numero inteiro depende da sua memoria

Em python podemos separar as unidades com '_'

1000000= 1 milhão ou 1_000_000(mais facil identificar)
é possivel converter de int para float:
num = 10_000
float(num)


A função type(), você pode colocar a variavel(ou numero) e ela vai te dizer qual o tipo
Exemplo:
num = 2.5
type(num)
<class 'float'>

# Operador IS => comparação de objetos


O operador is em Python é usado para testar se duas variáveis se referem ao mesmo objeto. A comparação "is" não é a mesma que a comparação "==".

O operador "==" compara os valores das duas variáveis, enquanto o operador "is" compara se as duas variáveis se referem ao mesmo objeto na memória.
ex.:
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)  # True, porque os valores são iguais
print(a == c)  # True, porque os valores são iguais

print(a is b)  # True, porque 'a' e 'b' se referem ao mesmo objeto
print(a is c)  # False, porque 'a' e 'c' se referem a objetos diferentes, embora seus valores sejam iguais

Operador de associação 

Os operadores de associação em Python são usados para testar se uma sequência é apresentada em um objeto. Existem dois operadores de associação:

in: Retorna True se uma sequência com o valor especificado é encontrada no objeto.

not in: Retorna True se uma sequência com o valor especificado não é encontrada no objeto.

Aqui está um exemplo:

lista = [1, 2, 3, 4, 5]

print(3 in lista)  # Retorna True, porque 3 está na lista
print(6 in lista)  # Retorna False, porque 6 não está na lista
print(6 not in lista)  # Retorna True, porque 6 não está na lista

"""
