class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Motor ligado')

    def __str__(self):
        return f'{self.cor} {self.placa} {self.numero_rodas}'

class Motocicleta(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas):
        super().__init__(cor, placa, numero_rodas)
    
    def esta_carregado(self):
        print(f'{'Sim' if self.esta_carregado else  'Nao'}estou carregado')


moto = Motocicleta('preta', 'ABC1234', 2)
print(moto)
moto.ligar_motor()

caminhao = Caminhao('branco', 'XYZ5678', 6)
print(f'caminhao: {caminhao}')
caminhao.ligar_motor()
caminhao.esta_carregado()
