#decorador
def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")
        
    return envelope
 
#usando o decorador   
@meu_decorador
def ola_mundo():
    print("ola mundo")
  

ola_mundo()