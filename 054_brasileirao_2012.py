
tabela = ('Fluminense','Atlético-MG','grêmio','São paulo',
'Vasco','Corinthians','Botafogo','Santos','cruzeiro',
'Internacional','Flamengo','Náutico','Coritiba','Ponte preta',
'Bahia','Portuguesa','Sport','Palmeiras','Atlético-GO','Figueirense')


print(f'\nO campeonato brasileiro 2012 contou com {len(tabela)} equipes \n')
print(f'A classificação final foi: {tabela}\n')
print(f'classificados para a libertadores: {tabela[0:4]}\n')
print(f'Os times rebaixados foram: {tabela[-4:]}\n')
print(f'O nautico ficou na {tabela.index("Náutico") + 1} posição')