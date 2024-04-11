pares = []
for _ in range(6):
    num = int(input('Informe o numero par: '))
    if num > 0:
        if num%2 == 0:
            pares.append(num)
        else:
            while num%2 != 0:
                print('Erro! Informe apenas numeros pares')
                num = int(input('Informe o numero par: '))
                if num%2 == 0:
                    pares.append(num)
                    break
    else:
        while num <= 0:
            print('Erro! Informe um numero maior que 0')
            num = int(input('Informe o numero par: '))
            if num%2 == 0:
                    pares.append(num)
                    break
            else:
                while num%2 != 0:
                    print('Erro! Informe apenas numeros pares')
                    num = int(input('Informe o numero par: '))
                    if num%2 == 0:
                        pares.append(num)
                        break
pares.reverse()
print(pares)

"""
    codigo ficou bom, corrigir erros, trabalhou bastante a logica, codigo ficaria mais bonito se eu usasse funções
"""
