valores = list()

for cont in range(0,5):
    valores.append(int(input('Digite o Valor: ')))

print('\n')

for c, v in enumerate(valores):
    print(f'Encontrei {v} na posição {c}')


print('\n')