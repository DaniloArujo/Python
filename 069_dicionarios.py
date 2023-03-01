
#dados = dict()


dados = {'nome':'Danilo','idade':'28'}

print(dados['nome'])
print(dados['idade'])

dados['sexo'] = 'M'

print(dados)

del dados['sexo']
print(dados)

print(dados.values())
print(dados.keys())
print(dados.items())

dados['sexo'] = 'M'
dados['cor'] = 'pardo'

for k,v in dados.items():
    print(f'{k} {v}')

