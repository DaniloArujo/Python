# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: Quantas vezes apareceu o valor 9. Em que posição foi digitado o primeiro valor 3. Quais foram os números pares.


tupla = (int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')))

print(tupla)
print(f'O numero 9 foi digitado {tupla.count(9)} vezes')

if 3 in (tupla):
    print(f'O numero 3 está na {tupla.index(3)+1} posição')

print('Os valores pares foram: ', end='')

for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')