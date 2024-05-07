class Estudante:
    #variaveis de classe
    escola = 'DIO'
    
    def __init__(self, nome, matricula):
        # variaveis de instancia
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self):
        return f'Estudante {self.nome} - {self.matricula} - {self.escola}'

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

estudante1 = Estudante('Lucas', 123)
estudante2 = Estudante('João', 321)
mostrar_valores(estudante1, estudante2)

# aq eu estou mudando o valor da variavel de classe escola
# e isso vai afetar todos os objetos da classe Estudante
# pois a variavel escola é compartilhada por todos os objetos
# da classe

Estudante.escola = 'IFSP'
aluno1 = Estudante('Lucas', 123)

# para alterar uma variavel de class somene para um objeto
# especifico, eu devo fazer isso:

aluno1.escola = 'USP'
mostrar_valores(aluno1, estudante1, estudante2)
