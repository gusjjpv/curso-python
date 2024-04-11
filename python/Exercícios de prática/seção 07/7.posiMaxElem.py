num = [int(input('Digite um numero: ')) for _ in range(10)]
print(num)
print(f'Maior numero: {max(num)}')

indexMaior = num.index(max(num))

print(f'Indece do maior numero: {indexMaior}')
