# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for item in range(5):
    lista.append(int(input('Digite um valor: ')))


print(lista)
print(f'O maior valor é {max(lista)}, que está na posição {lista.index(max(lista))}, e o menor valor é {min(lista)}, que está na posição {lista.index(min(lista))}')