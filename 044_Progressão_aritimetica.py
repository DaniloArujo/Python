#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Escreva o primeiro termo: '))
razao = int(input('Escreva a razão: '))

for loop in range(10):
    print(termo, end=', ')
    termo += razao

print('Fim')