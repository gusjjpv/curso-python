#vai abrir o arquivo em modo de escrita, se nao existir o arquivo ele cria um
arquivo = open('C:/Users/gusjj/Documents/GitHub/curso-python/python/Anotações de estudo/manipulando_arquivos/escrevendo.txt', 'w')

arquivo.write('hello world')
#o writelines vai escrever apartir de um inteiravel, uma lista, tuplas...
arquivo.writelines(['\nescrevendo\n', 'no\n', 'arquivo\n'])

arquivo.close()