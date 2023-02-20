#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

tupla = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print(f'Os numeros gerados foram: {tupla}')

print(f'O maior valor foi: {max(tupla)} e o menor valor foi: {min(tupla)}')