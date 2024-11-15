from pathlib import Path
"""
    # o with ele garante que o arquivo vai ser fechado msm se ocorrer um erro.
    # with open('arquivo.txt', 'r') as arquivo:
"""

with open("nome_do_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# podemos verificar se o arquivo foi aberto corretamente combinando 'with' com o 'try except'

try:
    with open("arquivo.py", 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")


# Verificar a codificação do arquivo
#with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
# ROOT_PATH = Path(__file__).parent
# try:
#     with open(ROOT_PATH/'arquivo-utf-8.txt', "w", encoding='utf-8') as arquivo:
#         arquivo.write('Aprendendo')
# except IOError:
#     print(f"erro ao abrir arquivo")

