"""
    polimorfismo
    - Polimorfismo é o princípio pelo qual duas ou mais classes derivadas de uma mesma superclasse podem invocar métodos que têm a mesma assinatura (nome e parâmetros) mas comportamentos distintos.
"""

class Passaro:
    def voar(self):
        print('Voando...')
        
class Pardal(Passaro):
    def voar(self):
        super().voar()
        
class Pinguim(Passaro):
    def voar(self):
        print('Pinguim não voa...')
        
def voar_com(obj):
    obj.voar()

voar_com(Pardal())
voar_com(Pinguim())