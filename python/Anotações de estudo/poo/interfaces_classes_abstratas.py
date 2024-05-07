# criando uma classe abstrata com o modulo abc(@abstractmethod)

from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class ControleTv(ControleRemoto):
    def ligar(self):
        print('Ligando a TV')
        print('Ligada!')
    
    def desligar(self):
        print('Desligando a TV')
        print('Desligada!')

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando o Ar Condicionado')
        print('Ligado!')
    
    def desligar(self):
        print('Desligando o Ar Condicionado')
        print('Desligado!')

controle = ControleTv()
controle.ligar()
controle.desligar()

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
