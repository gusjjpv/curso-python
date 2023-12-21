import random

def cointoss():
    if random.randint(0,1) == 0:
        return 'cara'
    else:
        return 'coroa'

chute = input('Vai cair cara ou coroa?')

moeda = cointoss()

if chute == moeda:
    print(f'Caiu {chute} vc acertou')
else:
    print(f'Caiu {moeda}, vc ERROUUU')
