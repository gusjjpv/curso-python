"""
# Dois conceitos basicos para aprender poo em python são class e objeto

- `class`: Uma classe é como um modelo ou um plano para criar objetos. Ela define um conjunto de atributos que caracterizarão qualquer objeto que seja fabricado a partir da classe. Os atributos são dados membros (variáveis de classe e variáveis de instância) e métodos, acessados via notação de ponto.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


Neste exemplo, `Pessoa` é uma classe que tem dois atributos: `nome` e `idade`.

- `objeto`: Um objeto é uma instância de uma classe. Um objeto inclui tanto os dados (os atributos que definem o objeto) quanto o comportamento (os métodos, ou funções, que manipulam os objetos). Cada objeto é uma instância de uma classe e pode acessar os atributos e métodos definidos na classe.

p1 = Pessoa('João', 25)

Neste exemplo, `p1` é um objeto da classe `Pessoa`. Ele tem os atributos `nome` e `idade`, que foram definidos na classe `Pessoa`.

o metodo construtor `__init__` é um metodo especial que é chamado quando um objeto é criado a partir de uma classe. Ele é usado para inicializar os atributos do objeto.

o metodo destructor `__del__` é um metodo especial que é chamado quando um objeto é destruido. Ele é usado para liberar recursos que o objeto está usando.

# Herança em POO



"""
