#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

num01 = int(input('digite um valor: '))

num02 = int(input('digite um valor: '))

if num01 == num02:
    print("valores iguais")

elif num01 < num02:
    print('segundo valor é maior')

elif num02 < num01:
    print('primeiro valor é maior')
