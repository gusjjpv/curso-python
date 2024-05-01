class Pessoa:
    def __init__(self, nome, data_nasc):
        self._nome = nome
        self._data_nasc = data_nasc
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._data_nasc
    
pessoa = Pessoa('João', 1990)
print(f"Nome: {pessoa.nome}\tIdade: {pessoa.idade} anos")