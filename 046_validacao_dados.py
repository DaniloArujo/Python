# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Informe o seu sexo: ')

while (sexo != 'm' and sexo != 'f'):
    sexo = input('Dados inválidos. por favor, informe o seu sexo: ')


print(f'Sexo {sexo} Registrado com sucesso!')
