#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0

for x in range(6):
    num = int(input('Digite um valor qualquer: '))
    if num > 0 and num % 2 == 0:
        soma += num

print(soma)