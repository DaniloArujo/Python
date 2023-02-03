
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))

menor = num1

if num2 < num1 and num2 < num3:
    menor = num2

if num3 < num1 and num3 < num2:
    menor = num3

print(f'menor: {menor}')

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2

if num3 > num2 and num3 > num1:
    maior = num3

print(f'maior: {maior}')