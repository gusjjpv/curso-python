"""
Modulo collections - Defalut Dict

# Recap dicionarios

dicionario = {'curso': 'Python'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) # KeyError

Default Dict -> Ao criar um dicionario utilizando-o, nós informamos um valor default, podendo utilizar um lambda para isso. Esse valor sera utilizado sempre que não houver um valor definido. caso tentemos acessar uma chave que não existe, essa chave sera criada e o valor default sera atribuido.

OBS: Lambdas são funções sem nome, que podem ou não receber parametros de entrada e retornar valores.

"""

# fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'python'

print(dicionario)

print(dicionario['outro']) # KeyError no dicionario comum, mas aq nao

print(dicionario)
