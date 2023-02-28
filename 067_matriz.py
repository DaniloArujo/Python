#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
#A) A soma de todos os valores pares digitados.  
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
soma2 = 0
maior_Segunda = 0

for x in range(0,3):
    for y in range(0,3):
        matriz [x][y] = int(input(f'Digite um valor para a posição [{x}][{y}]: '))
        if matriz[x][y] % 2 == 0:
            soma += matriz[x][y]

print()
for elem in matriz:
    print(elem)
print()
print(f'Soma dos numeros pares: {soma}')
print()

for x in range(0,3):
    soma2 += matriz[x][2]

print(f'Soma dos valores da terceira coluna: {soma2}')

for x in range(0,3):
    if matriz[1][x] > maior_Segunda:
        maior_Segunda = matriz[1][x]
print()

print(f'O maior numero da segunda coluna é: {maior_Segunda}')
