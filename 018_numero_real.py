#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

num = float(input('Digite um valor: '))

print(f'Utilizando o metodo trunc da biblioteca math transformei o float {num} em {trunc(num)}, que é o numero sem a parte fracionada.')