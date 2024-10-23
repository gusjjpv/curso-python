""" 
    Geradores
    
São tipos especiais de iteradores, ao contrario das listas ou outros iteraveis, não armazanam todos os seus valores na memoria.

sao definidos usando funções regulares, mas, ao inves de retornar valores usando "return", utilizam "yield"

uma vez que um item gerado é consumido, ele é esquecido e não pode ser acessado novamente.

O estado interno de um gerador é mantido entre chamadas.

A execução de um gerador é pausada na declaração do "yield" e retomada dai na proxima vez que ele for chamado.

"""

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2
    
for i in meu_gerador(numeros=[1,2,3]):
    print(i)
