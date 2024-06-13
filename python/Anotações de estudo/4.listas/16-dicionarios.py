"""
Dicionarios 

OBS: em algumas linguagens de programação são conhecidos por mapas.

Dicionarios são coleções do tipo chave/valor.

Dicionairios são representados por {}.

print(type({}))

OBS: sobre dicionarios
    - Chave e valor são separados por dois pontos ' chave:valor ';
    - tanto chave quanto valor podem ser qualquer tipo de dado, mas a chave tem que ser imutavel;
    - podemos misturar tipos de dados

# Criação de dicionarios

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua':'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (menos comum)

paises = dict(br='Brasil', eua='Estados Unidos da America', py='Paraguai')

print(paises)
print(type(paises))

# forma de adicionar a um dicionario 

paises['jap'] = 'japao'

# Acessando elementos

# Forma 1 - Acessando via chave, da msm forma lista/tupla

paises = {'br': 'Brasil', 'eua':'Estados Unidos', 'py': 'Paraguai'}
print(paises['br'])
print(paises['eua'])

# OBS: caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro keyError

# Forma 2 - Acessando via get - RECOMENDADA

print(paises.get('br'))
print(paises.get('ru')) # vai retornar None, pois n existe a chave

# caso o get não encontre o objeto com a chave informada sera retornado o valor None e não sera gerado KetError

pais = paises.get('ru')

if pais:
    print(f'encontrei o pais {pais}')
else:
    print('Não encontrei o pais')

paises = {'br': 'Brasil', 'eua':'Estados Unidos', 'py': 'Paraguai'}

# podemos definir um valor padrao para caso nao encontremos o objeto com a chave informada
pais = paises.get('ru', 'não encontrado')

print(f'encontrei o pais {pais}')


# podemos verifica se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('estados unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']


# Podemos utilizar qualquer tipo de dado(int, float, string, boolean), inclusice lista, tupla dicionario, como chaves de dicionarios.

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionarios, pois as mesmas são imutaveis

localidades = {
    (35.3234, 39.3254): 'escritorio em Tokio', 
    (40.6409, 74.0909): 'escritorio em Nova York',
    (37.7799, 122.3242): 'escritorio em São Paulo',  
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionario

receita = {'jan': 100, 'fev': 200, 'mar': 500}

print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 350
print(receita)

# Forma 2

novo_dado = {'mai' = 450}

receita.update(novo_dado) # receita.update({['mai': 500]})

print(receita)

#Atualizando dados em um dicionario

#forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update(['mai':600])

print(receita)

#CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicioinario é a msm.
#CONCLUSÃO 2: Em dicionarios, NÂO podemos ter chaves repetidas.

# Removendo dados de um dicionario
receita = {'jan': 100, 'fev': 200, 'mar': 500}

# Forma 1 - Mais comum

ret = receita.pop('mar')
print(ret)

print(receita)
# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor deste objeto é smepre retornado

# Forma 2

del receita['fev']

print(receita)

#se a chave não existir sera gerado um KeyError
# OBS: Neste caso o vlaor removido não é retornado

# 1 - poderiamos utilizar uma lista para isso? Sim

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o indice de cada informação no produto.

# 2 - poderiamos utilizar uma tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teriamos que saber qual é o indice de cada informação no produto

# 3 - poderiamos utilizar um dicionario para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco':2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco':150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

#Desta forma facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter a certeza sobre cada informação

# Metodos De dicionarios.

d = dict(a=1,b=2,c=3)

print(d)
print(type(d))

# Limpar o dicionario (Zerar dados)

d.clear()

print(d)

# Copiando um dicionario para outro

# Forma 1 - Deep Copy

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)

print(novo)

# Forma 2 - Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma não usual de criação de dicionarios

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# o metodo fromkeys recebe dois parametros um interavel e um valor
# ele vai ferar para cada valor do iteravel uma chave e ira atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)

"""

contatos = {
    "joaogustavo@gmail.com":{'nome':'Joao Gustavo', 'telefone':'999999999'},
    "maria@gmail.com":{'nome':'Maria', 'telefone':'888888888'},
}

print(contatos['joaogustavo@gmail.com']['telefone'])

for chave, valor in contatos.items():
    print(chave, valor)
    
# contatos['chave'] # keyerror


# o get não gera erro, caso a chave não exista, vai retornar None ou o valor default informado
contatos.get('chave') # None
contatos.get('chave', 'Não encontrado') # Não encontrado
contatos.get('joaogustavo@gmail.com', {}) # {'nome':'Joao Gustavo', 'telefone':'999999999'}

# items() retorna uma lista de tuplas com chave e valor
print(contatos.items()) # dict_items([('joaogustavo@gmail.com', {'nome': 'Joao Gustavo', 'telefone': '999999999'})

#keys() retorna uma lista de chaves
# ultil para iterar sobre dicionarios e pegar as chaves do diciionario
novo_dicionario = {"a": 1, "b": 2, "c": 3}
print(novo_dicionario.keys()) # dict_keys(['a', 'b', 'c'])

# pop() remove um item de um dicionario e retorna o valor

resultado = contatos.pop('mariana@gmail.com', "nao encontrado")
print(resultado) # nao encontrado

# popitem() remove um item aleatorio de um dicionario

#setdefault() -> forma de adicionar um elemento ao dicionario, caso a chave não exista

contatos.setdefault('idade', 20)

# values() retorna uma lista de valores
print(contatos.values()) # dict_values([{'nome': 'Joao Gustavo', 'telefone': '999999999'}, {'nome': 'Maria', 'telefone': '888888888'}])

# operador in -> verifica se a chave existe no dicionario

resultado = "joaogustavo@gmail.com" in contatos
print(resultado) # True

resultado = "mariazinha@gmail.com" in contatos
print(resultado) # False

