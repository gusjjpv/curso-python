class Foo:
    def __init__(self, x=None):
        self._x = x
    
    #@property é um decorador que permite definir métodos como propriedades em uma classe. Isso permite que você acesse esses métodos como se fossem atributos de dados, sem a necessidade de usar parênteses. Propriedades podem ser úteis para controlar o acesso ou a modificação de atributos de uma classe e adicionar lógica adicional aos métodos getter e setter.
    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        self._x += value
    
    @x.deleter
    def x(self):
        self._x = -1
    
foo = Foo(10)
print(foo.x)