#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
contador = 0

for x in range (1,500,2):
    if x % 3 == 0:
        soma += x
        contador += 1

print(f'A soma de todos os {contador} algarismos é: {soma}')