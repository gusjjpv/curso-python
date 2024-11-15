arquivo = open("C:/Users/gusjj/Documents/GitHub/curso-python/python/Anotações de estudo/manipulando_arquivos/exemplo.txt", "r")

#vai ler todo o arquivo
print(arquivo.read())

#vai ler linha por linha
#so teve uma chamada, ent vai ler apenas a primeira linha
print(arquivo.readline())

# tem o readlines() que vai ler as linhas e adicionalas a uma lista
arquivo.close()
