#padrão ansi cores terminal = 0 none, 1 bold, 4 underline, 7 negative

print('\033[7;31;43mTeste\033[m')

#para facilitar a vida:

corverde = '\033[32m'
fimcor = '\033[m'

print(f'{corverde}teste{fimcor}')
