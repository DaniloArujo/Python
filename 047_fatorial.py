#Faça um programa que leia um número qualquer e mostre o seu fatorial.

numero = int(input('Digite um numero: '))
fatorial = 0



print(f'{numero}!', end=' = ')


if numero == 0 or numero == 1:
    print('')
while numero >= 1:
    if numero > 1:
        print(f'{numero} x', end=' ' )
    else:
        print(f'{numero}', end=' ')
    
    if fatorial == 0:
        fatorial = numero
    else:
        fatorial = fatorial * numero

    numero -= 1

    print(f'= {fatorial}')