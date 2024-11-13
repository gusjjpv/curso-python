from datetime import datetime , timedelta

tipo_carro = 'G' #P, M, G
tempo_p = 30
tempo_m = 45
tempo_g = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_p)
    print(f"O carro chegou: {data_atual} e ficara pronto as {data_estimada}")
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_m)
    print(f"O carro chegou: {data_atual} e ficara pronto as {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_g)
    print(f"O carro chegou: {data_atual} e ficara pronto as {data_estimada}")