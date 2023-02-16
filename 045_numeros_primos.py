#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um valor: '))
divisores = [1]

if num == 0 or num == 1:
    print(f'{num}Não é um numero primo')
else:
    for elem in range(2,num + 1):
        if num % elem == 0:
            divisores.append(elem)


if len(divisores) == 2:
    print(f'O numero é primo pois é divisível apenas por {divisores}')
else:
    print(f'O numero não é primo pois é divisível por {divisores}')
