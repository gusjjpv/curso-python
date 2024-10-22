def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")
        
    return envelope
    

def ola_mundo():
    print("ola mundo")
    
# exemplo 1
ola_mundo1 = meu_decorador(ola_mundo)
ola_mundo()



