#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

candidato = {
    'nome' : input('Nome: '),
    'idade': int(input('Ano de nascimento: ')),
    'ctps' : int(input('Carteira de trabalho (0 não tem: )'))
}

print(f' - Nome tem o valor {candidato["nome"]}')
print(f' - idade tem o valor {candidato["idade"]}')
print(f' - ctps tem o valor {candidato["ctps"]}')


