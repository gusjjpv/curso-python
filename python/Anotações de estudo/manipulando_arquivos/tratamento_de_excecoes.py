"""
Execoes mais comuns:

    FileNotFoundError: Lançada quando o arquivo que esta sendo aberto nao pode ser encontrado no diretorio especificado.
    
    PermissionError: Lançado quando ocorre uma tentativa de abrir um arquivo sem as permissoes adequadas para leitura ou gravação.
    
    IOError: lancada quando ocorre um erro geral de E/S (entrada/saida) ao trabalhar com o arquivo, como problemas de permissao, falta de espaço em disco, entre outros.
    
    UnicodeDecodeError: Lançada quando ocorre um erro ao tentar decodificar os dados de um arquivo de texto usando uma codificação inadequada.
    
"""

try:
    arquivo = open("meu_arquivo.py")
except FileNotFoundError:
    print("arquivo nao encontrado")
