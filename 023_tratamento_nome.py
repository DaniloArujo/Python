#Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = input('Digite seu nome: ').strip()

print(f'Seu nome é: {nome}')
print(f'Em maiusculo: {nome.upper()}')
print(f'Em minusculo: {nome.lower()}')

replace = nome.replace(' ','')
#Posso fazer a conta assim: len(nome) - nome.count(' ')
print(f'Seu nome tem {len(replace)} letras')

lista = nome.split()
print(f'Seu primeiro nome tem {len(lista[0])} letras')
