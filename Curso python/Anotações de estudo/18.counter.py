"""
Modulo Collections - Counter(Contador)

Collection -> High-performance Container Datetype

Counter -> Recebe um interavel como parametro e cria um objeto do tipo collections Counter que é parecido com um dicionario, contendo como chave o elemento da lista passada como parametro e como valor a quantidade de ocorrencias desse elemento.

# Utilizano o Counter

# Realizando o import

from collections import Counter

# Exemplo 1

#podemos utilizar qualquer iteravel, aqui usamos uma lista

lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5]

# Utilizando o Counter
res = Counter(lista)

print(res)
# Counter({3:4, 1:3, 2:2, 5:2, 4:1})

# Veja que, para cada elemento da lista, o counter criou uma chave e colocou como valor a quantidade de ocorrencias

# Exemplo 2

print(Counter('São paulo maior do brasil'))

# Counter({'o': 4, ' ': 4, 'a': 3, 'l': 2, 'i': 2, 'r': 2, 'S': 1, 'ã': 1, 'p': 1, 'u': 1, 'm': 1, 'd': 1, 'b': 1, 's': 1})

"""
from collections import Counter

# Exemplo 3

texto = """Stardew Valley é um RPG sem fim da vida no campo! Você herdou a antiga fazenda de seu avô no Vale do Orvalho. 
Equipado com ferramentas de segunda mão e algumas moedas, você irá começar sua nova vida. 
Será que você consegue aprender a viver da terra e transformar esses campos absurdamente vegetados em uma casa próspera? Não vai ser fácil. 
Desde que Corporação Joja veio à cidade, os antigos modos de vida quase desapareceram. 
O Centro Comunitário, uma vez o lugar mais visitado da cidade, agora está em ruínas. 
Mas o vale parece cheio de oportunidades. 
Com um pouco de dedicação, você pode ser a pessoa que restaurará a grandeza do Vale do Orvalho!"""

palavras = texto.split()

#print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(3))
