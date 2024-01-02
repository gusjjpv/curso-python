import random

def cointoss():
    if random.randint(0,1) == 0:
        return 'cara'
    else:
        return 'coroa'

while True:
    
    chute = input('Vai cair cara ou coroa?')

    moeda = cointoss()

    if chute == moeda:
        print(f'Caiu {chute} vc acertou')
    else:
        print(f'Caiu {moeda}, vc ERROUUU')

    print('Deseja jogar novamente?')
    resposta = input()
    if resposta == 'nao' or resposta == 'n' or resposta == 'N' or resposta == 'NAO' or resposta == 'Não' or resposta == 'não':
        break
