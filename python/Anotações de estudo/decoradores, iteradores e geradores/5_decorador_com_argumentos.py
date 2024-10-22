def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        funcao(*args,**kwargs)
        print("faz algo depois de executar")
        
    return envelope

#usando o decorador   
@meu_decorador
def ola_mundo(nome):
    print(f"ola {nome}!")
  

ola_mundo("João")