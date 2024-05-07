"""
    Métodos de classe x métodos de estâticos
    
    Um metodo de classe recebe um primeiro parametro que aponta para a classe, enquanto um metodo estatico nao.
    @classmethod
    
    um metodo de classe pode acessar ou modificar o estado da classe enquanto um metodo estatico nao.
    @staticmethod
"""

class Pessoa:
    def __init__(self,nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def cria_de_data_nasc(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def is_adulto(idade):
        return idade > 18
    
    def __str__(self):
        return f'{self.nome} - {self.idade if self.idade != None else "Idade nao cadastrada"}'
    
p = Pessoa.cria_de_data_nasc(1990, 1, 1, 'Lucas')
print(p)
print(Pessoa.is_adulto(p.idade))
