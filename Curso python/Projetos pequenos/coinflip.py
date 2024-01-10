import random

print('Bem vindo ao jogo de cara ou coroa')

acertos = 0
erros = 0

while True:
    def cointoss():
        if random.randint(0, 1) == 0:
            return 'cara'
        else:
            return 'coroa'

    chute = input('Vai cair cara ou coroa?')

    moeda = cointoss()

    if chute == moeda:
        print(f'Caiu {chute} vc acertou')
        acertos = acertos + 1
    else:
        print(f'Caiu {moeda}, vc ERROUUU')
        erros = erros + 1

    print('Deseja jogar novamente?')
    resposta = input()
    if resposta == 'nao' or resposta == 'n' or resposta == 'N' or resposta == 'NAO' or resposta == 'Não' or resposta == 'não':
        break

print(f'O total de acertos foi:{acertos}\nO total de erros foi:{erros}')
print('Obrigado por jogar')
