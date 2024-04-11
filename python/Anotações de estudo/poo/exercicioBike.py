class Bike:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print('Bi Bi')
    
    def correr(self):
        print('Correndo')
    
    def parar(self):
        print('Parando')
    
    def __str__(self):
        return f'Bike {self.modelo} {self.cor} {self.ano}'
    
    # ou 
    
    # def __str__(self):
    #     return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

bike1 = Bike('azul', 'BMX', 2020, 500)
bike2 = Bike('vermelha', 'Caloi', 2019, 400)

print(bike1.cor)
print(bike2.cor)

bike1.buzinar()

print(bike1)