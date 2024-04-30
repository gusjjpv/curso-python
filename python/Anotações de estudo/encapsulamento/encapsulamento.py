# recursos publicos e privados

class Conta:
    def __init(self, nro_agencia ,saldo = 0):
        # o _ antes do nome da variavel indica que ela é privada e não deve ser acessada diretamente
        self._saldo = saldo
        self.nro_agencia = nro_agencia
    
    def deposito(self, valor):
        #...
        self._saldo += valor
        
    def saque(self, valor):
        # ...
        self._saldo -= valor
    
    def saldo(self):
        return self._saldo
        
conta = Conta("1234", 100.0)
conta.deposito(20.0)

# forma n indicada de acessar o saldo
print(conta._saldo) # 120.0
# a forma certa de acessar o saldo é atraves de um metodo

print(conta.saldo()) # 120.0

