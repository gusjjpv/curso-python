"""
Definindo funções
- Funções são pequenas partes do codigo que realizam tarefas especificas;
- pode ou nao receber entradas de dados e retornar uma saida de dados;
- muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza varias tarefas dentro dela:
é bom fazer uma verificação para que a função seja simplificada

ja utilizamos varias funções desde que iniciamos este curso:

- print()
- len()
- e muito mais;

Em Python, a froma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

onde:

- nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome composto, separado por underline (Snake Case);
- parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opicionais ou não;
- bloco_da_funcao -> Tambem chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao python que estamos definindo uma função. Tambem abrimos o bloco de codigo com : que é utilizado em python para definir blocos.
"""

# definindo a primeira função

def diz_oi():
    print('oi')

# chamando a função 

diz_oi()

# Em python, podemos inclusive criar variasveis do tipo de uma função e executar esta função atraves da variavel

cumprimentar = diz_oi

cumprimentar()