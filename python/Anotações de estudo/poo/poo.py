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

    em python herança é a capacidade de criar uma classe que herda atributos e métodos de uma classe pai. A classe pai é chamada de superclasse e a classe filha é chamada de subclasse.


    beneficios da herança:
    - Reutilização de código
        *Fornece uma maneira de reutilizar o código de uma classe existente, evitando a duplicação de código.
        se a classe filha precisa de funcionalidades adicionais, ela pode adicionar novos atributos e métodos sem alterar a classe pai.
        se a classe filha herda da class pai, ela pode acessar todos os atributos e métodos da classe pai.

sintaxe da herança:
"""

class A:
    pass

class B(A):
    pass

# Neste exemplo, a classe `B` herda da classe `A`. Isso significa que a classe `B` terá todos os atributos e métodos da classe `A`.

# Herança multipla

class C(A, B):
    pass

# Neste exemplo, a classe `C` herda de duas classes, `A` e `B`. Isso significa que a classe `C` terá todos os atributos e métodos das classes `A` e `B`.
